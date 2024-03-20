#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from os import path

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    module = __import__("models." + cls_name, fromlist=[cls_name])
                    cls = getattr(module, cls_name)
                    self.__objects[key] = cls(**value)
