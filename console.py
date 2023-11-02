#!/usr/bin/python3
'''
Module to create a console to add interactivity to our
project where admin users can update add delete
'''

import cmd
from models.base_model import BaseModel
import models
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''
    Console class to create a console
    '''

    prompt = "(hbnb) "
    valid_classes = ['BaseModel', 'User', 'State',
                     'City', 'Amenity', 'Place', 'Review']
    def emptyline(self):
        pass

    def do_quit(self, arg):
        '''
        Exit from the console
        '''
        exit(0)

    def do_EOF(self, line):
        '''
        End-of-file
        '''

        return True

    def do_create(self, arg):
        '''
        Command to create a new instance of BaseModel
        Usage: create <name of model to create>
        '''

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        obj = eval(args[0])()
        print(obj.id)
        models.storage.new(obj)
        models.storage.save()

    def do_show(self, arg):
        '''
        Command to show string represantation of
        object given by id and class name
        ---------------------------------
        Usage: show <class name> <id>
        '''

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            object = models.storage.all()
            print(str(object[f"{args[0]}.{args[1]}"]))
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Command to delete an instance
        given by id and class name
        ---------------------------------
        Usage: destroy <class name> <id>
        '''

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            object = models.storage.all()
            del object[f"{args[0]}.{args[1]}"]
            models.storage.save()
        except Exception as e:
            print("** no instance found **")

    def do_all(self, arg):
        '''
        Command to show a string represantation of all objects created if
        all command has no other arguments or a represantaion of all objects
        of given class name if an argument is supplied
        --------------------------------------------------------------------
        Usage: all <class name><-(optional it can be ignored) ex: all
        '''
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values()
               if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        '''
        Command to update an instance
        attritube one at a time given
        by id and class name
        ---------------------------------
        Usage: update <class name> <id> <attribute name> "<attribute value"
        '''

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            object = models.storage.all()[f"{args[0]}.{args[1]}"]
            setattr(object, args[2], args[3])
            models.storage.save()
        except Exception as e:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
