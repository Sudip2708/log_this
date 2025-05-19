"""
Interní ověřovací funkce pro duck typing validaci hodnot.

Tento modul obsahuje pomocné funkce, které se používají
v rámci méně přísné validace hodnot – tzv. duck typing přístup.

Tento balíček obsahuje pouze ty metody, u kterých je potřeba předefinovat vstupná hodnoty,
tak aby byli kmpatibilní s výstupem pro duck typing ověřovací funkci.
"""
from .has_int_attribute_verifier import has_int_attribute_verifier
from .lambda_command_attribute_verifier import lambda_command_attribute_verifier

__all__ = [
    "has_int_attribute_verifier",
    "lambda_command_attribute_verifier",
]
