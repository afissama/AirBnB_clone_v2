#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, ForeignKey, String, INTEGER, FLOAT
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

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
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            """returns the list of City instances with
            state_id equals to the current State.id"""

            from models import storage
            from models.review import Review

            all_reviews = storage.all(Review)
            reviews = list()
            for rv_key in all_reviews.keys():
                if self.id in rv_key:
                    reviews.append(all_reviews[rv_key])
            return reviews
