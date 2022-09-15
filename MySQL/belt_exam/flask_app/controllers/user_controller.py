import re
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user_model

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('login.html')

@app.route('/user/register', methods=["POST"])
def register():
    if not user_model.User.validate(request.form):
        return redirect ('/home')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = user_model.User.create_user(data)
    print(id)
    session['user_id'] = id
    return redirect ('/welcome')

@app.route('/user/login', methods=['POST'])
def login():
    data = {'email':request.form['email']}
    user_in_db = user_model.User.get_by_email(data)
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect ('/home')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info', 'log')
        return redirect ('/home')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect ('/')