from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
  
  DB = 'z_exam_prep'
  
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.email = data ['email']
    self.password = data ['password']
    self.created_at = data ['created_at']
    self.updated_at = data ['updated_at']
    
  @classmethod
  def create(cls, data):
    query = """INSERT INTO users (name, email, password)
            VALUES (%(name)s, %(email)s, %(password)s)
            ;"""
    return connectToMySQL(cls.DB).query_db(query, data)

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL(cls.DB).query_db(query)
    users_list = []
    for user in results:
      users_list.append(cls(user))
    return users_list
    
  @classmethod
  def get_with_id(cls, data):
    query = """SELECT * FROM users
            WHERE id = %(id)s
            ;"""
    results = connectToMySQL(cls.DB).query_db(query, data)
    return cls(results[0])
    
  # @staticmethod
  # def validate_user(user):
  #   is_valid = True
  #   if len(user['first_name'])<2:
  #     flash('First Name must be at least 2 characters.')
  #     is_valid = False
  #   if len(user['last_name'])<2:
  #     flash('Last Name must be at least 2 characters.')
  #     is_valid = False
  #   if not EMAIL_REGEX.match(user['email']):
  #     flash('Invalid email address')
  #     is_valid = False
  #   if len(user['password'])<8:
  #     flash('Password must be at least 8 characters.')
  #     is_valid = False
  #   if user['password'] != user['confirm_password']:
  #     flash('Your passwords do not match.')
  #     is_valid = False
  #   return is_valid    