"""USER CLASS"""
import os

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.regular_expressions import EMAIL_REGEX


class User:
    """Constructor de clase User"""
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __str__(self) -> str:
        return f"{self.email} ({self.id})"


    @classmethod
    def validate(cls, form):
        """Método que valida el formulario"""
        errors = []
        if not EMAIL_REGEX.match(form['email']):
            errors.append(
                "Invalid email"
            )

        if cls.get_by_email(form['email']):
            errors.append(
                "Email already exists"
            )

        if len(form['first_name']) < 2:
            errors.append(
                "First name must have at least 2 characters"
            )

        if len(form['last_name']) < 2:
            errors.append(
                "Last name must have at least 2 characters"
            )


        if len(form['password']) < 8:
            errors.append(
                "Password must have at least 8 characters"
            )

        for key, valor in form.items():
            if len(valor) == 0:
                errors.append(
                    f"{key} not present. Obligatory field"
                )

        return errors


    @classmethod
    def get_all(cls):
        """Método que busca todos los users"""
        instances_results = []
        query = "SELECT * FROM users"
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db(query)
        for result in results:
            instance = cls(result)
            instances_results.append(instance)

        return instances_results


    @classmethod
    def save(cls, data ):
        """Método que guarda nuevo user"""
        print("Data:", data)
        query = (
            "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) "
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        )


        return connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )


    @classmethod
    def get(cls, id ):
        """Método para buscar un solo user por id"""
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        if results:
            return cls(results[0])

        return None


    @classmethod
    def get_by_email(cls, email):
        """Método para buscar user por email"""
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = { 'email': email }
        results = connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        if results:
            return cls(results[0])

        return None


    @classmethod
    def delete(cls, id ):
        """Método que elimina thought por id"""
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    def remove(self):
        """Método que elimina thought de instancia por id"""
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True

    def update(self):
        """Método para actulizar datos del user"""
        query = ("UPDATE users SET nombre = %(nombre)s, apellido = %(apellido)s, "
                "email = %(email)s, password = %(password)s, updated_at = NOW() WHERE id = %(id)s")

        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
        }
        connectToMySQL(os.getenv('DATA_BASE')).query_db( query, data )
        return True
