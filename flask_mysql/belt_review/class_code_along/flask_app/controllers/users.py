from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def home():
  return render_template('index.html', user=User.get_all())

@app.route('/user/login', methods=['POST'])
def login():
  session['id'] = request.form['id']
  return redirect('/dashboard')

