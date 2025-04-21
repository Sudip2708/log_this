from typing import Any, Callable, Optional, Type, Union, Tuple, List, Dict
import abc
import inspect
import functools
import logging


def _extract_type_hints(func_or_type):
    """
    Extrahuje typové anotace z funkce nebo přímého vstupu.

    Podporuje:
    - Kompletní funkce
    - Tuple typových anotací
    - Jednotlivé typy
    """
    if callable(func_or_type):
        # Pokud je vstup funkce, extrahuj anotace
        return inspect.getfullargspec(func_or_type).annotations

    # Pokud je vstup tuple nebo single typ
    return func_or_type


def abc_method(
        name: Optional[str] = None,
        param: Optional[Union[Callable, Tuple, Any]] = None,
        return_type: Optional[Type] = None,
        log: bool = False,
        validate_types: bool = False,
        generate_docs: bool = False
) -> Callable:
    """
    Vysoce flexibilní implementace abstraktní metody.

    Podporuje různé způsoby definice:
    1. Jako standalone metoda
    2. Jako dekorátor
    3. S různými formami definice parametrů

    Příklady:
    # Standalone definice
    process_data = abc_method(
        "process_data",
        param=(data, config),
        return_type=bool
    )

    # Dekorátor
    @abc_method(log=True)
    def method(self, x: int) -> str:
        pass
    """

    def method_decorator(func: Optional[Callable] = None) -> Callable:
        # Extrakce jména, pokud není poskytnuto
        method_name = name or (func.__name__ if func else 'unnamed_method')

        # Extrakce typových anotací
        type_hints = {}
        if func:
            type_hints.update(inspect.getfullargspec(func).annotations)

        # Příprava finální metody
        def prepare_method(method: Callable) -> Callable:
            # Nastavení jména
            method.__name__ = method_name

            # Nastavení návratového typu
            if return_type:
                method.__annotations__['return'] = return_type

            # Volitelné dekorátory
            if generate_docs:
                method = generate_abstract_method_docs()(method)

            if log:
                method = log_abstract_method(logging.INFO)(method)

            if validate_types:
                method = validate_abstract_method_types(method)

            # Finální aplikace abstractmethod
            return abc.abstractmethod(method)

        # Logika pro různé způsoby volání
        if func is not None:
            return prepare_method(func)

        def wrapper(method: Callable) -> Callable:
            return prepare_method(method)

        return wrapper

    # Podpora pro různé vstupy
    if callable(name):
        # Pokud je první argument funkce (bez explicitního jména)
        func = name
        name = None
        return method_decorator(func)

    return method_decorator


# # Příklady použití
# class ExampleClass(abc.ABC):
#     # Varianta 1: Standalone s plnou konfigurací
#     process_data = abc_method(
#         "process_data",
#         return_type=bool,
#         log=True,
#         validate_types=True,
#         generate_docs=True
#     )
#
#     # Varianta 2: Dekorátor bez explicitního jména
#     @abc_method(log=True, validate_types=True, generate_docs=True)
#     def another_method(
#             self,
#             data: List[int],
#             config: Dict[str, Any],
#             optional_param: Optional[str] = None
#     ) -> str:
#         pass
#
#     # Varianta 3: Dekorátor s minimální konfigurací
#     @abc_method()
#     def simple_method(self, x: int) -> str:
#         pass
#
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
#         param = [
#             ("data", List[int]),
#             ("config", Dict[str, Any]),
#             ("optional_param", Optional[str])
#         ],
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