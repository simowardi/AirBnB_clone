#!/usr/bin/python3
""" import all the necessary modules """

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class for airbnb console """
    prompt = "hbnb"

    def _EOF(self, line):
        """End of file = CTRL+D to exit the program"""
        return True

    def _quit(self, line):
        """a fun that exit the program\n"""
        return True

    def _empty(self):
        """a fun that pass if empty line is entered by user"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

