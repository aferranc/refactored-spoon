"""
This module sets up the error handling blueprint for the Flask application.

It imports the necessary components and initializes the blueprint for the error handlers.

Modules:
    Blueprint: Flask class for creating blueprints.
    handlers: Contains the error handling routes for the blueprint.
"""

from flask import Blueprint

bp = Blueprint("errors", __name__)

from app.errors import handlers
