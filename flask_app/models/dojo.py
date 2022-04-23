from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name ) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        dojo_results = connectToMySQL('dojos_and_ninjas_schema').query_db(
            query
        )
        dojos = []
        for dojo in dojo_results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        dojo_results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(dojo_results[0])
        for row in dojo_results:
            if row['ninjas.id']:
                dojo_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                dojo.ninjas.append(Ninja(dojo_data))
        return dojo
