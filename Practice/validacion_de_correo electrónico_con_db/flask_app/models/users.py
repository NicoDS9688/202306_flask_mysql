"""USER CLASS"""
import os

from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.regular_expressions import EMAIL_REGEX


class User:
    """Constructor de clase User"""
    def __init__(self, data) -> None:
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __str__(self) -> str:
        return f"{self.email} ({self.id})"


    @classmethod
    def add_email(cls, data: dict):
        """Método para agregar email a db"""
        query = """INSERT INTO users(email)
        VALUES(%(email)s)"""

        connectToMySQL(os.getenv('DATA_BASE')).query_db(query,data)
        flash(f"Email: {data['email']} added successfully")


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
    def delete(cls, data):
        """Método que elimina email de db"""

        query = "DELETE FROM users WHERE id = %(id)s"

        connectToMySQL(os.getenv('DATA_BASE')).query_db(query,data)


    @staticmethod
    def validate(form):
        """Valida email"""
        validation = True

        if not EMAIL_REGEX.match(form["email"]):
            validation = False
            flash("Invalid email","warning")

        instances_results = User.get_all()
        print(f"---{instances_results}---")

        for email in instances_results:
            if email.email == form["email"]:
                validation = False
                flash("Email already exist","warning")

        return validation
