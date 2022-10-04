from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

mysql_db = "cars_and_users_db"

class Car:
    def __init__(self,data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.price = data['price']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE
    @classmethod
    def create_car(cls, data):
        query ='INSERT INTO cars (make, model, year, price, description, user_id) VALUES(%(make)s,%(model)s,%(year)s,%(price)s,%(description)s,%(user_id)s);'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_all_cars(cls):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id;"
        results = connectToMySQL(mysql_db).query_db(query)
        if len(results) > 0:
            all_cars = []
            for row in results:
                this_car = cls(row)
                user_data = {
                    **row,
                    'id':row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_car.creator = this_user
                all_cars.append(this_car)
            return all_cars
        return []

    #UPDATE
    @classmethod
    def update_car(cls, data):
        query = 'UPDATE cars SET make=%(make)s, model=%(model)s, year=%(year)s, price=%(price)s, description=%(description)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM cars JOIN users on users.id = cars.user_id WHERE cars.id = %(id)s;"
        results = connectToMySQL(mysql_db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_car = cls(row)
        user_data = {
            **row,
            'id':row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        creator = user_model.User(user_data)
        this_car.creator = creator
        return this_car

    #DELETE
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM cars WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #VALIDATE
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['make']) < 1:
            flash("Make required")
            is_valid = False
        if len(form_data['model']) < 1:
            flash("Model required")
            is_valid = False
        if len(form_data['year']) < 1:
            flash("Year required")
            is_valid = False
        if len(form_data['price']) < 1:
            flash("Date required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("Description required")
            is_valid = False
        return is_valid
