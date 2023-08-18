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
