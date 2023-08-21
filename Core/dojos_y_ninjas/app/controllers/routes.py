
"""CONTROLLERS"""
# Flask
from flask import Flask, render_template, redirect, request

# App config
from app import app


# Models
from app.models.dojos import Dojo
from app.models.ninjas import Ninja


@app.route("/")
def home():

    """Redirige a la página principal del Dojo."""

    return redirect("/dojos")

@app.route("/dojos/")
def dojos():
    """Método que devuelve todos los ojos"""

    all_dojos = Dojo.get_all()
    return render_template("/dojos.html", dojos = all_dojos)

@app.route("/dojos/<int:id>")
def show_dojo(id):
    """Método que devuelve un solo dojo"""

    data = {
        "id" : id
    }

    dojo = Dojo.get_one(data)


    return render_template("/show_dojo.html", dojo = dojo)

@app.route("/ninjas/")
def add_ninja():
    """Método que devuelve el formulario para crear un ninja"""
    all_dojos = Dojo.get_all()

    return render_template("/ninjas.html", dojos = all_dojos)

@app.route("/ninjas/add/", methods=["POST"])
def new_ninja():
    """Método que agrega un nuevo ninja a la base de datos."""

    new_ninja = request.form
    print(new_ninja)

    data = {
        "first_name" : new_ninja["first_name"],
        "last_name" : new_ninja["last_name"],
        "age": new_ninja["age"],
        "dojo_id": new_ninja["dojo"]
    }

    print(data)

    Ninja.new_ninja(data)


    return redirect("/")


@app.route("/dojo/create/", methods = ["POST"])
def new_dojo():
    """Método que crea un nuevo dojo."""

    form = request.form

    dojo_data = {
        "name" : form["name"]
    }
    print(f"---{dojo_data}---")

    Dojo.new_dojo(dojo_data)

    return redirect("/")
