from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.boilerplate import Boilerplate

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('boilerplate.html')