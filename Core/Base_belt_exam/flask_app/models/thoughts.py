"""THOUGHT CLASS"""
import os

from flask import session

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User


class Thought:
    """Constructor de clase Thought"""
    def __init__(self, data) -> None:
        self.id = data['id']
        self.thought = data['thought']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.likes = 0
        self.has_like = False

    def __str__(self) -> str:
        return f"{self.thought}"

    @classmethod
    def validate(cls, form):
        """Método que valida el formulario para thought"""
        errors = []

        if len(form['thought']) == 0:
            errors.append(
                "Thought is mandatory"
            )

        if len(form['thought']) < 5:
            errors.append(
                "Thought must have at least 5 characters"
            )

        return errors

    @classmethod
    def get_all(cls):
        """Método que busca todos los thoughts""" 
        instances_results = []
        query = "SELECT * FROM thoughts join users ON thoughts.user_id = users.id"
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query)
        for result in results:
            print(result)
            instance = cls(result)

            data = {
                'id': result['id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'email': result['email'],
                'password': result['password'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
            }

            instance.user = User(data)
            instance.likes = instance.get_likes()
            instance.has_like = instance.verify_like(instance.id, session['user']['id'])

            instances_results.append(instance)

        return instances_results


    @classmethod
    def save(cls, data):
        """Método que guarda los thoughts en base de datos"""
        query = "INSERT INTO thoughts (thought, user_id, created_at, updated_at) " \
                "VALUES (%(thought)s, %(user_id)s, NOW(), NOW());"

        user_with_data = {
            **data,
            'user_id': session['user']['id'],
        }

        return connectToMySQL(os.getenv('DATA_BASE')).query_db( query, user_with_data )

    @classmethod
    def get(cls, id):
        """Método que busca un solo thought por id"""
        query = "SELECT * FROM thoughts WHERE id = %(id)s;"
        data = { 'id': id }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        if results:
            return cls(results[0])

        return None

    @classmethod
    def get_by_user(cls, user_id ):
        """Método que busca thougths por user"""
        instances_results = []
        query = "SELECT * FROM thoughts WHERE user_id = %(user_id)s;"
        data = { 'user_id': user_id }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query, data)
        for result in results:
            instance = cls(result)
            instances_results.append(instance)

        return instances_results


    @classmethod
    def delete(cls, id ):
        """Método que elimina thought por id"""
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    def remove(self):
        """Método que elimina thought de instancia por id"""
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    @classmethod
    def add_like(cls, thought_id, user_id):
        """Método para agregar like"""
        query = "INSERT INTO likes (user_id,thought_id) VALUES (%(user_id)s,%(thought_id)s);"
        data = {
            'thought_id': thought_id,
            'user_id': user_id,
        }
        return connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )

    def get_likes(self):
        """Método que cuenta los likes"""
        query = "SELECT COUNT(*) as count FROM likes WHERE thought_id = %(id)s;"
        data = { 'id': self.id }
        result = connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        if result:
            print("Likes = ", result)
            return result[0]['count']

        return True

    @classmethod
    def verify_like(cls, thought_id, user_id):
        """Método que verifica si hay like"""
        query = "SELECT COUNT(*) as count FROM likes WHERE thought_id = %(thought_id)s " \
        "and user_id = %(user_id)s"
        data = {
            'thought_id': thought_id,
            'user_id': user_id,
        }
        result = connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        if result:
            return result[0]['count'] >= 1
        return False

    @classmethod
    def remove_like(cls, thought_id):
        """Método que remueve el like"""
        query = "DELETE FROM likes WHERE thought_id = %(thought_id)s  and user_id = %(user_id)s"
        data = {
            'thought_id': thought_id,
            'user_id': session['user']['id'],
        }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True
