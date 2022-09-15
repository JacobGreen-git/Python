from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

mysql_db = "recipe_db"

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE
    @classmethod
    def create_recipe(cls, data):
        query ='INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s,%(user_id)s);'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(mysql_db).query_db(query)
        if len(results) > 0:
            all_recipes = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id':row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.creator = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    #UPDATE
    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(mysql_db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id':row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        creator = user_model.User(user_data)
        this_recipe.creator = creator
        return this_recipe

    #DELETE
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #VALIDATE
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 1:
            flash("Name required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("Description required")
            is_valid = False
        if len(form_data['instructions']) < 1:
            flash("Instructions required")
            is_valid = False
        if len(form_data['date_made']) < 1:
            flash("Date required")
            is_valid = False
        if "under_30" not in form_data:
            flash("Under 30 mins response required")
            is_valid = False
        return is_valid
