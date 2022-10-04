from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import request_model
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


mysql_db = "user_review_db"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.review_id = data['review_id']
        self.review_user_id = data['review_user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #CREATE
    @classmethod
    def create_user(cls, data):
        query ='INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #READ ALL
    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(mysql_db).query_db(query)
        print("============================")
        print("This is the result we got from our get all query...", results)
        print("============================")
        empty_list = []
        for u in results:
            empty_list.append(cls(u))
        print("============================")
        print("This is our list of users...", empty_list)
        print("============================")
        return empty_list
    
    #READ ONE
    @classmethod
    def get_one_user(cls,data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        the_one_item = cls(results[0])
        return the_one_item
    
    #UPDATE
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET COLUMN_NAME=%(FORM_NAME)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #DELETE
    @classmethod
    def destroy_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #GET BY ID WITH JOIN
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN requests on users.id = requests.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(mysql_db).query_db(query, data)
        if len(results) < 1:
            return False
        user = cls(results[0])
        list_of_requests = []
        for row in results:
            if row['requests.id'] == None:
                break
            recipe_data = {
                **row,
                'id': row['requests.id'],
                'created_at': row['requests.created_at'],
                'updated_at': row['requests.updated_at']
            }
            this_recipe = request_model.Recipe(recipe_data)
            list_of_requests.append(this_recipe)
        user.requests = list_of_requests
        return user

    #GET BY MAIL TO VALIDATE
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(mysql_db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    #VALIDATE
    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash("First name required", "reg")
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash("Last name required", "reg")
            is_valid = False
        if len(user_data['email']) < 2:
            flash("Email required", 'reg')
            is_valid = False
        if len(user_data['password']) < 8:
            flash("Password must be at least 8 characters", "reg")
            is_valid = False
        elif not user_data['password'] == user_data['confirm_pass']:
            flash("Passwords do not match", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid Email", "reg")
            is_valid=False
        else:
            data = {
                'email':user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("Email already in use", 'reg')
                is_valid = False
        return is_valid