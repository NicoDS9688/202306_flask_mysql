"""CORE"""
from flask import render_template
from flask_app import app




@app.route('/')
def home():
    """Ruta home"""
    return render_template("/login.html")
