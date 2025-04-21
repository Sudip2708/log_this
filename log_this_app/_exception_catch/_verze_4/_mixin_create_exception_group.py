from typing import Any, Callable, Type

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC, abc_property


class CreateExceptionGroupMixin(ABC):


    def create_exception_group(
            self,
            group_name: str,
            *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Vytvoření skupiny příbuzných výjimek.

        :param group_name: Název skupiny výjimek
        :param exception_types: Typy výjimek ve skupině
        :return: Instance ExceptionHandleru
        """

        self._exception_groups[group_name] = list(exception_types)

        return self