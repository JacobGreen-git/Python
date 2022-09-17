from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask_app.controllers import user_controller

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_recipes = Recipe.get_all_recipes()
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('welcome.html', all_recipes=all_recipes, logged_user=logged_user)

@app.route('/recipes/new')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipes_new.html')

@app.route('/recipes/create', methods=['POST'])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect ("/recipes/new")
    data ={
        **request.form,
        'user_id': session['user_id']
    }
    id = Recipe.create_recipe(data)
    return redirect(f'/recipes/{id}') #redirects us to the show one page

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Cannot delete other's recipes")
        return redirect('/welcome')
    Recipe.delete({'id':id})
    return redirect('/welcome')

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Cannot edit other's recipes")
        return redirect('/welcome')
    recipe = Recipe.get_by_id({'id':id})
    return render_template('recipe_edit.html', recipe=recipe)

@app.route("/recipes/<int:id>/update", methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:                        #protection code
        return redirect('/')                            #protection code
    recipe = Recipe.get_by_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:   #protection code
        flash("Cannot edit other's recipes")            #protection code
        return redirect('/welcome')                     #protection code
    if not Recipe.validator(request.form):
        return redirect(f"/recipes/{id}/edit")
    data = {
        **request.form,
        'user_id': session['user_id'],
        'id': id
    }
    print(data)
    Recipe.update_recipe(data)
    return redirect('/welcome')

@app.route('/recipes/<int:id>')
def show_recipes(id):
    recipe = Recipe.get_by_id({'id':id})
    user_data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('view_one.html', recipe=recipe, logged_user=logged_user)

@app.route('/my_recipes')
def my_reccipes():
    user = User.get_by_id({'id':session['user_id']})
    return render_template('my_recipes.html', logged_user=user)