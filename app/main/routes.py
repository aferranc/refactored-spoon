from flask import flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import login_required

from app import db
from app.main import bp
from app.models import City, Country, Province, Region, Restaurant


# Define index route
@bp.route("/", methods=("GET", "POST"))
def index():
    cities = City.query.all()
    countries = Country.query.all()
    regions = Region.query.all()
    provinces = Province.query.all()

    if request.method == "POST":
        city_id = request.form.get("city_id")
        if city_id:
            restaurants = Restaurant.query.filter_by(city_id=city_id).all()
        else:
            restaurants = Restaurant.query.all()
    else:
        restaurants = Restaurant.query.all()

    return render_template(
        "index.html", restaurants=restaurants, cities=cities, countries=countries, regions=regions, provinces=provinces
    )


# Define edit route
@bp.route("/edit/<int:id>", methods=("GET", "POST"))
@login_required
def edit(id):
    restaurant = Restaurant.query.get_or_404(id)
    countries = Country.query.all()
    regions = Region.query.all()
    provinces = Province.query.all()
    cities = City.query.all()

    if request.method == "POST":
        restaurant.name = request.form["name"]
        restaurant.address = request.form["address"]
        restaurant.city_id = request.form["city_id"]
        restaurant.province_id = request.form["province_id"]
        restaurant.region_id = request.form["region_id"]
        restaurant.country_id = request.form["country_id"]
        db.session.commit()
        flash(_("Restaurant successfully updated!"), "success")
        return redirect(url_for("main.index"))
    return render_template(
        "edit.html", restaurant=restaurant, countries=countries, regions=regions, provinces=provinces, cities=cities
    )
