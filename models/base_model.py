#!/usr/bin/python3

"""
Module to houses the BaseModel class
where other classes inherits from
"""


from models import storage
from uuid import uuid4
from datetime import datetime


strptime = datetime.strptime
dformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class where other class inherits from
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        initializes all instance of the BaseModel class
        """
        if kwargs:
            kwargs['created_at'] = strptime(kwargs['created_at'], dformat)
            kwargs['updated_at'] = strptime(kwargs['updated_at'], dformat)
            self.update_attribute(**kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        obj_key = f"{self.__class__.__name__}.{self.id}"

        if obj_key not in storage._FileStorage__objects:
            storage.new(self)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
        return

    def to_dict(self) -> dict:
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance:
              by using self.__dict__, only instance attributes
              set will be returned
              a key __class__ must be added to this dictionary
              with the class name of the object
              created_at and updated_at must be converted to
              string object in ISO format:
              format: %Y-%m-%dT%H:%M:%S.%f
              (ex: 2017-06-14T22:31:03.285259)
              you can use isoformat() of datetime object
              This method will be the first piece of the
              serialization/deserialization process:
              create a dictionary representation with
              “simple object type” of our BaseModel
        """
        properties = self.__dict__.copy()
        properties['__class__'] = self.__class__.__name__
        properties['created_at'] = properties['created_at'].isoformat()
        properties['updated_at'] = properties['updated_at'].isoformat()
        return properties

    def update_attribute(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if k == '__class__':
                continue
            setattr(self, k, v)
