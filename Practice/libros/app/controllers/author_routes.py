"""CONTROLLERS"""
# Flask
from flask import render_template, redirect, request, url_for

# App config
from app import app


# Models
from app.models.authors import Author
from app.models.books import Book


@app.route("/")
def home():

    """Redirige a la página principal."""

    return redirect(url_for("authors"))


@app.route("/authors/")
def authors():
    """Ruta que devuelve todos los autores"""

    all_authors = Author.get_all()
    return render_template("/authors.html", authors = all_authors)


@app.route("/authors/add", methods=["POST"])
def add_author():
    """Ruta para agregar un nuevo autor"""

    data = request.form

    author_info = {
        "name" : data["name"],
    }

    Author.add_author(author_info)
    return redirect(url_for("authors"))


@app.route("/authors/<int:id>")
def show_author(id):
    """Método que devuelve un solo autor"""

    data = {
        "id" : id
    }

    author = Author.get_one(data)


    return render_template("show_author.html", author = author)

