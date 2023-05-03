from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Recipe:
  
  DB = 'recipes_many_to_many'
  
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.under_30 = data['under_30']
    self.description = data['description']
    self.instructions = data['instructions']
    self.date_cooked = data ['date_cooked']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.liked_by = []
    self.publisher = None
    
  def is_liked_by(self, id):
    found_user = None
    for user in self.liked_by:
      if user.id == id:
        found_user = user
    return found_user
  
  @classmethod
  def create_recipe(cls, data):
    query = """
            INSERT INTO recipes (name, under_30, description, instructions, date_cooked)
            VALUES (%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_cooked)s)
            ;"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  # @classmethod
  # def display_all_recipes(cls):
  #   query = """
  #           SELECT * FROM recipes
  #           LEFT JOIN likes ON likes.recipe_id = recipes.id
  #           LEFT JOIN users ON users.id = likes.user_id
  #           WHERE recipes.id = %(id)s
  #           ;"""
  #   results = connectToMySQL(cls.DB).query_db(query)
  #   recipes = []
  #   for data in results:
  #     that_recipe = cls(data)
  #     user_info = {
  #       'id': data['users.id'],
  #       'first_name': data['first_name'],
  #       'last_name': data['last_name'],
  #       'email': data['email'],
  #       'password': '',
  #       'created_at': data['users.created_at'],
  #       'updated_at': data ['users.updated_at']
  #     }
  #     that_recipe.publisher = user.User(user_info)
  #     recipes.append(that_recipe)
  #   return recipes
  
  @classmethod
  
  def display_all_recipes(cls):
    from flask_app.models.user import User 
    query = """
            SELECT * FROM recipes
            LEFT JOIN likes ON likes.recipe_id = recipes.id
            LEFT JOIN users ON users.id = likes.user_id
            WHERE recipes.id = %(id)s
            ;"""
    results = connectToMySQL(cls.DB).query_db(query)
    if results:
      recipe = cls(results[0])
      for data in results:
        recipe.liked_by.append(User({
          'id': data['users.id'],
          'first_name': data['first_name'],
          'last_name': data['last_name'],
          'email': data['email'],
          'password': '',
          'created_at': data['users.created_at'],
          'updated_at': data ['users.updated_at']
        }))
      return recipe
    return None
  
  @classmethod
  def delete_recipe(cls, data):
    query = """
            DELETE FROM recipes
            WHERE id = %(id)s
            ;"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @classmethod
  def get_with_id(cls, data):
    query = """
            SELECT * FROM recipes
            JOIN users on recipes.user_id = users.id
            WHERE recipes.id = %(id)s
            ;"""
    result = connectToMySQL(cls.DB).query_db(query, data)
    if not result:
      return False
    data = result[0]
    that_recipe = cls(data)
    user_info = {
      'id': data['users.id'],
      'first_name': data['first_name'],
      'last_name': data['last_name'],
      'email': data['email'],
      'password': '',
      'created_at': data['created_at'],
      'updated_at':  data['updated_at']
    }
    that_recipe.publisher = user.User(user_info)
    return that_recipe
  
  @classmethod
  def revise_recipe(cls, data):
    query = """
            UPDATE recipes
            SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s
            WHERE id = %(id)s
            ;"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @staticmethod
  def validate_recipe(recipe):
    is_valid = True
    if len(recipe['name'])<3:
      flash('Recipe Name has to be at least 3 characters long!')
      is_valid = False
    if len(recipe['description'])<3:
      flash('Recipe Description has to be at least 3 characters long!')
      is_valid = False
    if len(recipe['instructions'])<3:
      flash('Recipe Instructions have to be at least 3 characters long!')
      is_valid = False
    if 'under_30' not in recipe:
      flash('Please specify if recipe took longer than 30 minutes to make!')
      is_valid = False
    if recipe['date_cooked'] == '00':
      flash('Please specify when the recipe was cooked for the first time!')
      is_valid = False
    return is_valid