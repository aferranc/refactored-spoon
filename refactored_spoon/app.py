from flask import Flask, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
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
app.secret_key = "jXthea5ednWrlExO1WJfewOq6COYPE3N"  # nosec

# Minify app
Minify(app=app, html=True, js=True, cssless=True, static=True)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the SQLAlchemy extension
db.init_app(app)


# Define the Country model
class Country(db.Model):
    name: Mapped[str] = mapped_column(String(80), primary_key=True, nullable=False)


# Define the Region model
class Region(db.Model):
    name: Mapped[str] = mapped_column(String(80), primary_key=True, unique=True)
    country_name: Mapped[str] = mapped_column(ForeignKey("country.name"), nullable=False)


# Define the Province model
class Province(db.Model):
    name: Mapped[str] = mapped_column(String(80), primary_key=True, unique=True)
    region_name: Mapped[str] = mapped_column(ForeignKey("region.name"), nullable=False)


# Define the City model
class City(db.Model):
    name: Mapped[str] = mapped_column(String(80), primary_key=True, unique=True)
    province_name: Mapped[str] = mapped_column(ForeignKey("province.name"), nullable=False)


# Define the Restaurant model
class Restaurant(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    address: Mapped[str] = mapped_column(String(120), nullable=False)
    city_name: Mapped[str] = mapped_column(ForeignKey("city.name"), nullable=False)
    province_name: Mapped[str] = mapped_column(ForeignKey("province.name"), nullable=False)
    region_name: Mapped[str] = mapped_column(ForeignKey("region.name"), nullable=False)
    country_name: Mapped[str] = mapped_column(ForeignKey("country.name"), nullable=False)


# Create all database tables
with app.app_context():
    db.create_all()

# Initialize Flask-Migrate
migrate = Migrate(app, db)


# Define the index route
@app.route("/", methods=("GET", "POST"))
def index():
    cities = City.query.all()  # Query all cities

    if request.method == "POST":
        city_name = request.form.get("city_name")  # Get the selected city name from the form
        if city_name:
            restaurants = Restaurant.query.filter_by(
                city_name=city_name
            ).all()  # Query restaurants in the selected city
        else:
            restaurants = Restaurant.query.all()  # Query all restaurants if no city is selected
    else:
        restaurants = Restaurant.query.all()  # Query all restaurants for GET requests

    return render_template("index.html", restaurants=restaurants, cities=cities)


# Define the edit route
@app.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    restaurant = Restaurant.query.get_or_404(id)
    if request.method == "POST":
        restaurant.name = request.form["name"]
        restaurant.address = request.form["address"]
        restaurant.city_name = request.form["city_name"]
        restaurant.province_name = request.form["province_name"]
        restaurant.region_name = request.form["region_name"]
        restaurant.country_name = request.form["country_name"]
        db.session.commit()
        flash("Restaurant actualitzat correctament!")
        return redirect(url_for("index"))
    return render_template("edit.html", restaurant=restaurant)


# Run the app
if __name__ == "__main__":
    app.run()
