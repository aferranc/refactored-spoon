from urllib.parse import urlsplit

import sqlalchemy as sa
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import app, db
from app.forms import LoginForm
from app.models import City, Country, Province, Region, Restaurant, User


# Define index route
@app.route("/", methods=("GET", "POST"))
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
@app.route("/edit/<int:id>", methods=("GET", "POST"))
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
        flash("Restaurant successfully updated!", "success")
        return redirect(url_for("index"))
    return render_template(
        "edit.html", restaurant=restaurant, countries=countries, regions=regions, provinces=provinces, cities=cities
    )


# Define login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


# Define logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
