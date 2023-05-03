# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
  DB="first_flask"
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.occupation = data['occupation']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
# Now we use class methods to query our database
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM friends;"
  # make sure to call the connectToMySQL function with the schema you are targeting.
    results = connectToMySQL(cls.DB).query_db(query)
  # Create an empty list to append our instances of friends
    friends = []
  # Iterate over the db results and create instances of friends with cls.
    for friend in results:
      friends.append( cls(friend) )
    return friends
  
  
#CRUD Methods
  #Create
  @classmethod
  def save(cls, data):
    query = """INSERT INTO friends (first.name, last_name, occupation,)
            VALUES (%(first_name)s,%(last_name)s,%(occ)s);"""
    result= connectToMySQL(cls.DB).query_db(query, data)
    return result
  
  #Read - above get_all function is also a Read Method
  @classmethod
  def get_friend_by_id(cls, id):
    query="""SELECT * FROM Friends
            WHERE id = %(id)s;"""
    results = connectToMySQL(cls.DB).query_db(query, {'id': id})
    return cls(results[0])
  
  #Update
  @classmethod
  def update(cls, data):
    query = """UPDATE friends
            SET first_name=%(first_name)s, last_name=%(last_name)s, occupation=%(occ)s
            WHERE id = %(id)s;"""
    return connectToMySQL(cls.DB).query_db(query, data)
  
  #Delete
  @classmethod
  def delete(cls, id):
    query = """DELETE FROM friends
            WHERE id = %(id)s;"""
    results = connectToMySQL(cls.DB).query_db(query, {'id':id})
    return results
    

