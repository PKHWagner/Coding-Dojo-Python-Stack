from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes/new')
def new_recipe_form():
  if 'user_id' not in session:
    return redirect('/logout')
  return render_template('create_recipe.html')

@app.route('/recipes/new/add', methods=['POST'])
def add_recipe():
  if 'user_id' not in session:
    return redirect('/')
  if not Recipe.validate_recipe(request.form):
    return redirect('/recipes/new')
  data = {
    'user_id': session['user_id'],
    'name': request.form['name'],
    'under_30': request.form['under_30'],
    'description': request.form['description'],
    'instructions': request.form['instructions'],
    'date_cooked': request.form['date_cooked']
    }
  Recipe.create_recipe(data)
  return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def remove_recipe(id):
  if 'user_id' not in session:
    return redirect('/')
  Recipe.delete_recipe({'id':id})
  return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def display_recipe(id):
  user = User.get_with_id({'id': session['user_id']})
  if 'user_id' not in session:
    return redirect('/')
  return render_template('recipe_card.html', user=user, recipe = Recipe.get_with_id({'id': id}))

@app.route('/recipes/update/<int:id>')
def update_form(id):
  if 'user_id' not in session:
    return redirect('/')
  return render_template('update_recipe.html', recipe = Recipe.get_with_id({'id': id}))
  
@app.route('/recipes/update/handle/<int:id>', methods=['POST'])
def update_recipe(id):
  if 'user_id' not in session:
    return redirect('/')
  if not Recipe.validate_recipe(request.form):
    return redirect(f'/recipes/update/{id}')
  data = {
    'id': id,
    'name': request.form['name'],
    'under_30': request.form['under_30'],
    'description': request.form['description'],
    'instructions': request.form['instructions'],
    'date_cooked': request.form['date_cooked']
    }
  Recipe.revise_recipe(data)
  return redirect('/dashboard')