from typing import Any, Type, Union, get_origin, get_args

from ..._validators import (
    validate_native_type,
    validate_typing,
    validate_condition
)

class BaseTypeValidator:
    
    # Pojmenování typu (dle get_origin())
    GET_ORIGIN = None

    # Validační metoda pro koncovou validaci
    validate_native_type = validate_native_type

    # Metoda pro validaci typing anotace
    validate_typing = validate_typing

    # Metoda pro validaci bool podmínky
    validate_condition = validate_condition

    # Metoda která se bude přepisovat v každé třídě a bude obsahovat vlastní logiku pro validaci
    def validate(self, value, annotation, inner_check, custom_types, bool_only):
        return self.validate_native_type(value, self.GET_ORIGIN)

    @staticmethod
    def _reduce_depth_check(depth_check):
        """Metoda sníží hodnotu pro kontrolu vnitřních položek"""
        if isinstance(depth_check, int):
            depth_check = depth_check - 1 if depth_check >= 0 else 0
        return depth_check

    # @staticmethod
    # def _get_first_arg(annotation):
    #     """Vrátí první typový argument (např. pro List[T]) nebo Any"""
    #     return get_args(annotation)[0] if get_args(annotation) else Any
    #
    # @staticmethod
    # def _get_all_args_as_tuple(annotation):
    #     """Vrátí všechny typové argumenty jako tuple (např. Tuple[int, str])"""
    #     return get_args(annotation) or (Any,)