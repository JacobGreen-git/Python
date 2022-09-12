from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s,"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query, data)
        if len(results) > 0:
            dojo_instance = cls(results[0])
            return dojo_instance
        return False

    @classmethod
    def get_one_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query, data)
        # print(results)
        if len(results) > 0:
            print(results)
            dojo_instance = cls(results[0])
            ninja_list = []
            for row_from_db in results:
                ninja_data = {
                    'id': row_from_db['ninjas.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db ['last_name'],
                    'age': row_from_db['age'],
                    'dojo_id': row_from_db['dojo_id'],
                    'created_at': row_from_db['ninjas.created_at'],
                    'updated_at': row_from_db['ninjas.updated_at']
                }
                ninja_instance = ninjas_model.Ninja(ninja_data)
                ninja_list.append(ninja_instance)
            dojo_instance.ninja_list = ninja_list
            return dojo_instance
        return False


    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query,data)
        return results