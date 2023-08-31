"""CORE"""
from flask import render_template, flash, redirect, session
from flask_app import app
from flask_app.models.recipes import Recipe
from flask_app.models.users import User



@app.route('/')
def home():
    """Ruta home, si no en sesión, redirecciona al login"""
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")

    return render_template('recipes.html', recipes=Recipe.get_all(), user=session.get('user'))
