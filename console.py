#!/usr/bin/python3
'''
Module to create a console to add interactivity to our
project where admin users can update add delete
'''


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()