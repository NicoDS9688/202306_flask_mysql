"""CORE"""
from flask import render_template, flash, redirect, session
from flask_app import app
from flask_app.models.thoughts import Thought



@app.route('/')
def home():
    """Ruta home, si no en sesión, redirecciona al login"""
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")


    return render_template(
        'home.html',
        thoughts=Thought.get_all()
    )
