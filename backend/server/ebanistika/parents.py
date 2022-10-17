from .ebExceptions import *


class Model:
    def __init__(self) -> None:
        pass

    def varChar(self, **kwargs) -> dict:
        arguments = {
            'name': None,
            'length': None,
            'nullable': False,
            'field': 'varchar'
        }
        explicit = kwargs.keys() - arguments.keys()
        if explicit:
            raise UnknownArgumentError(explicit.pop())
        arguments.update(kwargs)
        self.validateArguments(**arguments)

        return arguments

    def bigInteger(self, **kwargs) -> dict:
        arguments = {
            'name': None,
            'nullable': False,
            'field': 'bigInteger'
        }
        explicit = kwargs.keys() - arguments.keys()
        if explicit:
            raise UnknownArgumentError(explicit.pop())
        arguments.update(kwargs)
        self.validateArguments(**arguments)

        return arguments

    def integer(self, **kwargs) -> dict:
        arguments = {
            'name': None,
            'nullable': False,
            'field': 'integer'
        }
        explicit = kwargs.keys() - arguments.keys()
        if explicit:
            raise UnknownArgumentError(explicit.pop())
        arguments.update(kwargs)
        self.validateArguments(**arguments)

        return arguments

    def bigSerial(self, **kwargs) -> dict:
        arguments = {
            'name': None,
            'primary': False,
            'field': 'bigSerial'
        }
        arguments.update(kwargs)
        explicit = kwargs.keys() - arguments.keys()
        if explicit:
            raise UnknownArgumentError(explicit.pop())
        self.validateArguments(**arguments)
        
        return arguments

    def serial(self, **kwargs) -> dict:
        arguments = {
            'name': None,
            'primary': False,
            'field': 'serial'
        }
        arguments.update(kwargs)
        explicit = kwargs.keys() - arguments.keys()
        if explicit:
            raise UnknownArgumentError(explicit.pop())
        self.validateArguments(**arguments)
        
        return arguments

    def date(self, **kwargs):
        pass

    def validateArguments(self, **kwargs):
        for name, val in kwargs.items():
            if (name == 'primary' and not isinstance(val, bool)) or (name == 'nullable' and not isinstance(val, bool)):
                raise ArgumentValidationError(name)  
            elif not val and name != 'primary' and name != 'nullable':
                raise ArgumentValidationError(name)


class Serializer:
    def __init__(self) -> None:
        pass
    
    
    
