import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Configuration class for the application.

    Attributes:
        SECRET_KEY (str): The secret key used for session management and other security-related purposes.
        SQLALCHEMY_DATABASE_URI (str): The database URI that specifies the database to be used.
        LANGUAGES (list): A list of supported languages for the application.
        BABEL_DEFAULT_LOCALE (str): The default locale for the Babel extension.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "jXthea5ednWrlExO1WJfewOq6COYPE3N"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "restaurants.db"
    )  # pylint: disable=line-too-long
    LANGUAGES = ["ca", "es"]
    BABEL_DEFAULT_LOCALE = "ca"
