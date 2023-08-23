"""SERVER"""

# App config
from app import app

# Controllers
from app.controllers.author_routes import *
from app.controllers.book_routes import *


# Inciamos servidor
if __name__ == "__main__":
    app.run(debug=True)
    