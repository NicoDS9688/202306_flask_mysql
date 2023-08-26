"""USER CLASS"""
import os
import re
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


        password = form['password']
        if len(password) < 8:
            errors.append("Password must have at least 8 characters")
        if not re.search(r'[a-z]', password):
            errors.append("Password must contain at least one lowercase letter")
        if not re.search(r'[A-Z]', password):
            errors.append("Password must contain at least one uppercase letter")

        return errors


    @classmethod
    def save(cls, data ):
        """Método que guarda nuevo user"""
        print("LLEGA", data)
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
