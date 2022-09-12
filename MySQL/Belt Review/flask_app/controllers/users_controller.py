from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

Bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template ('index.html')

# @app.route('/dojos')
# def home():
#     all_dojos = Dojo.get_all_dojos()
#     return render_template("home.html", all_dojos=all_dojos)

# @app.route('/dojo/create',methods=['POST'])
# def create_dojo():
#     Dojo.save_dojo(request.form)
#     return redirect ('/dojos')

# @app.route('/ninja/add')
# def add_ninja():
#     all_dojos = Dojo.get_all_dojos()
#     return render_template('add_ninja.html', all_dojos=all_dojos)

# @app.route('/dojo/<int:id>')
# def view_ninjas(id):
#     one_dojo = Dojo.get_one_dojo({'id':id})
#     # one_dojo_with_ninjas = Dojo.get_one_dojo_with_ninjas({'id':id})
#     return render_template('view_ninjas.html', one_dojo=one_dojo)
