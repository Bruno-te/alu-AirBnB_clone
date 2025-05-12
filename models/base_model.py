#!/usr/bin/python3
"""
BaseModel class for alu-AirBnB_clone.
Defines common attributes/methods for all classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel with id, created_at, updated_at, etc."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance or recreate from dictionary."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values
        of __dict__ plus the class name.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy

