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
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        The String representation when instance printed:
        Description:
        Creates a string representation of this instance object.
        Returns:
        A string of this model instance.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        This method tracks the date the instance object was updated
        """
        self.updated_at = datetime.today()
        models.storage.save()

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
