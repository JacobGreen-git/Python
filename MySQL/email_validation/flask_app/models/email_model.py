from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(cls):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(cls['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def add_email(data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        results = connectToMySQL('emails_db').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('emails_db').query_db(query)
        all_emails = []
        for row_from_db in results:
            email_instance = cls(row_from_db)
            all_emails.append(email_instance)
        return all_emails
