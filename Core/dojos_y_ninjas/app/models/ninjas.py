"""NINJAS"""
from app.config.mysqlconnection import connectToMySQL

class Ninja:
    """Clase que crea al ninja"""

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    def __str__(self) -> str:
        f"""Ninja attributes id = {self.id}, first_name = 
        {self.first_name}, last_name = {self.last_name}, age = {self.age},
        created_at = {self.created_at}, updated_at = {self.updated_at},
        dojo = {self.dojo_id}"""

    @classmethod
    def new_ninja(cls,data):
        """Método de clase que inserta los ninjas en dojos"""
        query = """INSERT INTO ninjas(first_name,last_name,age,dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"""

        connectToMySQL("esquema_dojos_y_ninjas").query_db(query, data)


    @classmethod
    def ninja_by_dojo(cls, data):
        """Método de clase que obtiene una lista de todos los ninjas de un dojo específico"""

        ninjas = []

        query = """SELECT * FROM ninjas WHERE dojo_id = %(id)s"""

        result = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,data)

        for ninja in result:
            ninjas.append(cls(ninja))

        return ninjas
