import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# ROUTES
@app.route('/drinks', methods=['GET'])
def drinks():
    try:
        drinks = Drink.query.all()
        drinks_short = [drink.short() for drink in drinks]
        return jsonify({
            'success': True,
            'drinks': drinks_short
            }), 200
    except:
        abort(404)


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_detail(jwt):
    drinks = Drink.query.all()
    try:
        drinks_long = [drink.long() for drink in drinks]
        return jsonify({
            'success': True,
            'drinks': drinks_long
            }), 200
    except:
        abort(401)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(jwt):
    data = request.get_json()
    title = data.get('title')
    recipe = data.get('recipe')
    drink = Drink(title=title, recipe=json.dumps(recipe))
    try:
        drink.insert()

        return jsonify({
            'success': True,
            'created': drink.id,
            'drinks': [drink.long()]
        }), 200
    except:
        abort(422)


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id):
    drink = Drink.query.filter(Drink.id == id).first()
    data = request.get_json()

    try:
        drink.title = data.get('title')
        recipe = data.get('recipe')
        drink.recipe = json.dumps(recipe)

        drink.update()
        return jsonify({
            'success': True,
            'updated': drink.id,
            'drinks': [drink.long()]
        }), 200
    except:
        abort(404)


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, id):
    drink = Drink.query.filter(Drink.id == id).first()

    try:
        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink.id
        }), 200
    except:
        abort(404)


# Error Handling
@app.errorhandler(AuthError)
def forbidden(AuthError):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Auth Error"
    }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
         }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable Entity"
        }), 422
