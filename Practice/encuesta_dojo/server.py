"""SERVER"""
from app import app
app.secret_key = "supersecret"

from app.controllers.survey import *

if __name__ == "__main__":
    app.run(debug=True)
