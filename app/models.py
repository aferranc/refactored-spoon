"""
This module defines the database models for the Flask application.

It includes models for User, Country, Region, Province, City, and Restaurant,
and sets up relationships between these models.

Modules:
    Optional: A typing hint for optional values.
    sqlalchemy: SQLAlchemy library for database operations.
    sqlalchemy.orm: SQLAlchemy ORM components.
    UserMixin: Flask-Login mixin for user session management.
    check_password_hash, generate_password_hash: Functions for password hashing.
    db: SQLAlchemy database instance.
    login: Flask-Login instance for user session management.
"""

from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(UserMixin, db.Model):
    """
    User model for storing user details.

    Attributes:
        id (int): The primary key for the user.
        username (str): The username of the user.
        password_hash (str, optional): The hashed password of the user.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        """
        Sets the user's password.

        Args:
            password (str): The password to set.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks the user's password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password_hash(self.password_hash, password)


class Country(db.Model):
    """
    Country model for storing country details.

    Attributes:
        id (int): The primary key for the country.
        name (str): The name of the country.
        regions (list): The regions in the country.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)

    regions: so.WriteOnlyMapped["Region"] = so.relationship("Region", back_populates="country")

    def __repr__(self):
        return "<Country {}>".format(self.name)


class Region(db.Model):
    """
    Region model for storing region details.

    Attributes:
        id (int): The primary key for the region.
        name (str): The name of the region.
        country_id (int): The ID of the country the region belongs to.
        country (Country): The country the region belongs to.
        provinces (list): The provinces in the region.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    country_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Country.id), index=True)

    country: so.Mapped[Country] = so.relationship("Country", back_populates="regions")
    provinces: so.WriteOnlyMapped["Province"] = so.relationship("Province", back_populates="region")

    def __repr__(self):
        return "<Region {}>".format(self.name)


class Province(db.Model):
    """
    Province model for storing province details.

    Attributes:
        id (int): The primary key for the province.
        name (str): The name of the province.
        region_id (int): The ID of the region the province belongs to.
        region (Region): The region the province belongs to.
        cities (list): The cities in the province.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    region_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Region.id), index=True)

    region: so.Mapped[Region] = so.relationship("Region", back_populates="provinces")
    cities: so.WriteOnlyMapped["City"] = so.relationship("City", back_populates="province")

    def __repr__(self):
        return "<Province {}>".format(self.name)


class City(db.Model):
    """
    City model for storing city details.

    Attributes:
        id (int): The primary key for the city.
        name (str): The name of the city.
        province_id (int): The ID of the province the city belongs to.
        province (Province): The province the city belongs to.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    province_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Province.id), index=True)

    province: so.Mapped[Province] = so.relationship("Province", back_populates="cities")

    def __repr__(self):
        return "<City {}>".format(self.name)


class Restaurant(db.Model):
    """
    Restaurant model for storing restaurant details.

    Attributes:
        id (int): The primary key for the restaurant.
        name (str): The name of the restaurant.
        address (str): The address of the restaurant.
        city_id (int): The ID of the city the restaurant is located in.
        province_id (int): The ID of the province the restaurant is located in.
        region_id (int): The ID of the region the restaurant is located in.
        country_id (int): The ID of the country the restaurant is located in.
        city (City): The city the restaurant is located in.
        province (Province): The province the restaurant is located in.
        region (Region): The region the restaurant is located in.
        country (Country): The country the restaurant is located in.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    address: so.Mapped[str] = so.mapped_column(sa.String(120), nullable=False)
    city_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(City.id), index=True)
    province_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Province.id), index=True)
    region_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Region.id), index=True)
    country_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Country.id), index=True)

    city: so.Mapped[City] = so.relationship("City")
    province: so.Mapped[Province] = so.relationship("Province")
    region: so.Mapped[Region] = so.relationship("Region")
    country: so.Mapped[Country] = so.relationship("Country")

    def __repr__(self):
        return "<Restaurant {}>".format(self.name)


@login.user_loader
def load_user(id):
    """
    Loads a user by ID.

    Args:
        id (int): The ID of the user to load.

    Returns:
        User: The user object.
    """
    return db.session.get(User, int(id))
