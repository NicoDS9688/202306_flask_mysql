"""SHOW ROUTES"""
from datetime import datetime

from flask import flash, redirect, render_template, request, session, url_for

from flask_app import app
from flask_app.models.recipes import Recipe
from flask_app.models.users import User


@app.route('/new_recipe/', methods=['GET', 'POST'])
def new_recipe():
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")
    return render_template('new_recipe.html')


@app.route('/process_new_recipe', methods=["POST"])
def process_new_recipe():
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")

    user_id = session['user']['id']


    errors = Recipe.validate(request.form)
    if len(errors) > 0:
        for error in errors:
            flash(error, "error")
        return redirect("/new_recipe")


    form_data_with_user_id = {**request.form, 'user_id': user_id}

    Recipe.save(form_data_with_user_id)
    flash("Recipe added", "success")
    return redirect("/")


@app.route('/recipe_delete/<int:recipe_id>')
def recipe_delete(show_id):
    recipe = Recipe.get(show_id)

    if recipe is None:
        flash("Recipe not found.", "error")
        return redirect('/')

    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")

    if recipe.user_id != session['user']['id']:
        flash("You don't have permission to delete this recipe.", "error")
        return redirect('/')

    if Recipe.delete(show_id):
        flash("Recipe deleted!", "success")
    else:
        flash("Failed to delete Recipe.", "error")

    return redirect('/')

@app.route('/recipe/<int:recipe_id>')
def recipe_info(recipe_id):
    """Ruta de info del recipe"""
    recipe = Recipe.get(recipe_id)
    if recipe:
        user = session.get('user')
        return render_template('recipe_info.html', recipe=recipe, user=user)
    else:
        flash("Recipe not found", "error")
        return redirect('/')

@app.route('/edit_recipe/<int:recipe_id>', methods=["GET"])
def edit_recipe(recipe_id):
    """Renderiza la página de edición de recipe"""
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")

    recipe = Recipe.get(recipe_id)
    if recipe is None:
        flash("Recipe not found.", "error")
        return redirect('/')

    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/process_edit_recipe/<int:recipe_id>', methods=["POST"])
def process_edit_recipe(recipe_id):
    """Procesa el formulario de edición de recipe"""
    if 'user' not in session:
        flash("You are not logged in", "error")
        return redirect("/login")

    recipe = Recipe.get(recipe_id)
    if recipe is None:
        flash("Recipe not found.", "error")
        return redirect('/')

    form = request.form
    success, errors = recipe.edit_recipe(form)

    if success:
        flash("Recipe updated!", "success")
    else:
        for error in errors:
            flash(error, "error")

    return redirect(url_for('recipe_info', recipe_id=recipe_id))