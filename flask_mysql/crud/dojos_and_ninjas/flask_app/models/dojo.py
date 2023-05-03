from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
  
  DB = "dojos_and_ninjas_schema"
  
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.ninjas = []
    
  @classmethod
  def show_dojos(cls):
    query = "SELECT * FROM dojos;"
    results = connectToMySQL(cls.DB).query_db(query)
    dojos_list = []
    for one_dojo in results:
      dojos_list.append(cls(one_dojo))
    return dojos_list
  
  @classmethod
  def save_dojos(cls, data):
    query = """INSERT INTO dojos (name)
            Values (%(name)s);"""
    result = connectToMySQL(cls.DB).query_db(query, data)
    return result
  
  @classmethod
  def show_dojo_with_ninjas(cls, data):
    query = """SELECT * FROM dojos
            LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;"""
    results = connectToMySQL(cls.DB).query_db(query, data)
    dojo = cls(results[0])
    for row in results:
      ninja_data = {
        'id': row['ninjas.id'],
        'first_name': row['first_name'],
        'last_name': row['last_name'],
        'age': row['age'],
        'created_at': row['ninjas.created_at'],
        'updated_at': row['ninjas.updated_at']
      }
      dojo.ninjas.append(ninja.Ninja(ninja_data))
    return dojo