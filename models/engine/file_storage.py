#!/usr/bin/python3

"""
module that houses the FileStorage Class which handles the
storage and retrival of data stored in a file in JSON
string format
"""


from os import path
from json import dump, load


class FileStorage:
    """
    class that handles storage and retrival of data in/from a file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj) -> None:
        """
        sets in __objects the obj with key <obj class name>.id
        """
        objWithId = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[objWithId] = obj

    def save(self) -> None:
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj = {}

        for k, v in FileStorage.__objects.items():
            obj[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            dump(obj, json_file)
        return

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as reader:
                from models.base_model import BaseModel
                from models.user import User
                data = load(reader)
                for k, v in data.items():
                    className = v['__class__']
                    obj = eval(className + "(**v)")
                    FileStorage.__objects[k] = obj

    def classes(self):
        """
        return a dictionary containing all classes
        available in the storage holder
        """
        return list({key.split('.')[0] for key in FileStorage.__objects})
