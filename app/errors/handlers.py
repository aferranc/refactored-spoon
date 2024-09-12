"""
This module defines the error handlers for the Flask application.

It includes handlers for 404 (Not Found) and 500 (Internal Server Error) errors,
rendering the appropriate error templates.

Modules:
    render_template: Function to render HTML templates.
    db: SQLAlchemy database instance.
    bp: Blueprint for the error handlers.
"""

from flask import render_template

from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Handler for 404 Not Found error.

    Renders the 404 error template when a 404 error occurs.

    Args:
        error: The error object.

    Returns:
        tuple: The rendered template and the status code.
    """
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Handler for 500 Internal Server Error.

    Rolls back the database session and renders the 500 error template when a 500 error occurs.

    Args:
        error: The error object.

    Returns:
        tuple: The rendered template and the status code.
    """
    db.session.rollback()
    return render_template("errors/500.html"), 500
