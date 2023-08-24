"""SURVEY"""
from flask import flash

class Survey:
    """Constructor de clase Survey"""

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def validate_data(data):
        """Valida datos del formulario"""
        valid = True

        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters.")
            valid = False
        if data["location"] == "--Select A Location--":
            flash("You must choose a location")
            valid = False
        if data["language"] == "--Select A Language--":
            flash("You must choose a language")
            valid = False
        if len(data["comment"]) < 1:
            flash("Comment section is empty")
            valid = False

        return valid
