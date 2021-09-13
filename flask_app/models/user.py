from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(form_data):
        is_valid = True
        if len(form_data['fname']) <= 3:
            flash('First name must be at least 3 characters.')
            is_valid = False
        if len(form_data['lname']) <= 3:
            flash('Last name must be at least 3 characters long')
            is_valid = False
        if len(form_data['email']) <= 3:
            flash('Email must be at least 3 characters long')
            is_valid = False
        return is_valid
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('users').query_db(query, data)
    @classmethod
    def select_all_users(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def one_user(cls, data):
        query = 'SELECT * FROM users WHERE id = %(user_id)s;'
        results = connectToMySQL('users').query_db(query, data)
        return cls( results[0] )
    @classmethod
    def show_update_user_page(cls, data):
        query = 'SELECT * FROM users WHERE id = %(user_id)s;'
        results = connectToMySQL('users').query_db(query, data)
        return cls( results[0] )
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(user_id)s;'
        return connectToMySQL('users').query_db(query, data)
    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(user_id)s'
        return connectToMySQL('users').query_db(query, data)
