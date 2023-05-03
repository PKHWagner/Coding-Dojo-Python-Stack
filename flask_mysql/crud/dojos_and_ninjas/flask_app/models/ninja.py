from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
  
  DB = 'dojos_and_ninjas_schema'
  
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
  @classmethod
  def save_ninjas(cls, data):
    query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            Values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"""
    result = connectToMySQL(cls.DB).query_db(query, data)
    return result

    