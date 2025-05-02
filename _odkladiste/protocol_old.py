"""
protocol.py
Typová anotace nebo pomocná metoda?
Tento soubor definuje Protocol, což je základ pro tvorbu protokolů, které definují očekávané metody nebo chování pro třídy, které implementují tento protokol.

Použití v typových anotacích?
Ano, Protocol se používá v typových anotacích pro definování protokolů, které musí být implementovány v třídách.
"""
from typing import Protocol, get_type_hints, Any
import inspect
from typing import Protocol

from ...._bases import BaseIsInstanceValidator


class ProtocolValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci Protocol

    """

    VALIDATOR_KEY = "protocol"
    ANNOTATION = Protocol[T]
    INFO = "Definuje typ pro protokol, což je abstraktní základ pro definici chování, který mohou implementovat jiné třídy"
    ORIGIN = Protocol


    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání informací o protokolu - metody a atributy
        protocol_attrs = {}

        # Pokud má protokol __annotations__, získáme typy atributů
        if hasattr(annotation, "__annotations__"):
            protocol_attrs.update(annotation.__annotations__)

        # Získání metod protokolu
        for name, member in inspect.getmembers(annotation):
            if name.startswith(
                    "_") and name != "__call__":  # Přeskočení interních metod kromě __call__
                continue
            if inspect.isfunction(member):
                protocol_attrs[name] = member

        # Kontrola, zda objekt implementuje všechny požadované atributy a metody
        for name, expected_type in protocol_attrs.items():
            if not hasattr(value, name):
                if bool_only:
                    return False
                raise AttributeError(
                    f"Objekt nemá požadovaný atribut nebo metodu '{name}'")

            # Pokud se jedná o metodu, kontrolujeme pouze existenci
            if inspect.isfunction(expected_type):
                if not callable(getattr(value, name)):
                    if bool_only:
                        return False
                    raise TypeError(f"Atribut '{name}' by měl být volatelný")

            # Pro atributy kontrolujeme typ, pokud je vyžadována hloubková kontrola
            elif depth_check:
                attr_value = getattr(value, name)
                new_depth_check = self._reduce_depth_check(depth_check)
                self.validate_typing(attr_value, expected_type, new_depth_check,
                                     custom_types, bool_only)

        return True