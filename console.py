#!/usr/bin/python3
"""Console module"""


import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
