"""
This module defines the authentication routes for the Flask application.

It includes routes for logging in and logging out users, and handles user authentication.

Modules:
    urlsplit: Function to split a URL into components.
    sqlalchemy: SQLAlchemy library for database operations.
    flash: Function to flash messages to the user.
    redirect: Function to redirect the user to a different endpoint.
    render_template: Function to render HTML templates.
    request: Proxy for the current request.
    url_for: Function to build a URL to a specific endpoint.
    _: Function for translation and localization.
    current_user: Proxy for the current logged-in user.
    login_user: Function to log in a user.
    logout_user: Function to log out a user.
    db: SQLAlchemy database instance.
    bp: Blueprint for the authentication routes.
    LoginForm: Form class for user login.
    User: User model class.
"""

from urllib.parse import urlsplit

import sqlalchemy as sa
from flask import flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import current_user, login_user, logout_user

from app import db
from app.auth import bp
from app.auth.forms import LoginForm
from app.models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Route for user login.

    If the user is already authenticated, they are redirected to the main index.
    If the login form is submitted and valid, the user is authenticated and logged in.
    If authentication fails, an error message is flashed.

    Returns:
        Response: The response object to render the login template or redirect the user.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"), "danger")
            return redirect(url_for("auth.login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title=_("Sign In"), form=form)


@bp.route("/logout")
def logout():
    """
    Route for user logout.

    Logs out the current user and redirects them to the main index.

    Returns:
        Response: The response object to redirect the user.
    """
    logout_user()
    return redirect(url_for("main.index"))
