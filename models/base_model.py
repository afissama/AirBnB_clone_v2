#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import copy
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class.
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:

            if "updated_at" in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(
                                                         kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                 )
            if "created_at" in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(
                                                         kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                           )

            if "__class__" in kwargs.keys():
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation
        of the instance
        """

        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        tmp_dict = self.__dict__
        if "_sa_instance_state" in tmp_dict.keys():
            del tmp_dict["_sa_instance_state"]

        return "[" + self.__class__.__name__ + \
            "] (" + self.id + ") " + str(tmp_dict)

    def __repr__(self) -> str:
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        temp = copy.deepcopy(self.__dict__)

        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "_sa_instance_state" in temp.keys():
            del temp["_sa_instance_state"]
        return temp

    def delete(self):
        """Delete  the current instance from the storage"""
        from models import storage
        storage.delete(self)
