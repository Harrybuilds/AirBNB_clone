#!/usr/bin/python3

"""
Module to handle the Console Application
for the AirBnB project
"""

from cmd import Cmd
from models.user import User
from models.base_model import BaseModel
import models.base_model as BM
import sys


storage = BM.storage._FileStorage__objects
saveToFile = BM.storage


class HBNBCOMMAND(Cmd):
    classes = BM.storage.classes()
    prompt = "(hbnb) "

    def do_EOF(self, command):
        """
        func -> exit/quit the console Application when called upon
        command -> command to be passed

        Usage: quit || EOF
        """
        return True

    # aliasing the quit command to point to the do_EOF command
    do_quit = do_EOF

    def emptyline(self) -> None:
        pass

    def precmd(self, line):
        """
        receives the command from the command line
        and handle any pre-processing to the command
        before calling on all other needed methods
        """
        if "()" in line and "." in line:
            line = line.replace('(', ' ').replace(')', ' ')
            line = line.split(".", maxsplit=1)
            line = f"{line[1]} {line[0].capitalize()}"
        elif "()" not in line and '.' in line:
            line = line.split(".", maxsplit=1)
            line = f"{line[1]} {line[0].capitalize()}"
        if not sys.stdin.isatty():
            return line
        else:
            return line

    def do_create(self, classname):
        """
        func -> Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id. Ex: $ create BaseModel
        If the class name is missing
        print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ create MyModel)

        classname -> className of instance to be created

        Usage: create BaseModel
        """
        if classname:
            if classname not in HBNBCOMMAND.classes:
                print("** class doesn't exist **")
            else:
                instance = eval(classname + "()")
                saveToFile.save()
                print(instance.id)
        else:
            print('** class name missing **')

    def do_show(self, instanceDetails):
        """
        func -> Prints the string representation of an instance
        based on the class name and id.

        Ex: $ show BaseModel 1234-1234-1234.

        If the class name is missing,
        print ** class name missing ** (ex: $ show)

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ show MyModel)

        If the id is missing,
        print ** instance id missing ** (ex: $ show BaseModel)

        If the instance of the class name doesn’t exist for
        the id,
        print ** no instance found **
        (ex: $ show BaseModel 121212)

        instanceDetails -> details of ths instance
        to view its details

        Usage: show BaseModel 1234-1234-1234.
        """
        if instanceDetails:
            splitted_command = instanceDetails.split(" ")
            className = splitted_command[0]
            if className not in HBNBCOMMAND.classes:
                print("** class doesn't exists **")
            else:
                if len(splitted_command) < 2:
                    print("** instance id missing **")
                else:
                    instanceId = splitted_command[1]
                    classWithId = f"{className}.{instanceId}"
                    if classWithId not in storage:
                        print("** no instance found **")
                    else:
                        print(storage.get(classWithId))

        else:
            print("** class name missing **")

    def do_destroy(self, instanceDetails):
        """
        func -> Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.

        If the class name is missing,
        print ** class name missing ** (ex: $ destroy)

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex:$ destroy MyModel)

        If the id is missing,
        print ** instance id missing ** (ex: $ destroy BaseModel)

        If the instance of the class name doesn’t exist
        for the id,
        print ** no instance found **
        (ex: $ destroy BaseModel 121212)

        Usage: destroy BaseModel 1234-1234-1234.
        """
        if instanceDetails:
            splitted_command = instanceDetails.split(" ")
            className = splitted_command[0]
            if className not in HBNBCOMMAND.classes:
                print("** class doesn't exists **")
            else:
                if len(splitted_command) < 2:
                    print("** instance id missing **")
                else:
                    instanceId = splitted_command[1]
                    classWithId = f"{className}.{instanceId}"
                    if classWithId not in storage:
                        print("** no instance found **")
                    else:
                        del storage[classWithId]
                        saveToFile.save()

        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        func -> Prints all string representation of
        all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.

        The printed result must be a list of strings

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ all MyModel)

        Usage: all BaseModel || all
        """
        if line:
            con = storage
            cName = line.split(" ")[0]
            if cName in HBNBCOMMAND.classes:
                sClass = [str(con[k]) for k in con if k.startswith(cName)]
                print(sClass)
            else:
                print("** class doesn't exist **")
        else:
            allobj = [str(storage[k]) for k in storage]
            print(allobj)

    def do_update(self, attribute):
        """
        func -> Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Only one attribute can be updated at the time

        You can assume the attribute name is valid
        (exists for this model)

        The attribute value must be casted to the attribute type

        If the class name is missing,
        print ** class name missing ** (ex: $ update)

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ update MyModel)

        If the id is missing,
        print ** instance id missing ** (ex: $ update BaseModel)

        If the instance of the class name doesn’t exist for the id,
        print ** no instance found **
        (ex: $ update BaseModel 121212)

        If the attribute name is missing,
        print ** attribute name missing **
        (ex: $ update BaseModel existing-id)

        If the value for the attribute name doesn’t exist,
        print ** value missing **
        (ex: $ update BaseModel existing-id first_name)

        All other arguments should not be used
        (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        first_name "Betty" = $ update BaseModel 1234-1234-1234
        email "aibnb@mail.com")

        id, created_at and updated_at cant’ be updated.
        You can assume they won’t be passed in the update command

        Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if attribute:
            skip_fields = ['id', 'created_at', 'updated_at']
            splitted_command = attribute.split(" ")
            className = splitted_command[0]
            if className not in HBNBCOMMAND.classes:
                print("** class doesn't exist **")
            else:
                if len(splitted_command) < 2:
                    print("** instance id missing **")
                else:
                    instanceId = splitted_command[1]
                    classWithId = f"{className}.{instanceId}"
                    if classWithId not in storage:
                        print("** no instance found **")
                    else:
                        theInstance = storage.get(classWithId).__dict__
                        if len(splitted_command) < 3:
                            print("** attribute name missing **")
                        else:
                            field = splitted_command[2]
                            if field in skip_fields:
                                pass
                            else:
                                isField = theInstance.get(field)
                                if isField:
                                    if len(splitted_command) < 4:
                                        print("** value missing **")
                                    else:
                                        value = splitted_command[3]
                                        theInstance[field] = value
                                        saveToFile.save()
                                else:
                                    print("** value missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCOMMAND().cmdloop()
