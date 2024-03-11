#!/usr/bin/python3
"""Module for command line interface implementation"""

import cmd
import json
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Constants
PROMPT = '(hbnb) '


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for airbnb console"""

    prompt = PROMPT

    cmds_models = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]

    cmds_name = ["create", "show", "update", "destroy", "all", "count"]

    def parse_command_input(self, raw):
        """Parse Command Input
        Description:
        Parses the command input to handle compound commands
        like "ClassName.command()".
        Args:
        raw (str): The original input command.
        Returns:
        str: The modified argument.
        """
        if "." in raw and "(" in raw_cmd and ")" in raw_cmd:
            class_c = raw.split(".")
            c = class_c[1].split("(")
            args_list = c[1].split(")")

            if class_c[0] in HBNBCommand.models and c[0] in HBNBCommand.cmds:
                # Modify the argument accordingly
                raw = c[0] + " " + class_c[0] + " " + args_list[0]

        return raw_cmd

    def do_EOF(self, line):
        """End of file = CTRL+D to exit the program"""
        print("")
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_quit(self, line):
        """a fun that exit the program\n"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def emptyline(self):
        """a fun that pass if empty line is entered by user"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
