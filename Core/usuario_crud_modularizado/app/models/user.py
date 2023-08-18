"""USER"""
from datetime import datetime
# MySQL connection
from app.config.mysqlconnection import connectToMySQL


class User:
    """Modelo de la clase `User`."""

    def __init__(self, data: dict):
        """Constructor de la clase `User.`"""

        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        """Método que selecciona todos usuarios"""
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users: list = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls,data):
        """Método de clase que agrega un nuevo usuario a la base de datos."""
        query = "INSERT INTO users(name, email, created_at) \
            VALUES(%(name)s, %(email)s, %(created_at)s);"

        data['created_at'] = datetime.now()

        return connectToMySQL("user_schema").query_db(query, data)

    @classmethod
    def get_one(cls,data):
        """Método de clase que busca un usuario"""

        query = "SELECT * FROM users WHERE id = %(id)s;"
        print(query)
        result = connectToMySQL("user_schema").query_db(query,data)

        return cls(result[0])

    @classmethod
    def edit_user(cls,data):
        """Método de clase que realiza la edición de un usuario en la base de datos."""
        query = """UPDATE users SET name = %(name)s,
        email = %(email)s,
        updated_at = Now() WHERE id = %(id)s;"""

        return connectToMySQL("user_schema").query_db(query, data)

    @classmethod
    def delete_user(cls,data):
        """Método de clase que elimina un usuario de la base de datos."""
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL("user_schema").query_db(query,data)
