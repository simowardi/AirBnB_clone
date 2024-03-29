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
ERROR_ATTRIBUTE_NAME_MISSING = "** attribute name missing **"


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for airbnb console"""

    prompt = PROMPT

    models = ["BaseModel", "User", "State", "City", "Amenity",
              "Place", "Review"]
    cmd_names = ["create", "show", "update", "destroy", "all"]

    def parse_cmd_in(self, raw):
        """
        Parses the command input to handle compound commands
        like "ClassName.command()".
        raw (str): The original input command.
        Returns: The modified argument.
        """
        if "." in raw and "(" in raw and ")" in raw:
            clss = raw.split(".")
            c = clss[1].split("(")
            args_list = c[1].split(")")

            if clss[0] in HBNBCommand.models and c[0] in HBNBCommand.cmd_names:
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
        print("Quit command to exit the program\n")

    def emptyline(self):
        """a fun that pass if empty line is entered by user"""
        pass

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def do_create(self, model_name):
        """Usage: create <class>
        Creates a new instance of a model, saves it in the
        JSON file, and prints its ID to the console.
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

    def do_show(self, model_name):
        """Usage: show <class> <id> or <class>.show(<id>)
        Show by print a string representation of an instance based
        on the model name and id.
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

    def do_destroy(self, model_name):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Destroy & delete an instance based model's name and id
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

    def do_all(self, model_name):
        """Usage: all or all <class> or <class>.all()
        Prints the string representation of all instances of a
        given model. In the absence of a model,
        it prints all instances of all models.
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
        """Usage: count <class> or <class>.count()
        Updates the attributes of an instance of a given model
        based on the model's name and id
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
                        print("** value missing **")
                    else:
                        setattr(val, model[2], model[3])
                        storage.save()
                        return

            print(ERROR_INSTANCE_NOT_FOUND)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
