#!/usr/bin/python3
"""
Defines the base model for various classes
"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes and methods 
	for other classes in the BaseModel of the HBnB project.
	"""

    def __init__(self, *args, **kwargs):
        ""a new BaseModel Initialization.
		Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']

            kwargs['created_at'] = datetime.strptime(kwargs['created_at'])
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'])

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            from . import inst_storage
            inst_storage.new(self)

    def __str__(self):
		""The String representation when instance printed:

        Description:
        Creates a string representation of this instance object.

        Returns:
        A string of this model instance.
        """

		string = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
		return string

    def save(self):
		"""Save updates to instance

        Description:
        This method tracks the date the instance object was updated
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
		"""A dictionary representation of an instance

        Description:
        Creates a dictionary representation of this instance object.
        It contains the class name of the object, the date and time
        the instance object was created and last updated

        Returns:
        Returns a dictionary of this model instance
        """

		dirre = self.__dict__.copy()
        dirre["created_at"] = self.created_at.isoformat()
        dirre["updated_at"] = self.updated_at.isoformat()
        dirre["__class__"] = self.__class__.__name__
        return dirre
