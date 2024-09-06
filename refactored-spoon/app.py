from flask import Flask, redirect, render_template, request, url_for
from flask_minify import Minify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Define a base class for declarative class definitions
class Base(DeclarativeBase):
    pass


# Initialize SQLAlchemy with a custom base class
db = SQLAlchemy(model_class=Base)

# Create the Flask application instance
app = Flask(__name__)

# Minify app
Minify(app=app, html=True, js=True, cssless=True, static=True)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the SQLAlchemy extension
db.init_app(app)


# Define the Country model
class Country(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)


# Define the Region model
class Region(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)


# Define the Province model
class Province(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"), nullable=False)


# Define the City model
class City(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    province_id: Mapped[int] = mapped_column(ForeignKey("province.id"), nullable=False)


# Define the Restaurant model
class Restaurant(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    address: Mapped[str] = mapped_column(String(120), nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"), nullable=False)


# Create all database tables
with app.app_context():
    db.create_all()


# Define the index route
@app.route("/", methods=("GET", "POST"))
def index():
    cities = City.query.all()  # Query all cities

    if request.method == "POST":
        city_id = request.form["city_id"]  # Get the selected city ID from the form
        if city_id:
            restaurants = Restaurant.query.filter_by(city_id=city_id).all()  # Query restaurants in the selected city
        else:
            restaurants = Restaurant.query.all()  # Query all restaurants if no city is selected
    else:
        restaurants = Restaurant.query.all()  # Query all restaurants for GET requests

    return render_template("index.html", restaurants=restaurants, cities=cities)  # Render the template with data


# Run the app
if __name__ == "__main__":
    app.run(debug=False)
