from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['post'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/users/show/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    one_user = User.get_one(data)
    return render_template('one_user.html', only_one_user = one_user)

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data={
        'id':id
    }
    user = User.get_one(data)

    return render_template('edit_user.html', user_we_are_editing = user)

@app.route('/users/update', methods=['post'])
def users_update():
    User.update(request.form)
    return redirect('/')

@app.route('/user/destroy/<int:id>')
def destroy_user(id):
    data={
        'id':id
    }
    User.destroy(data)
    return redirect('/')
