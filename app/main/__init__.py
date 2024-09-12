"""
This module sets up the main blueprint for the Flask application.

It imports the necessary components and initializes the blueprint for the main routes.

Modules:
    Blueprint: Flask class for creating blueprints.
    routes: Contains the main routes for the blueprint.
"""

from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import routes
