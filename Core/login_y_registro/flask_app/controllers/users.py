"""USERS ROUTES"""
from flask import flash, redirect, render_template, request, session
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.users import User

bcrypt = Bcrypt(app)

@app.route('/login')
def register():
    """Método que realiza el login"""
    if 'user' in session:
        flash("You are already logged in. You are " + session['user']['email'], "info")
        return redirect("/")

    return render_template("login.html")

@app.route('/process_login', methods=["POST"])
def process_login():
    """Método que procesa el login"""
    print(request.form)

    user  = User.get_by_email(request.form['email'])
    if not user:
        flash("Email or password not valid", "error")
        return redirect("/login")

    result = bcrypt.check_password_hash(user.password, request.form['password'])

    if result:
        session['user'] = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        return redirect("/")

    flash("Email or password not valid", "error")
    return redirect("/login")

@app.route('/process_register', methods=["POST"])
def process_register():
    """Método que procesa el register"""
    print(request.form)

    errors = User.validate(request.form)
    if len(errors) > 0:
        for error in errors:
            flash(error, "error")
        return redirect("/login")

    if request.form["password"] != request.form["confirm_password"]:
        flash("Passwords don't match", "error")
        return redirect("/login")

    data = {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': bcrypt.generate_password_hash(request.form["password"])
    }

    id = User.save(data)

    flash("You have successfully registered", "success")
    return redirect("/login")



@app.route('/exit')
def exit():
    """Método que remueve el session"""
    session.clear()
    return redirect("/login")
