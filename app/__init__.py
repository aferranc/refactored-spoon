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
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = _l("Please log in to access this page.")
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    from app.routes import bp as routes_bp

    app.register_blueprint(routes_bp)

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

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
