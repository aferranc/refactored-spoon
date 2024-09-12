"""
This module sets up the Flask application, including configuration, database,
and logging. It also defines the shell context and initializes various Flask extensions.

Modules:
    logging: Provides logging functionality.
    os: Provides a way of using operating system dependent functionality.
    RotatingFileHandler: A handler for logging that rotates log files.
    Flask: The Flask application class.
    current_app: Proxy for the current application.
    request: Proxy for the current request.
    Babel: Flask extension for internationalization and localization.
    lazy_gettext: Function for lazy translation.
    LoginManager: Flask-Login extension for user session management.
    Migrate: Flask-Migrate extension for handling database migrations.
    SQLAlchemy: Flask-SQLAlchemy extension for database integration.
    Config: Configuration class for the application.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, current_app, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _l
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


def get_locale():
    """
    Determines the best match for supported languages based on the request.

    Returns:
        str: The best match for the supported languages.
    """
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = _l("Please log in to access this page.")
babel = Babel()


def create_app(config_class=Config):
    """
    Creates and configures the Flask application.

    Args:
        config_class (class): The configuration class to use.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    from app.main import bp as routes_bp

    app.register_blueprint(routes_bp)

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.cli import bp as cli_bp

    app.register_blueprint(cli_bp)

    if not app.debug and not app.testing:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler("logs/restaurant.log", maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Restaurant startup")

    return app
