#!/usr/bin/python3
"""
Defines the FileStorage class
Serializes instances to JSON file and deserializes JSON file to instances
"""
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:    
	"""Serializes instances to a JSON file and 
	represent an abstracted storage engine.

    Attributes:
        __file_path (str): name of the file to save objects to.
        __objects (dict): dictionary of instantiated objects.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
		"""Return the dictionary __objects."""

        return FileStorage.__objects

    def new(self, cstm_objct):
		"""Set in __objects custom_object with key <obj_class_name>.id"""

		objclsname = cstm_objct.__class__.__name__
		FileStorage.__objects["{}.{}".format(objclsname, cstm_objct.id)] = cstm_objct

    def save(self):
    """
    Serializes FileStorage.__objects to a JSON file
    """

    with open(FileStorage.__file_path, 'w+') as fh:
        srl_objct = {}
        for cstm_objct, value in FileStorage.__objects.items():
            srl_objct[cstm_objct] = value.to_dict()
        json.dump(srl_objct, fh)


    def reload(self):
        """
        deserializes instances from json file, if it exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as fh:
                srl_objct = json.loads(fh.read())
                from models.base_model import BaseModel
                Classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                }
                for cstm_objct, value in srl_objct.items():
                    class_name  = value.get('__class__')
                    if class_name  in Classes:
                        FileStorage._objects[cstm_objct] = Classes[class_name ](**value)

        except FileNotFoundError:
            pass
