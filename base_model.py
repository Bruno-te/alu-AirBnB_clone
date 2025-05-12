#!/usr/bin/python3
"""
BaseModel module for alu-AirBnB_clone project.

This class defines all common attributes and methods
for other classes in the project.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all AirBnB clone models."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update `updated_at` and save the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

