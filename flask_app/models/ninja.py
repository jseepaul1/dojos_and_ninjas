
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, ninja_data):
        self.id = ninja_data['id']
        self.first_name = ninja_data['first_name']
        self.last_name = ninja_data['last_name']
        self.age = ninja_data['age']
        self.created_at = ninja_data['created_at']
        self.updated_at = ninja_data['updated_at']

    @classmethod
    def save (cls, data):
        query = "INSERT INTO  ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)