from flask_app.config.mysqlconnection import connectToMySQL

mysql_db = "users_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query ='INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);'
        result = connectToMySQL(mysql_db).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(mysql_db).query_db(query)
        print("============================")
        print("This is the result we got from our get all query...", results)
        print("============================")
        users = []
        for u in results:
            users.append(cls(u))
        print("============================")
        print("This is our list of users...", users)
        print("============================")
        return users
    
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        the_one_item = cls(results[0])
        return the_one_item
    
    @classmethod
    def update(cls, data):
        print("============================")
        print("I MADE IT TO THE UPDATE", data)
        print("============================")
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    @classmethod
    def destroy(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results
    
   


