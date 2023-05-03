from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
def pointer():
  return redirect('/users')

@app.route('/users')
def show_users():
  users = User.show_users()
  return render_template('read.html', all_users=users)

@app.route('/users/new')
def create_new_user():
  return render_template('create.html')

@app.route('/users/process', methods=['POST'])
def process_user():
  data = {
    "fname": request.form["fname"],
    "lname": request.form["lname"],
    "email": request.form["email"]
  }
  User.save(data)
  print(data)
  return redirect('/users')



if __name__ == '__main__':
  app.run(debug=True, port=5001)