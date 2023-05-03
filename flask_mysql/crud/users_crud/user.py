from mysqlconnection import connectToMySQL

class User:
  DB = "users_schema"
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.update_at = data['update_at']
    
  @classmethod
  def show_users(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL(cls.DB).query_db(query)
    users_list = []
    for one_user in results:
      users_list.append(cls(one_user))
    return users_list
  
  @classmethod
  def save_user(cls, data):
    query = """INSERT INTO users (first_name, last_name, email)
            Values (%(fname)s, %(lname)s, %(email)s);"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @classmethod
  def get_one(cls, user_id):
    query = """SELECT * FROM users
            WHERE id =%(id)s;"""
    data = {'id': user_id }
    results = connectToMySQL(cls.DB).query_db(query, data)
    return cls(results[0])
    
  @classmethod
  def update(cls, data):
    query = """UPDATE users
            SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s
            WHERE id = %(id)s;"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  @classmethod
  def delete(cls, user_id):
    query = """DELETE FROM users
            WHERE id = %(id)s;"""
    results = connectToMySQL(cls.DB).query_db(query, {'id': user_id})
    return results
    
if __name__ =='__main__':
  app.run(debug=True, port=5001)