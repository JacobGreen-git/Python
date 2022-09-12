from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save_ninja(request.form)
    return redirect ('/dojos')