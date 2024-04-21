
from flask import request, jsonify
from datetime import datetime, timezone
from app import app
from shopping_list import shopping_list

@app.route('/', methods=['GET'])
def index():
    return '''
Hello There! ~General K.~ 
Welcome to the Shopping List API!
'''

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
    if not request.json:
        return {'error': 'Your content type must be in json'}, 400
    
    # Check for missing required fields (ingredient and description)
    data = request.json
    missing_fields = []
    if 'ingredient' not in data:
        missing_fields.append('ingredient')
    if 'description' not in data:
        missing_fields.append('description')
    if missing_fields:
        return {'error': f'Missing required fields: {", ".join(missing_fields)}'}, 400
    
    ingredient_id = len(shopping_list) + 1  # Generate a new ingredient_id for the new task
    new_ingredient = {
        'ingredient_id': ingredient_id,
        'ingredient': data['ingredient'],
        'description': data['description'],
        'status': False,
        'date_added': datetime.now(timezone.utc).strftime('%Y-%m-%d')
        }
    # Add the new ingredient to the shopping_list
    shopping_list.append(new_ingredient)
    # Return a success message and the updated shopping_list
    return new_ingredient, 201

