# class NameValidationError(Exception):
#     def __init__(self):
#         super().__init__("Name not given or incorrect data type. Please provide 'str' value.")

# class LengthValidationError(Exception):
#     def __init__(self):
#         super().__init__("Length not given or incorrect data type. Please provide 'int' value.")

# class NullableValidationError(Exception):
#     def __init__(self):
#         super().__init__("Please provide 'bool' value.")

# class NonOverridableError(Exception):
#     def __init__(self):
#         super().__init__("You cannot override this value. Use correct field instead.")

class UnknownArgumentError(Exception):
    def __init__(self, arg):
        super().__init__(f"Argument '{arg}' is not supported yet.")
    

class ArgumentValidationError(Exception):
    errors = {
        'name': "Name not given or incorrect data type. Please provide 'str' value.",
        'length': "Length not given or incorrect data type. Please provide 'int' value.",
        'nullable': "Please provide 'bool' value.",
        'primary': "Please provide 'bool' value."
    }

    def __init__(self, arg):
        super().__init__(self.errors[arg])
