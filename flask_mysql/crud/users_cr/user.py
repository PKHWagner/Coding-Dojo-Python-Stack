from mysqlconnection import connectToMySQL

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data ['first_name']
    self.last_name = data ['last_name']
    self.email = data ['email']
    self.created_at = data ['created_at']
    self.update_at = data ['update_at']
    
  @classmethod
  def save(cls, data):
    query = "INSERT INTO users (first_name, last_name, email) VALUES ( %(fname)s, %(lname)s, %(email)s);"
    return connectToMySQL('users_schema').query_db(query, data)

  @classmethod
  def show_users(cls):
    query = 'SELECT * FROM users;'
    results = connectToMySQL('users_schema').query_db(query)
    users_list = []
    for one_user in results:
      users_list.append(cls(one_user))
    return users_list

if __name__ == '__main__':
  app.run(debug=True, port=5001)