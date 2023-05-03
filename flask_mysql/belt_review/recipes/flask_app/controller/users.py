from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def sign_up():
  return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
  if not User.validate_user(request.form):
    return redirect('/')
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': bcrypt.generate_password_hash(request.form['password'])
  }
  id = User.create_user(data)
  session['user_id'] = id
  return redirect('/dashboard')

@app.route ('/dashboard')
def user_dashboard():
  if 'user_id' not in session:
    return redirect('/logout')
  user = User.get_with_id({'id': session['user_id']})
  if not user:
    return redirect('/logout')
  return render_template('user_dashboard.html', user=user, recipes = Recipe.display_all_recipes())

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
  return redirect('/dashboard')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')