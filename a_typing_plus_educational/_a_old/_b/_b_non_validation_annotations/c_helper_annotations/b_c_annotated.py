from typing import Annotated

from .._base_type_validator import TypeValidator


class AnnotatedValidator(TypeValidator):
    """
    Validátor pro zápis Annotated[int, "Popis"]

    Po obdržení hodnot zjistí, zda v obsahu jsou uvedené i informační řetězce.
    Pokud ano, odstraní je.
    Pokud po úpravě zbyde jen jeden prvek, pak je předáván samostatně.
    Pokud zbyde více prvků, jsou předávány jako tuple,
    kde hodnota musí splnit všechny podmínky.

    Hint:
        Annotated[int, "Popis"] = Typ s dodatečnou informací
        Annotated může mít jako metadata:
            - řetězce: "Popis"
            - objekty: Form(...), Field(...), Widget(...)
            - instance tříd: MinLength(3), UppercaseOnly()
            - nebo i celé třídy: Positive, Required
    """

    VALIDATOR_KEY = "annotated"
    ANNOTATION = Annotated[int, "Popis"]
    INFO = "Definuje upřesňující parametry pro validaci"
    GET_ORIGIN = Annotated  # typing.Annotated

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typy
        inner_args = self._get_inner_args(annotation)

        # Odstranění všech řetězcových metadat (informačních popisků)
        filtered_args = tuple(arg for arg in inner_args if not isinstance(arg, str))

        # Pokud zůstala jen jedna položka, předáváme ji přímo
        # Jinak předáváme celý tuple všech ověřitelných prvků
        prepared_annotation = filtered_args[0] if len(filtered_args) == 1 else filtered_args

        # Předání dál do obecné validace
        return self.validate_typing(value, prepared_annotation, depth_check, custom_types, bool_only)
