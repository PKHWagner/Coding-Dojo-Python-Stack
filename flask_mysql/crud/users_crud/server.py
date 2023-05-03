from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def skip_home():
  return redirect('/users')

@app.route('/users')
def show_users():
  users = User.show_users()
  return render_template('users.html', all_users=users)

@app.route('/users/new')
def add_user():
  return render_template('create_new.html')

@app.route('/users/process', methods=['POST'])
def process_new_user():
  data = {
    'fname': request.form['fname'],
    'lname': request.form['lname'],
    'email': request.form['email']
  }
  User.save_user(data)
  print(data)
  return redirect('/users')

@app.route('/users/show/<int:user_id>')
def show_single_user(user_id):
  user=User.get_one(user_id)
  return render_template('user_card.html', user=user)

@app.route('/users/update/<int:user_id>')
def edit_user(user_id):
  return render_template('edit_user.html', user=User.get_one(user_id))

@app.route('/users/update', methods=['POST'])
def update_user():
  User.update(request.form)
  return redirect('/users')

@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):
  User.delete(user_id)
  return redirect('/users')

if __name__ == '__main__':
  app.run(debug=True, port=5001)