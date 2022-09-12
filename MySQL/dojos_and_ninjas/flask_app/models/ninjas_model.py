from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninja(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query)
        all_ninjas = []
        for row_from_db in results:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s);"
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query,data)
        return results