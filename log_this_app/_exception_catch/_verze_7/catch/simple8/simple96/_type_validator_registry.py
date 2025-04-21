from typing import Any, Type, Union, get_origin, get_args

from .type_validators import ListValidator

class TypeValidatorRegistry:

    def __init__(self, value_validator):
        self.validators = {
            list: ListValidator(value_validator)

        }

    # key = get_origin(annotation)
    def get_validator(self, key):
        if key in self.validators:
            return self.validators[key]
        return None
