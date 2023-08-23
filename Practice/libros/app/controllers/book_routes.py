"""CONTROLLERS"""
#Importaciones externas
from flask import render_template, redirect, request, url_for

#Importaciones locales
from app import app
from app.models.books import Book
from app.models.authors import Author




@app.route("/books/")
def books():
    """Muestra todos los libros"""
    book=Book.get_all()

    return render_template("books.html", books = book)



@app.route("/books/add/", methods=["POST"])
def add_book():
    """Para agregar un libro"""
    result = request.form

    book_data = {
        "title" : result["title"],
        "num_of_pages" : result["num_of_pages"]
    }

    Book.add_book(book_data)

    return redirect(url_for("books"))


@app.route("/books/<int:id>")
def show_book(id):
    """Muestra un solo libro"""
    print(f"---{id}---")

    data = {
        "id" : id
    }

    return render_template("show_book.html", book=Book.get_one(data),
                           unfavourited_authors=Author.unfavourited_authors(data))

@app.route("/book/add/favourite/<int:id>", methods=["POST"])
def add_favourite_author(id):    

    data = {
        "book_id": id,
        "author_id": request.form["author_id"]
    }

    Book.add_author_to_favourite(data)
    return redirect(url_for("show_book", id = data["book_id"]))
