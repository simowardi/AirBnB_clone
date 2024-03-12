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

        from models import storage

        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeform)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)

    def save(self):
        """
        This method tracks the date the instance object was updated
        """
        from models import storage

        self.updated_at = datetime.today()
        storage.save()

    def __str__(self):
        """
        The String representation when instance printed:
        Description:
        Creates a string representation of this instance object.
        Returns:
        A string of this model instance.
        """

        string = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return string

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_rdict = self.__dict__.copy()
        my_rdict["created_at"] = self.created_at.isoformat()
        my_rdict["updated_at"] = self.updated_at.isoformat()
        my_rdict["__class__"] = self.__class__.__name__
        return my_rdict
