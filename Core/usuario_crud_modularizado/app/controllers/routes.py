"""CONTROLLERS"""
# Flask
from flask import Flask, render_template, redirect, request

# App config
from app import app


# Models
from app.models.user import User


@app.route("/users/")
def users():
    """Método que devuelve el template index"""

    users = User.get_all()
    return render_template("users.html", users=users)


@app.route("/users/add/")
def create_user():
    """Método que crea un nuevo usuario"""
    return render_template("new_user.html")

@app.route("/users/form/", methods=["POST"])
def add_user():
    """Método que maneja la ruta "/user/form/" y se utiliza para agregar un nuevo usuario."""

    form = request.form

    data_filled = {
        "name": form["name"],
        "email": form["email"],
    }

    print(f"--Dictionary-- {data_filled}")

    User.add_user(data_filled)

    return redirect("/users/")

@app.route("/")
def home():
    """Método que redirige a nuestra direccion users"""

    return redirect("/users")

@app.route("/users/<int:id>")
def show_user(id):
    """Método que muestra a un usuario"""

    data = {
        "id" : id
    }

    user = User.get_one(data)

    print(f"---{id}---")
    print(user)

    return render_template("show_user.html", user = user)

@app.route("/users/edit/<int:id>")
def edit_user(id):
    """Método que renderiza el formulario para editar un usuario"""
    data = {
        "id": id
    }

    user = User.get_one(data)
    print(f"---{id}---")

    return render_template("edit_user.html", user = user)

@app.route("/users/edit/<int:id>", methods=["POST"])
def update_user(id):
    """Método que maneja la ruta "/user/form/" y se utiliza para agregar un nuevo usuario."""

    edited_values = request.form

    data_for_edit = {
        "id" : edited_values["id"],
        "name" : edited_values["name"],
        "email" :edited_values["email"],
    }
    print(edited_values)
    print(data_for_edit)

    User.edit_user(data_for_edit)

    return redirect("/users/")

@app.route("/users/delete/<int:id>/")
def delete_user(id):
    """Metodo que elimina al usuario de la base de datos"""

    data =  {
        "id" : id
    }

    print("User deleted, id:", data)

    User.delete_user(data)

    return redirect("/users/")
