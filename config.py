import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "jXthea5ednWrlExO1WJfewOq6COYPE3N"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "restaurants.db")
    LANGUAGES = ["ca", "es"]
    BABEL_DEFAULT_LOCALE = "ca"
