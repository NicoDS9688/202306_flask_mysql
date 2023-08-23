"""BOOKS"""
from app.config.mysqlconnection import connectToMySQL

#Models
from app.models import authors


class Book:
    """Clase Libro"""

    def __init__(self, data: dict):
        self.id = data["id"]
        self.title= data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors_who_favourited: list = []


    @classmethod
    def add_book(cls,data:dict):
        """Método de clase que crea un nuevo libro en la base de datos."""

        query = """INSERT INTO books(title,num_of_pages)
        VALUES(%(title)s, %(num_of_pages)s)"""

        connectToMySQL("esquema_libros").query_db(query,data)


    @classmethod
    def add_author_to_favourite(cls,data: dict):
        """Método de clase que agrega un favorito a autores"""

        query = """INSERT INTO favourites(author_id, book_id)
        VALUES ( %(author_id)s, %(book_id)s )"""

        return connectToMySQL("esquema_libros").query_db(query,data)


    @classmethod
    def get_all(cls):
        """Método de clase que obtiene todos los libros de la base de datos"""

        query = "SELECT * FROM books"

        result = connectToMySQL("esquema_libros").query_db(query)

        return result

    @classmethod
    def get_one(cls, data):
        """Método de clase que busca un solo libro"""

        query = """SELECT * FROM books
        LEFT JOIN favourites ON books.id = favourites.book_id
        LEFT JOIN authors ON authors.id = favourites.author_id
        WHERE books.id = %(id)s;"""

        response = connectToMySQL("esquema_libros").query_db(query, data)

        book = cls(response[0])


        for row in response:
            if row["authors.id"] == None:
                break
            data={
                    "id":row["author_id"],
                    "name":row["name"],
                    "created_at":row["authors.created_at"],
                    "updated_at":row["authors.updated_at"]
                }
            book.authors_who_favourited.append(authors.Author(data))

        print(book)
        return book
