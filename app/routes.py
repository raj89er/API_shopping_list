
from flask import request, jsonify
from datetime import datetime, timezone
from app import app
from shopping_list import shopping_list


users_list = []


@app.route('/', methods=['GET'])
def index():
    return '''
Hello There! ~General K.~ 
Welcome to the Shopping List API!
'''

# User Endpoints
@app.route('/users', methods=['POST'])
def create_user():
    # Error handling
    if not request.is_json:
        return {'error': 'Your content type must be in json'}, 400
    
    data = request.json
    missing_fields = []
    for field in ['firstName' , 'lastName' , 'username' , 'email' , 'password']:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f'You are missing the following required fields: {", ".join(missing_fields)}'}, 400
    
    # Check if username or email already exists
    for user in users_list:
        if user['email'] == new_user['email'] or user['username'] == new_user['username']:
            return {'error': 'User with that username and/or email already exists'}, 409
    # Create a new user with the data received
    new_user = {
        'user_id': len(users_list) + 1,
        'username': data.get('username'),
        'name_first': data.get('description'),
        'name_last': data.get('lastName'),
        'email': data.get('email'),
        'password': data.get('password'),
        'date_joined': datetime.now(timezone.utc).strftime('%Y-%m-%d')
        }
    
    # Add the new user to the users_list
    users_list.append(new_user)
    # Return a success message
    return new_user, 201


# Ingredients Endpoints
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    return {'ingredients': shopping_list}

@app.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    for ingredient in shopping_list:
        if ingredient['ingredient_id'] == ingredient_id:
            return ingredient
    return {'error': f'ingredient with ID "{ingredient_id}" does not exist'}, 404

@app.route('/ingredients', methods=['POST'])
def create_ingredient():
    # Error handling
    if not request.is_json:
        return {'error': 'Your content type must be in json'}, 400
    
    # Check for missing required fields (ingredient and description)
    data = request.json
    missing_fields = []
    for field in ['ingredient', 'description']:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f'You are missing the following required fields: {", ".join(missing_fields)}'}, 400
    
    ingredient_id = len(shopping_list) + 1  # Generate a new ingredient_id for the new task
    new_ingredient = {
        'ingredient_id': ingredient_id,
        'ingredient': data['ingredient'],
        'description': data['description'],
        'status': False,
        'date_added': datetime.now(timezone.utc).strftime('%Y-%m-%d')
        }
    # Check if ingredient already exists
    for ingredient in shopping_list:
        if ingredient['ingredient'] == new_ingredient['ingredient']:
            return {'error': 'Ingredient with that name already exists'}, 409
    # Add the new ingredient to the shopping_list
    shopping_list.append(new_ingredient)
    # Return a success message and the updated shopping_list
    return new_ingredient, 201

