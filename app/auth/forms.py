"""
This module defines the form classes for the Flask application using Flask-WTF.

It includes the LoginForm class, which is used for user authentication.

Modules:
    FlaskForm: Base class for creating forms in Flask.
    PasswordField: Field for entering passwords.
    StringField: Field for entering strings.
    SubmitField: Field for creating a submit button.
    DataRequired: Validator to ensure data is provided.
"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):  # pylint: disable=too-few-public-methods
    """
    Form for user login.

    Attributes:
        username (StringField): Field for entering the username.
        password (PasswordField): Field for entering the password.
        submit (SubmitField): Field for submitting the form.
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")
