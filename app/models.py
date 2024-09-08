from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Country(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)

    regions: so.WriteOnlyMapped["Region"] = so.relationship("Region", back_populates="country")

    def __repr__(self):
        return "<Country {}>".format(self.name)


class Region(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    country_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Country.id), index=True)

    country: so.Mapped[Country] = so.relationship("Country", back_populates="regions")
    provinces: so.WriteOnlyMapped["Province"] = so.relationship("Province", back_populates="region")

    def __repr__(self):
        return "<Region {}>".format(self.name)


class Province(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    region_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Region.id), index=True)

    region: so.Mapped[Region] = so.relationship("Region", back_populates="provinces")
    cities: so.WriteOnlyMapped["City"] = so.relationship("City", back_populates="province")

    def __repr__(self):
        return "<Province {}>".format(self.name)


class City(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    province_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Province.id), index=True)

    province: so.Mapped[Province] = so.relationship("Province", back_populates="cities")

    def __repr__(self):
        return "<City {}>".format(self.name)


class Restaurant(db.Model):
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
    return db.session.get(User, int(id))
