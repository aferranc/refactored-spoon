"""
This module sets up the authentication blueprint for the Flask application.

It imports the necessary components and initializes the blueprint for the authentication routes.

Modules:
    Blueprint: Flask class for creating blueprints.
    routes: Contains the routes for the authentication blueprint.
"""

from flask import Blueprint

bp = Blueprint("auth", __name__)

from app.auth import routes
