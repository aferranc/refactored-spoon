import sqlalchemy as sa
import sqlalchemy.orm as so

from app import app, cli, db
from app.models import City, Country, Province, Region, Restaurant, User


@app.shell_context_processor
def make_shell_context():
    return {
        "sa": sa,
        "so": so,
        "db": db,
        "User": User,
        "Country": Country,
        "Region": Region,
        "Province": Province,
        "City": City,
        "Restaurant": Restaurant,
    }
