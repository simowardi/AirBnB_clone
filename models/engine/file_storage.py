#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, objct):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = objct.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, objct.id)] = objct

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""

        objcts = dict()
        for key, value in FileStorage.__objects.items():
            objcts[key] = value.to_dict().copy()
        with open(self.__file_path, "w", encoding="UTF-8") as objct_file:
            json.dump(objcts, objct_file)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects,
        if the file exists.
        """
        modls_dicts = {"BaseModel": BaseModel, "User": User, "State": State,
                       "City": City, "Amenity": Amenity, "Place": Place,
                       "Review": Review}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as ob_fi:
                for key, val in json.load(ob_fi).items():
                    self.new(modls_dicts[value["__class__"]](**val))
