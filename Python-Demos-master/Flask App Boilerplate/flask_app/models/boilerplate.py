from flask_app.config.mysqlconnection import connectToMySQL
#TO AVOID CIRCULAR IMPORT FOLLOW THIS SYNTAX
#from models import FILENAME
#when referencing the other model make sure you call on the other model as follows: FILENAME.CLASSNAME

mysql_db = "YOUR_SCHEMA_NAME_GOES_HERE"

class Boilerplate:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']

    #CREATE
    @classmethod
    def save(cls, data):
        query ='INSERT INTO TABLE_NAME(COLUMN_NAME) VALUES(%(FORM_NAME)s);'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #READ ALL
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM TABLE_NAME;'
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
    def get_one(cls,data):
        query = 'SELECT * FROM TABLE_NAME WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        the_one_item = cls(results[0])
        return the_one_item
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = 'UPDATE TABLE_NAME SET COLUMN_NAME=%(FORM_NAME)s WHERE id=%(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results

    #DELETE
    @classmethod
    def destroy(cls, data):
        query = 'DELETE FROM TABLE_NAME WHERE id = %(id)s;'
        results = connectToMySQL(mysql_db).query_db(query, data)
        return results
    
   



