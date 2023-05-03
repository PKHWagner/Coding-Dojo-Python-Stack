from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_new_user():
  if not User.validate_user(request.form):
    return redirect('/')
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': bcrypt.generate_password_hash(request.form['password'])
  }
  id = User.create(data)
  session['user_id'] = id
  return redirect('/success')

@app.route('/success')
def success():
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': session['user_id']
  }
  return render_template('success.html', user = User.get_with_id(data))

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  data = {
    'email': request.form['email']
  }
  user_in_db = User.get_with_email(data)
  if not user_in_db:
    flash('Invalid Log In Info!')
    return redirect('/')
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    flash('Invalid Log In Info!')
    return redirect('/')
  session['user_id'] = user_in_db.id
  return redirect('/success')