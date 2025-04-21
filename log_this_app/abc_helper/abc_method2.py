from typing import Any, Callable, Optional, Type, List, Dict
import abc
import functools
import logging


def abc_method(
        name: str,
        return_type: Optional[Type] = None,
        log: bool = False,
        validate_types: bool = False,
        generate_docs: bool = False,
        *params: str
) -> Callable:
    """
    Rozšířená implementace abstraktní metody s flexibilními volbami.

    Args:
        name: Název metody
        return_type: Očekávaný návratový typ
        log: Přidat logging decorator
        validate_types: Přidat type validator
        generate_docs: Přidat dokumentační generator
        *params: Volitelné parametry metody

    Returns:
        Abstraktní metoda s volitelnými dekorátory
    """

    def method_decorator(func: Callable) -> Callable:
        # Základní nastavení stub metody
        func.__name__ = name
        if return_type:
            func.__annotations__['return'] = return_type

        # Aplikace volitelných dekorátorů
        if generate_docs:
            func = generate_abstract_method_docs()(func)

        if log:
            func = log_abstract_method(logging.INFO)(func)

        if validate_types:
            func = validate_abstract_method_types(func)

        # Finální aplikace abstractmethod
        return abc.abstractmethod(func)

    # Podpora pro dva způsoby použití
    def wrapper(func: Optional[Callable] = None) -> Callable:
        if func is None:
            return method_decorator
        return method_decorator(func)

    return wrapper


# # Příklady použití
# class ExampleClass(abc.ABC):
#     # Varianta 1: Plná konfigurace
#     process_data = abc_method(
#         "process_data",
#         return_type=bool,
#         log=True,
#         validate_types=True,
#         generate_docs=True
#     )
#
#     process_data1 = abc_method(
#         "process_data",
#         param = (data: List[int], config: Dict[str, Any], optional_param: Optional[str] = None),
#         return_type = bool,
#         log = True,
#         validate_types = True,
#         generate_docs = True,
#     )
#
#     process_data2 = abc_method(
#         "process_data",
#         param = (data, config, optional_param),
#         return_type = bool,
#         log = True,
#         validate_types = True,
#         generate_docs = True,
#     )
#
#     process_data3 = abc_method(
#         "process_data",
#         param = data,
#         return_type = bool,
#         log = True,
#         validate_types = True,
#         generate_docs = True,
#     )
#
#     # Varianta 2: Jako dekorátor
#     @abc_method("another_method", return_type=str)
#     def another_method(
#             self,
#             data: List[int],
#             config: Dict[str, Any],
#             optional_param: Optional[str] = None
#     ) -> str:
#         pass
#
#     @abc_method(log = True, validate_types = True, generate_docs = True)
#     def another_method(
#             self,
#             data: List[int],
#             config: Dict[str, Any],
#             optional_param: Optional[str] = None
#     ) -> str:
#         pass