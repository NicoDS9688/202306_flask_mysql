"""DOJOS"""
from app.config.mysqlconnection import connectToMySQL
from app.models.ninjas import Ninja

class Dojo:
    """Modelo de la clase `Dojo`."""

    def __init__(self, data: dict):
        """Constructor de la clase `User.`"""

        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        """Método que selecciona todos los dojo"""
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos: list = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        """Método de clase que busca un único dojo junto con todos sus ninjas de la base de datos"""

        query = """SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id =
        ninjas.dojo_id WHERE dojos.id = %(id)s"""

        result = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,data)
        dojo = cls(result[0])

        all_ninjas = []
        for row_db in result:
            print("--ROW",row_db)

            ninja_data = {
                "id" : row_db["ninjas.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "age" : row_db["age"],
                "created_at" : row_db["ninjas.created_at"],
                "updated_at" : row_db["ninjas.updated_at"],
                "dojo_id" : row_db["id"]
            }

            ninja_instance = Ninja(ninja_data)
            all_ninjas.append(ninja_instance)

        dojo.ninjas = all_ninjas
        print(dojo)

        return dojo


    @classmethod
    def new_dojo(cls,data):
        """Agrega un nuevo dojo a la base de datos."""

        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        connectToMySQL("esquema_dojos_y_ninjas").query_db(query, data)
