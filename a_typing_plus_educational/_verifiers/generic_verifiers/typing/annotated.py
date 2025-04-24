from typing import Annotated, Any

from ...._bases import BaseGenericValidator, T


class AnnotatedValidator(BaseGenericValidator):
    """
    Validátor pro typovou anotaci Annotated[T, metadata...]

    Annotated je konstrukce zavedená v PEP 593, která umožňuje asociovat libovolná
    metadata s typovou anotací. Samotný typ se používá pro validaci, zatímco metadata
    poskytují dodatečné informace a mohou být využita pro rozšířenou validaci.

    Syntaxe:
        - Annotated[T, metadata1, metadata2, ...]  # Typ T s přidanými metadaty

    Příklady použití:
        - Annotated[int, "Věk uživatele"]         # Int s dokumentací
        - Annotated[str, MinLength(5)]            # Řetězec s minimální délkou
        - Annotated[List[int], "Sudá čísla"]      # Seznam s dokumentací
        - Annotated[float, Range(0, 1)]          # Desetinné číslo s rozsahem

    Implementační detaily:
        Tento validátor extrahuje skutečný typ z Annotated konstrukce a odstraní informační
        řetězce z metadat. Zachovává však jiná metadata, která mohou být použita pro
        další validaci. Implementace je specifická pro tuto knihovnu a může se lišit od
        chování jiných validátorů.

    Validační proces:
        1. Získá vnitřní typy a metadata pomocí _get_inner_args
        2. Odfiltruje řetězcová metadata (popisky)
        3. Pokud zbývá pouze jeden typ, použije ho přímo, jinak použije tuple typů
        4. Předá validaci s upravenou anotací metodě validate_typing
        5. Hodnota je platná, pokud odpovídá základnímu typu a všem validačním metadatům

    Typy metadat:
        - Řetězce ("Popisek"): Slouží především pro dokumentaci, jsou při validaci ignorovány
        - Validační objekty (Min(5), Email()): Poskytují dodatečná validační pravidla
        - Frameworkové objekty (Field(...), Column(...)): Specifické pro určité knihovny
        - Typy a třídy (Required, Positive): Mohou určovat dodatečné vlastnosti

    Použití v kódu:
        - S vlastními validátory:
          def register(name: Annotated[str, MinLength(3), MaxLength(50)]) -> None
        - Pro dokumentaci parametrů:
          def process(value: Annotated[int, "Musí být kladné"]) -> None
        - S frameworky:
          class User:
              username: Annotated[str, Field(min_length=3)]
              age: Annotated[int, Field(gt=0)]

    Výhody použití Annotated:
        - Odděluje typ od validačních a jiných metadat
        - Umožňuje přidávat dokumentaci přímo k typům
        - Podporuje komplexní validační pravidla
        - Je rozšiřitelný pro různé frameworky a knihovny

    Běžné vzory použití:
        - Dokumentace parametrů přímo v typu
        - Validační pravidla v typu namísto odděleného validátoru
        - Metadata pro generování API dokumentace
        - Informace pro ORM a frameworky

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Annotated
        - https://peps.python.org/pep-0593/ (Static Semantics for Annotated)
        - https://mypy.readthedocs.io/en/stable/python36.html#annotated
    """

    VALIDATOR_KEY = "annotated"
    ANNOTATION = Annotated[T, Any]
    INFO = "Definuje upřesňující parametry pro validaci"
    ORIGIN = Annotated

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

        # Získání tuple s vnitřními typy
        inner_args = self._get_inner_args(annotation)

        # Odstranění všech řetězcových metadat (informačních popisků)
        filtered_args = tuple(arg for arg in inner_args if not isinstance(arg, str))

        # Pokud zůstala jen jedna položka, předáváme ji přímo,
        # jinak předáváme celý tuple všech ověřitelných prvků
        prepared_annotation = filtered_args[0] if len(filtered_args) == 1 else filtered_args

        # Předání dál do obecné validace
        return self.validate_typing(value, prepared_annotation, depth_check, custom_types, bool_only)