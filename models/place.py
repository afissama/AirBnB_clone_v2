#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, ForeignKey, String, INTEGER, FLOAT
from models.base_model import Base, BaseModel
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Table


class Place(BaseModel, Base):
    """ A place to stay """


    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(FLOAT, nullable=True, default=0)
    longitude = Column(FLOAT, nullable=True, default=0)
    place_amenity = Table("place_amenity", Base.metadata,
                            Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
                            Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
                        )
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
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

        @property
        def amenities(self):
            """
            Returns all amenities
            """
            from models import storage
            from models.amenity import Amenity

            all_amenities = storage.all(Amenity)
            amenities = list()
            for amenity_key in all_amenities.keys():
                if amenity_key in self.amenity_ids:
                    amenities.append(all_amenities[amenity_key])
            return amenities
        
        @amenities.setter
        def amenities(self, value):
            """
            append method for adding an Amenity.id to the attribute amenity_ids
            """
            from models.amenity import Amenity

            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
