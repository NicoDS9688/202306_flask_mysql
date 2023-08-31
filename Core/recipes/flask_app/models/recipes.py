"""RECIPE CLASS"""
import os

from flask import session

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User


class Recipe:
    """Constructor de clase Recipe"""
    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.user_id = data['user_id']
        self.made_at = data['made_at']
        self.description = data['description']
        self.instructions = data['instructions']
        self.more_than_30 = data['more_than_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    def __str__(self) -> str:
        return f"{self.title}"

    @classmethod
    def validate(cls, form):
        """Método que valida el formulario"""
        errors = []

        if len(form['title']) < 3:
            errors.append(
                "Title must have at least 3 characters"
            )

        if len(form['description']) < 3:
            errors.append(
                "Description must have at least 3 characters"
            )

        if len(form['instructions']) < 3:
            errors.append(
                "Instructions must have at least 3 characters"
            )

        for key, valor in form.items():
            if len(valor) == 0:
                errors.append(
                    f"{key} not present. Obligatory field"
                )

        return errors

    @classmethod
    def validate_edit(cls, form):
        """Método que valida el formulario para la edición"""
        errors = []

        if 'title' in form and len(form['title']) < 3:
            errors.append(
                "Title must have at least 3 characters"
            )

        if 'description' in form and len(form['description']) < 3:
            errors.append(
                "Description must have at least 3 characters"
            )

        if 'instructions' in form and len(form['instructions']) < 3:
            errors.append(
                "Instructions must have at least 3 characters"
            )


        return errors

    @classmethod
    def get_all(cls):
        """Método que busca todos los recipes""" 
        instances_results = []
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query)
        for result in results:
            print(result)
            instance = cls(result)

            data = {
                'id': result['users.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'email': result['email'],
                'password': result['password'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
            }

            instance.user = User(data)
            instances_results.append(instance)

        return instances_results


    @classmethod
    def save(cls, data):
        """Método que guarda los recipes en base de datos"""
        query = (
            "INSERT INTO recipes (title, instructions, made_at, more_than_30, description, user_id, created_at, updated_at) "
            "VALUES (%(title)s, %(instructions)s, %(made_at)s, %(more_than_30)s, %(description)s, %(user_id)s, NOW(), NOW());"
        )

        user_with_data = {
            **data,
            'user_id': session['user']['id'],
        }

        return connectToMySQL(os.getenv('DATA_BASE')).query_db(query, user_with_data)

    @classmethod
    def get(cls, recipe_id):
        """Método que busca recipes por id"""
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        data = {
            "id": recipe_id
        }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query, data)

        if results:
            recipe_data = results[0]
            recipe = cls(recipe_data)
            return recipe

        return None

    @classmethod
    def get_by_user(cls, user_id ):
        """Método que busca recipes por user"""
        instances_results = []
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        data = { 'user_id': user_id }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query, data)
        for result in results:
            instance = cls(result)
            instances_results.append(instance)

        return instances_results


    @classmethod
    def delete(cls, id ):
        """Método que elimina recipes por id"""
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    def remove(self):
        """Método que elimina recipes de instancia por id"""
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    def edit_recipe(self, form):
        """Método para editar datos del recipes"""
        errors = Recipe.validate(form)

        if errors:
            return False, errors

        query = ("UPDATE recipes SET title = %(title)s, instructions = %(instructions)s, more_than_30 = %(more_than_30)s, "
                "made_at = %(made_at)s, description = %(description)s," 
                "updated_at = NOW() WHERE id = %(id)s")

        data = {
            'id': self.id,
            'title': form['title'],
            'description': form['description'],
            'instructions': form['instructions'],
            'more_than_30': form['more_than_30'],
            'made_at': form['made_at'],
        }
        connectToMySQL(os.getenv('DATA_BASE')).query_db(query, data)
        return True, None



