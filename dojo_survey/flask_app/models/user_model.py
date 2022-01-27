from flask import flash

import re

from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojo_survey'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);'
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = " SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def user_validation(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name has to be longer than 3 characters')
            is_valid = False
        if len(data['comment']) < 10:
            flash('Comments has to be longer than 10 characters')
            is_valid = False
        return is_valid