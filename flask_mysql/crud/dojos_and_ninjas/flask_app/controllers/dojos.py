from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def show_dojos():
  dojos=Dojo.show_dojos()
  return render_template('dojos.html', all_dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
  Dojo.save_dojos(request.form)
  return redirect('/dojos')

@app.route('/ninjas')
def ninja():
  dojo=Dojo.show_dojos()
  return render_template('create_ninjas.html', all_dojos=dojo)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
  Ninja.save_ninjas(request.form)
  return redirect(f"/dojos/{request.form['dojo_id']}")

@app.route('/dojos/<int:dojo_id>')
def show_dojo_with_ninjas(dojo_id):
  data = {
    'id': dojo_id
  }
  return render_template('dojo_ninjas.html', dojo = Dojo.show_dojo_with_ninjas(data))