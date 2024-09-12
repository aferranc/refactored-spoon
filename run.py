"""
This module initializes the Flask application and sets up the shell context.

It imports the necessary components from the app package, creates the Flask application
instance, and defines the shell context processor to make the database instance and models
available in the Flask shell.

Modules:
    create_app: Function to create the Flask application instance.
    db: SQLAlchemy database instance.
    models: Contains the database models for the application.
"""

from app import create_app, db
from app.models import City, Country, Province, Region, Restaurant, User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """
    Shell context processor for the Flask application.

    This function adds the database instance and models to the shell context,
    making them available in the Flask shell without needing to import them manually.

    Returns:
        dict: A dictionary containing the database instance and models.
    """
    return {
        "db": db,
        "User": User,
        "Country": Country,
        "Region": Region,
        "Province": Province,
        "City": City,
        "Restaurant": Restaurant,
    }


if __name__ == "__main__":
    app.run()
