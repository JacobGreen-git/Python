from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.car_model import Car
from flask_app.controllers import user_controller

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_cars = Car.get_all_cars()
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('dashboard.html', all_cars=all_cars, logged_user=logged_user)

@app.route('/cars/new')
def add_car():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('cars_new.html')

@app.route('/cars/create', methods=['POST'])
def process_car():
    if 'user_id' not in session:
        return redirect('/')
    if not Car.validator(request.form):
        return redirect ("/cars/new")
    data ={
        **request.form,
        'user_id': session['user_id']
    }
    Car.create_car(data)
    return redirect('/dashboard')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    car.delete({'id':id})
    return redirect('/dashboard')

@app.route('/cars/<int:id>/edit')
def edit_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    return render_template('car_edit.html', car=car)

@app.route("/cars/<int:id>/update", methods=['POST'])
def update_car(id):
    if 'user_id' not in session:                        #protection code
        return redirect('/')                            #protection code
    if not Car.validator(request.form):
        return redirect(f"/cars/{id}/edit")
    data = {
        **request.form,
        'user_id': session['user_id'],
        'id': id
    }
    print(data)
    Car.update_car(data)
    return redirect('/dashboard')

@app.route('/cars/<int:id>')
def show_cars(id):
    car = Car.get_by_id({'id':id})
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('view_one.html', car=car, logged_user=logged_user)
