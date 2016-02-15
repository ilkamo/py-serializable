import json

class Serializable(object):
    """
    Thanks to this class, each object can be serializable.
    I created it because I like saving my objects in key -> value storage systems.
    In this way, you can create a class that extends this one in order to obtain
    a serializable object.

    You can save an object into the database as text using the json_me() method.
    You can recreate the same object from text using its constructor. 
    For more info, see the how_to.py file.
    """

    """List of the required class parameters"""
    params = []

    def __init__(self, **kwargs):
        for param in self.params:
            if isinstance(param, tuple) and isinstance(kwargs[param[0]], param[1]):
                setattr(self, param[0], kwargs[param[0]])
            else:
                setattr(self, param, kwargs[param])

    def json_me(self):
        """Returns a string representation of the object"""
        temp_dict = dict()

        for key in self.__dict__:
            temp_dict[key] = getattr(self, key)

        temp_dict['__class__'] = self.__class__.__name__

        return json.dumps(temp_dict)
