"""Server."""

# App config
from app import app

# Controllers
from app.controllers.routes import *


# Inciamos servidor
if __name__ == "__main__":
    app.run(debug=True)
