"""USERS ROUTES"""
from flask import redirect, render_template, request, url_for, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.users import User

bcrypt = Bcrypt(app)

@app.route("/add/", methods=["POST"])
def add_email():
    """Agrega email a db"""
    data = {
        "email": request.form["email"]
    }

    response = User.validate(data)

    if not response:
        return redirect("/")

    flash("Email verified successfully", "success")
    print(data)
    User.add_email(data)


    return redirect(url_for("success"))


@app.route("/success/")
def success():
    """Muestra emails en db"""
    emails = User.get_all()

    for email in emails:
        print(email)


    return render_template("success.html", users = emails)

@app.route("/delete/<int:id>")
def delete_user(id):
    """Elimina email de db"""

    data = {
        "id": id
    }

    flash("Email deleted successfully", "success")
    User.delete(data)

    return redirect(url_for("success"))
