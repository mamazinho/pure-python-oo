"""
This class converts an object to Category type.
"""


class Category:

    def __init__(self, name:str, description:str, id:int=None):
        self.name = name
        self.description = description
        self.id = id
