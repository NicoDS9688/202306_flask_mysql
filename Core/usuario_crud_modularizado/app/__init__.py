"""INIT"""

# Flask
from flask import Flask

# App
app = Flask(__name__)

# Secret key
app.secret_key = "supersecret"
