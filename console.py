#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Allow clean exit with Ctrl-D"""
        return True

    def emptyline(self):
        """Prevents exiting the program if an emptyline is passed"""
        pass

    def do_create(self, class_name):
        """Command to create a new instance of BaseModel.
        Automatically saves it to the JSON file and prints the id.

        Args:
            class_name (str): Name of the class to create an instance of"""

        if not class_name:
            print("** class name missing **")
            return

        if class_name != BaseModel.__name__ and class_name != User.__name__:
            print("** class doesn't exist **")
            return

        if class_name == BaseModel.__name__:
            obj = BaseModel()
        elif class_name == User.__name__:
            obj = User()

        obj.save()
        print(obj.id)

    def check_args(argv):
        """Checks if the command line arguments are valid"""
        if not argv or argv[0] is None:
            print("** class name missing **")
            return

        if argv[0] != BaseModel.__name__ and argv[0] != User.__name__:
            print("** class doesn't exist **")
            return

        if len(argv) < 2:
            print("** instance id missing **")
            return

        my_class = argv[0]
        my_id = argv[1]

        obj = str(my_class) + "." + str(my_id)
        objects = storage.all()

        if obj not in objects:
            print("** no instance found **")
            return

        return True

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id

        Args:
            args (str): Class of the instance to show followed by its id
        """

        argv = args.split()

        if HBNBCommand.check_args(argv):
            my_class = argv[0]
            my_id = argv[1]

            obj = str(my_class) + "." + str(my_id)
            objects = storage.all()

            print(objects[obj])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (saves the change into the JSON file)

        Args:
            args (str): Class of the instance to delete followed by its id
        """

        argv = args.split()

        if HBNBCommand.check_args(argv):
            my_class = argv[0]
            my_id = argv[1]

            obj = str(my_class) + "." + str(my_id)
            objects = storage.all()

            del(objects[obj])
            storage.save()

    def do_all(self, class_name):
        """Prints all string representation of all instances based or not
        on the class name

        Args:
            class_name (str, optional): Class to show the objects of
        """

        objects = storage.all()

        if not class_name:
            for obj in objects.values():
                print(str(obj))

        else:
            if class_name != BaseModel.__name__ and \
                    class_name != User.__name__:
                print("** class doesn't exist **")
                return

            instances = []
            for obj in objects.values():
                if isinstance(obj, BaseModel):
                    instances.append(str(obj))

            print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Args:
            args (str): Class name followed by id, attribute name and
            "attribute value"
        """

        argv = args.split()

        if not HBNBCommand.check_args(argv):
            return

        if len(argv) < 3:
            print("** attribute name missing **")
            return

        if len(argv) < 4:
            print("** value missing **")
            return

        objects = storage.all()
        obj = str(argv[0]) + "." + str(argv[1])
        attr = argv[2]
        value = argv[3]

        setattr(objects[obj], attr, value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
