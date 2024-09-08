from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return "<User {}>".format(self.username)


class Country(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)

    regions: so.WriteOnlyMapped["Region"] = so.relationship(back_populates="countries")

    def __repr__(self):
        return "<Country {}>".format(self.name)


class Region(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    country_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Country.id), index=True)

    countries: so.Mapped[Country] = so.relationship(back_populates="regions")
    provinces: so.WriteOnlyMapped["Province"] = so.relationship(back_populates="regions")

    def __repr__(self):
        return "<Region {}>".format(self.name)


class Province(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    region_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Region.id), index=True)

    regions: so.Mapped[Region] = so.relationship(back_populates="provinces")
    cities: so.WriteOnlyMapped["City"] = so.relationship(back_populates="provinces")

    def __repr__(self):
        return "<Province {}>".format(self.name)


class City(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True)
    province_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Province.id), index=True)

    provinces: so.Mapped[Province] = so.relationship(back_populates="cities")

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

    cities: so.Mapped[City] = so.relationship()
    provinces: so.Mapped[Province] = so.relationship()
    regions: so.Mapped[Region] = so.relationship()
    countries: so.Mapped[Country] = so.relationship()

    def __repr__(self):
        return "<Restaurant {}>".format(self.name)
