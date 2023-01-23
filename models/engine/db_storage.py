""" Module for storage in DB"""
import os
from sqlalchemy import create_engine

from models.base_model import Base
from models import place, city, state, amenity, user

class DBStorage():
    """ DataBase Storage class"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all()
    
    def all(self, cls=None):
        _dict_objects = {}
        rows = self.__session.query(eval(cls)).all()
        
        if cls is not None:
            for row in rows:
                _dict_objects[cls + "." + row.id] = row
            return _dict_objects
        
        _dict_objects = {**_dict_objects, **self.all(user.User)}
        _dict_objects = {**_dict_objects, **self.all(state.State)}
        _dict_objects = {**_dict_objects, **self.all(city.City)}
        _dict_objects = {**_dict_objects, **self.all(amenity.Amenity)}
        _dict_objects = {**_dict_objects, **self.all(place.Place)}
        
        return _dict_objects

    def new(self, obj):
        "add the object to the current database session"
        self.__session.add(obj)

    def save(self):
        "Commit all changes"
        self.__session.commit()

    def delete(self, obj=None):
        "Delete obj from dataset"

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        ""
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.orm import scoped_session
        Base.metadata.create_all(self.__engine)
        
        sm = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sm)

        self.__session = Session()
