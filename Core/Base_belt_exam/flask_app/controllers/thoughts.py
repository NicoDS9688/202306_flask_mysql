"""THOUGHTS ROUTES"""
from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.thoughts import Thought
from flask_app.models.users import User


@app.route('/process_thought', methods=["POST"])
def process_thought():
    """Método que procesa el formulario para thought"""
    print(request.form)

    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")


    errors = Thought.validate(request.form)
    if len(errors) > 0:
        for error in errors:
            flash(error, "error")
        return redirect("/")

    Thought.save(request.form)
    flash("Thought added", "success")
    return redirect("/")

@app.route('/thought/<int:id>/delete')
def thought_delete(id):
    Thought.delete(id)
    flash("Thought deleted!", "success")
    return redirect("/")


@app.route('/user/<int:id>')
def user_thought(id):
    user = User.get(id)
    thoughts_user = Thought.get_by_user(id)
    return render_template("user.html", user=user, thoughts=thoughts_user)


@app.route('/add_like/<int:id>')
def thought_likes(id):
    if Thought.verify_like(id, session['user']['id']):
        flash("You already liked this", "error")
        return redirect("/")

    Thought.add_like(id, session['user']['id'])
    flash("Like added", "success")
    return redirect("/")

@app.route('/remove_like/<int:id>')
def remove_likes(id):
    if Thought.verify_like(id, session['user']['id']):
        Thought.remove_like(id)
        flash("Like deleted", "success")
        return redirect("/")

    return redirect("/")
