"""SURVEY"""
from flask import render_template, redirect, session, request

from app import app
from app.models.survey import Survey

@app.route("/")
def home():
    """Ruta home"""
    return render_template("form.html")


@app.route("/form/", methods = ["POST"])
def form():
    """Valida form"""

    print(request.form)
    if not Survey.validate_data(request.form):
        return redirect("/")

    keys = ["name","location","language","comment"]

    for key in keys:
        session[key] = request.form[key]

    print(session["name"],session["location"],session["language"],session["comment"] )


    return redirect("/result/")


@app.route("/result/")
def result():
    """Devuelve resultado"""

    return render_template("result.html")


@app.route("/reset/")
def reset_user():
    """Salir de session"""

    keys = ["name","location","language","comment"]

    for key in keys:
        del session[key]

    return redirect("/")
