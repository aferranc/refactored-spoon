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
