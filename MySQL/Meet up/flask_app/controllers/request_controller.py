from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.request_model import Request
from flask_app.models.user_model import User
from flask_app.controllers import user_controller

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_requests = Request.get_all_requests()
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('welcome.html', all_requests=all_requests, logged_user=logged_user)

@app.route('/requests/new')
def add_request():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('requests_new.html')

@app.route('/requests/create', methods=['POST'])
def process_request():
    if 'user_id' not in session:
        return redirect('/')
    if not Request.validator(request.form):
        return redirect ("/requests/new")
    data ={
        **request.form,
        'user_id': session['user_id']
    }
    id = Request.create_request(data)
    return redirect(f'/requests/{id}') #redirects us to the show one page

@app.route('/requests/<int:id>/delete')
def delete_request(id):
    if 'user_id' not in session:
        return redirect('/')
    requested = Request.get_by_id({'id':id})
    # if not int(session['user_id']) == requested.user_id:
    #     flash("Cannot delete other's requests")
    #     return redirect('/welcome')
    requested.delete({'id':id})
    return redirect('/welcome')

@app.route('/requests/<int:id>/edit')
def edit_request(id):
    if 'user_id' not in session:
        return redirect('/')
    requested = Request.get_by_id({'id':id})
    # if not int(session['user_id']) == requested.user_id:
    #     flash("Cannot edit other's requests")
    #     return redirect('/welcome')
    request = requested.get_by_id({'id':id})
    return render_template('request_edit.html', request=request)

@app.route("/requests/<int:id>/update", methods=['POST'])
def update_request(id):
    if 'user_id' not in session:                        #protection code
        return redirect('/')                            #protection code
    requested = Request.get_by_id({'id':id})
    # if not int(session['user_id']) == requested.user_id:   #protection code
    #     flash("Cannot edit other's requests")            #protection code
    #     return redirect('/welcome')                     #protection code
    if not requested.validator(request.form):
        return redirect(f"/requests/{id}/edit")
    data = {
        **request.form,
        'user_id': session['user_id'],
        'id': id
    }
    print(data)
    requested.update_request(data)
    return redirect('/welcome')

@app.route('/requests/<int:id>')
def show_requests(id):
    request = Request.get_by_id({'id':id})
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('view_one.html', request=request, logged_user=logged_user)

@app.route('/my_requests')
def my_reccipes():
    user = User.get_by_id({'id':session['user_id']})
    return render_template('my_requests.html', logged_user=user)