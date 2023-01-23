#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """returns the list of City instances with
            state_id equals to the current State.id"""

            from models import storage
            from models.city import City

            all_cities = storage.all(City)
            cities = list()
            for city_key in all_cities.keys():
                if self.id in city_key:
                    cities.append(all_cities[city_key])
            return cities
