"""AUTHORS"""
from app.config.mysqlconnection import connectToMySQL

# Models
from app.models.books import Book


class Author:
    """Modelo de la clase Author."""

    def __init__(self, data: dict):
        """Constructor de la clase Author"""

        self.id = data['id']
        self.name = data['name']
        self.favourite_books: list = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favourite_books: list = []

    def __str__(self) -> str:
        return f"""Atributos de la clase Author : (id = {self.id},
        name = {self.name}, libros favoritos = {self.favourite_books},
        created_at = {self.created_at},updated_at = {self.updated_at})"""

    @classmethod
    def get_all(cls):
        """Método que selecciona todos los autores"""
        query = "SELECT * FROM authors"
        result = connectToMySQL("esquema_libros").query_db(query)

        return result

    @classmethod
    def get_one(cls, data):
        """Método de clase que busca un solo autor con sus favoritos"""

        query = """SELECT * FROM authors
        LEFT JOIN favourites ON authors.id = favourites.author_id
        LEFT JOIN books ON books.id = favourites.book_id
        WHERE authors.id = %(id)s;"""

        response = connectToMySQL("esquema_libros").query_db(query, data)
        print(response)

        author = cls(response[0])

        for row in response:
            if row["book_id"] is not None:

                book_data = {
                    "id": row["books.id"],
                    "title": row["title"],
                    "num_of_pages": row["num_of_pages"],
                    "created_at": row["books.created_at"],
                    "updated_at": row["books.updated_at"]
                }
                author.favourite_books.append(Book(book_data))

        print(author)
        return author

    @classmethod
    def add_author(cls, data):
        """Agrega un nuevo autor a la base de datos."""

        query = "INSERT INTO authors(name) VALUES (%(name)s);"
        connectToMySQL("esquema_libros").query_db(query, data)

    @classmethod
    def add_book_to_favorite(cls, data: dict):

        query = """INSERT INTO favourites(author_id, book_id)
        VALUES ( %(author_id)s, %(book_id)s )"""

        return connectToMySQL("esquema_libros").query_db(query, data)

    @classmethod
    def unfavourited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favourites \
              WHERE book_id = %(id)s);"
        authors = []
        response = connectToMySQL('esquema_libros').query_db(query, data)
        for row in response:
            authors.append(cls(row))
        return authors
