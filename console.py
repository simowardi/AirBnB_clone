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
PROMPT = "(hbnb) "
ERROR_CLASS_MISSING = "** class name missing **"
ERROR_CLASS_DOESNT_EXIST = "** class doesn\'t exist **"
ERROR_INSTANCE_ID_MISSING = "** instance id missing **"
ERROR_INSTANCE_NOT_FOUND = "** no instance found **"
ERROR_VALUE_MISSING = "** value missing **"

# need create & show & update & destroy & all


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for airbnb console"""

    prompt = PROMPT

    models = ["BaseModel", "User", "State", "City", "Amenity",
              "Place", "Review"]
    cmds_names = ["create", "show", "update", "destroy", "all"]

    def parse_command_input(self, raw):
        """
        Parse Command Input
        Description:
        Parses the command input to handle compound commands
        like "ClassName.command()".
        Args:
        raw (str): The original input command.
        Returns:
        str: The modified argument.
        """
        if "." in raw and "(" in raw_cmd and ")" in raw_cmd:
            clss = raw.split(".")
            c = clss[1].split("(")
            args_list = c[1].split(")")

            if clss[0] in HBNBCommand.models and c[0] in HBNBCommand.cmds_name:
                # Modify the argument accordingly
                raw = c[0] + " " + clss[0] + " " + args_list[0]

        return raw

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

    def do_create(self, model_name):
        """Create New Instance
        Description:
        Creates a new instance of a model, saves it in the
        JSON file, and prints its ID to the console.
        model_name (str): the type of model to create
        """

        if not model_name:
            print(ERROR_CLASS_MISSING)
        elif model_name not in HBNBCommand.models:
            print(ERROR_CLASS_DOESNT_EXIST)
        else:
            dict_models = {"BaseModel": BaseModel, "User": User,
                           "State": State, "City": City, "Amenity": Amenity,
                           "Place": Place, "Review": Review}

            obj_model = dict_models[model_name]()
            print(obj_model.id)
            obj_model.save()

    def do_destroy(self, model_name):
        """
        Delete Instance
        Description:
        Destroy & delete an instance based model's name and id
        model_name : the model's name and id
        """
        if not model_name:
            print(ERROR_CLASS_MISSING)
            return

            model = model_name.split(" ")

            if model[0] not in HBNBCommand.models:
                print(ERROR_CLASS_DOESNT_EXIST)

            elif len(model) == 1:
                print(ERROR_INSTANCE_ID_MISSING)

            else:
                all_objcts = storage.all()

                for key, val in all_objcts.items():
                    ob_name = val.__class__.__name__
                    ob_id = val.id

                    if ob_name == model[0] and ob_id == model[1].strip('"'):
                        del val
                        del storage._FileStorage__objects[key]
                        storage.save()
                        return

                print(ERROR_INSTANCE_NOT_FOUND)

    def do_show(self, model_name):
        """
        Print Instances
        Description:
        Show by print a string representation of an instance based
        on the model name and id.
        model_name (model): the model's name and id
        """
        if not model_name:
            print(ERROR_CLASS_MISSING)
            return

        model = model_name.split(" ")

        if model[0] not in HBNBCommand.models:
            print(ERROR_CLASS_DOESNT_EXIST)

        elif len(model) == 1:
            print(ERROR_INSTANCE_ID_MISSING)

        else:
            all_objcts = storage.all()

            for key, val in all_objcts.items():
                ob_name = val.__class__.__name__
                ob_id = val.id

                if ob_name == model[0] and ob_id == model[1].strip('"'):
                    print(val)
                    return

            print(ERROR_INSTANCE_NOT_FOUND)

    def do_all(self, model_name):
        """
        Print All Instances
        Description:
        Prints the string representation of all instances of a
        given model. In the absence of a model,
        it prints all instances of all models.
        model_name : an optional model's name
        """
        if not model_name:
            print(ERROR_CLASS_MISSING)
            return

        model = model_name.split(" ")

        if model[0] not in HBNBCommand.models:
            print(ERROR_CLASS_DOESNT_EXIST)

        else:
            all_objcts = storage.all()
            list_objcts = []

            for key, val in all_objcts.items():
                ob_name = val.__class__.__name__

                if ob_name == model[0]:
                    list_objcts += [val.__str__()]
            print(list_objcts)

    def do_update(self, model_name):
        """
        Update Instance Attributes
        Description:
        Updates the attributes of an instance of a given model
        based on the model's name and id
        model_name : the name and id of a given model
        """
        if not model_name:
            print(ERROR_CLASS_MISSING)
            return

        argv = ""
        for model in model_name.split(","):
            argv += model

        model = shlex.split(argv)

        if model[0] not in HBNBCommand.models:
            print(ERROR_CLASS_DOESNT_EXIST)

        elif len(model) == 1:
            print(ERROR_INSTANCE_ID_MISSING)

        else:
            all_objcts = storage.all()

            for key, val in all_objcts.items():
                ob_name = val.__class__.__name__
                ob_id = val.id

                if ob_name == model[0] and ob_id == model[1].strip('"'):
                    if len(model) == 2:
                        print("** attribute name missing **")
                    elif len(model) == 3:
                        print(ERROR_VALUE_MISSING)

                    else:
                        setattr(val, model[2], model[3])
                        storage.save()
                        return

            print(ERROR_INSTANCE_NOT_FOUND)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
