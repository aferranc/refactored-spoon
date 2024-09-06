from flask import Flask, redirect, render_template, request, url_for
from flask_paginate import Pagination, get_page_parameter
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


@app.route("/", methods=("GET", "POST"))
def index():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    cities = City.query.all()

    if request.method == "POST":
        city_id = request.form["city_id"]
        if city_id:
            restaurants = Restaurant.query.filter_by(city_id=city_id).paginate(page, per_page, False)
        else:
            restaurants = Restaurant.query.paginate(page, per_page, False)
    else:
        restaurants = Restaurant.query.paginate(page, per_page, False)

    pagination = Pagination(page=page, total=restaurants.total, record_name="restaurants", per_page=per_page)
    return render_template("index.html", restaurants=restaurants.items, cities=cities, pagination=pagination)


@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        city_id = request.form["city_id"]

        new_restaurant = Restaurant(name=name, address=address, city_id=city_id)
        db.session.add(new_restaurant)
        db.session.commit()
        return redirect(url_for("index"))

    cities = City.query.all()
    return render_template("add.html", cities=cities)


if __name__ == "__main__":
    app.run(debug=True)
