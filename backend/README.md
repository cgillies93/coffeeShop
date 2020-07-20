# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`



## API Reference

Endpoints
- GET '/drinks'
- GET '/drinks-detail'
- POST '/drinks'
- PATCH '/drinks/<int:id>'
- DELETE '/drinks/<int:id>'


GET '/drinks'
- Fetches a list of drink objects in their short form representation
- Request Arguments: None
- Returns: An object with list of Drink objects, each with three key:value pairs,
  (id-Integer, title-String, and recipe which contains a list of ingredient dictionary
  objects. Each ingredient dictionary has the key:value pairs, (color-String,
  name-"String", parts-Integer)

The Drink Object in Short Form
{
  id: 1
recipe: [{color: "#ede8dd", name: "Milk", parts: 2}, {color: "#543308", name: "Coffee", parts: 1}]
title: "Caffe Latte"
}

The Drink Object in Long Form
{
    "id": 1,
    "recipe": [
      {
        "color": "#ede8dd",
        "name": "Milk",
        "parts": 2
      },
      {
        "color": "#543308",
        "name": "Coffee",
        "parts": 1
      }
    ],
    "title": "Caffe Latte"
}


GET '/drinks-detail'
- Fetches a list of drink objects in their long form representation
- Request Arguments: None
- Returns: An object with list of Drink objects, each with three key:value pairs,
  (id-Integer, title-String, and recipe which contains a list of ingredient dictionary
  objects. Each ingredient dictionary has the key:value pairs, (color-String,
  name-"String", parts-Integer)

The Drink Object in Long Form
{
    "id": 1,
    "recipe": [
      {
        "color": "#ede8dd",
        "name": "Milk",
        "parts": 2
      },
      {
        "color": "#543308",
        "name": "Coffee",
        "parts": 1
      }
    ],
    "title": "Caffe Latte"
}


POST '/drinks'
- Sends a drink object to the database
- Request Arguments: None
- Returns: An object with three key:value pairs, 'created': Integer, 'success': Boolean,
and 'drinks', a list containing the created Drink object

{
  "success": true,
  "created": 7,
  "drinks": [Drink object in long form]
}

The Drink Object in Long Form
{
    "id": 1,
    "recipe": [
      {
        "color": "#ede8dd",
        "name": "Milk",
        "parts": 2
      },
      {
        "color": "#543308",
        "name": "Coffee",
        "parts": 1
      }
    ],
    "title": "Caffe Latte"
}


PATCH 'drinks/<int:id>'
- Sends updated key:value pairs of the selected Drink object to the database
- Request Arguments: id
- Returns: An object with three key:value pairs, 'created': Integer, 'success': Boolean,
  and 'drinks', a list containing the created Drink object

{
  "success": true,
  "updated": 7
  "drinks": [Drink object in long form]
}

The Drink Object in Long Form
{
    "id": 1,
    "recipe": [
      {
        "color": "#ede8dd",
        "name": "Milk",
        "parts": 2
      },
      {
        "color": "#543308",
        "name": "Coffee",
        "parts": 1
      }
    ],
    "title": "Caffe Latte"
}


DELETE 'drinks/<int:id>'
- Deletes the selected Drink object from the database
- Request Arguments: id
- Returns: An object with two key:value pairs, 'delete': Integer, 'success': Boolean

{
  "delete": 26,
  "success": true
}
