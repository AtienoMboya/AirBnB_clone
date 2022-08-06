#!/usr/bin/python3
"""user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """represent a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instance with base class"""
        super().__init__(self, *args, **kwargs)