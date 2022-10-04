from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

mysql_db = "user_review_db"

class Request:
    def __init__(self,data):
        self.id = data['id']
        self.game = data['game']
        self.players_req = data['players_req']
        self.rating_min = data['rating_min']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE
    @classmethod
    def create_request(cls, data):
        query ='INSERT INTO requests (game, players_req, rating_min, date_made, under_30, user_id) VALUES(%(game)s,%(players_req)s,%(rating_min)s,%(user_id)s);'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_all_requests(cls):
        query = "SELECT * FROM requests JOIN users ON requests.user_id = users.id;"
        results = connectToMySQL(mysql_db).query_db(query)
        if len(results) > 0:
            all_requests = []
            for row in results:
                this_request = cls(row)
                user_data = {
                    **row,
                    'id':row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_request.creator = this_user
                all_requests.append(this_request)
            return all_requests
        return []

    #UPDATE
    @classmethod
    def update_request(cls, data):
        query = 'UPDATE requests SET game=%(game)s, players_req=%(players_req)s, rating_min=%(rating_min)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM requests JOIN users on users.id = requests.user_id WHERE requests.id = %(id)s;"
        results = connectToMySQL(mysql_db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_request = cls(row)
        user_data = {
            **row,
            'id':row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        creator = user_model.User(user_data)
        this_request.creator = creator
        return this_request

    #DELETE
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM requests WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #VALIDATE
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['game']) < 1:
            flash("game required")
            is_valid = False
        if len(form_data['players_req']) < 1:
            flash("players_req required")
            is_valid = False
        if len(form_data['rating_min']) < 1:
            flash("rating_min required")
            is_valid = False
        return is_valid
