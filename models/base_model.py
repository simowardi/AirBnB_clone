#!/usr/bin/python3
"""Defines the base model for various classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes and methods
    for other classes in the BaseModel of the HBnB project.
    """

    def __init__(self, *args, **kwargs):
        """
        A new BaseModel Initialization.
        Args:
        *args (any): Unused.
        **kwargs (dict): Key/value pairs of attributes.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, timeform)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """
        Tracks the date the instance object was last updated.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """
        The String representation when instance printed:
        Description:
        Creates a string representation of this instance object.
        Returns:
        A string of this model instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_rdict = self.__dict__.copy()
        my_rdict["created_at"] = self.created_at.isoformat()
        my_rdict["updated_at"] = self.updated_at.isoformat()
        my_rdict["__class__"] = self.__class__.__name__
        return my_rdict
