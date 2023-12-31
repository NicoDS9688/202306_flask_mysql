"""SERVER"""
from dotenv import load_dotenv

from flask_app import app
from flask_app.controllers import core, users

load_dotenv()

if __name__=="__main__":
    app.run(debug=True)
