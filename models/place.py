#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String, INTEGER, FLOAT
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(FLOAT, nullable=False, default=0)
    longitude = Column(FLOAT, nullable=False, default=0)
    amenity_ids = []
