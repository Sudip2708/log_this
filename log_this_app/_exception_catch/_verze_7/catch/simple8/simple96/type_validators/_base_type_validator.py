from typing import Any, Type, Union, get_origin, get_args


class TypeValidator:

    VALIDATOR_TYPE = None

    def __init__(self, value_validator):
        self.value_validator = value_validator

    def validate(self, value, annotation, inner_check=True):
        raise NotImplementedError("Musí být implementováno v podtřídě")
