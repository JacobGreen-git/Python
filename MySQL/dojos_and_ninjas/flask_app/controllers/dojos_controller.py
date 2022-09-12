from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojos import Dojo


@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def home():
    all_dojos = Dojo.get_all_dojos()
    return render_template("home.html", all_dojos=all_dojos)

@app.route('/dojo/create',methods=['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect ('/dojos')

@app.route('/ninja/add')
def add_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('add_ninja.html', all_dojos=all_dojos)

@app.route('/dojo/<int:id>/ninjas')
def view_ninjas(id):
    one_dojo = Dojo.get_one_dojo_with_ninjas()
    return render_template('view_ninjas.html', one_dojo = one_dojo)
