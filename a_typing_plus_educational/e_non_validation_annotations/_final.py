from typing import Final, Any

from .._base_type_validator import TypeValidator


class FinalValidator(TypeValidator):
    """
    Validátor pro zápis Final[T]

    Final označuje, že hodnota proměnné se nemůže změnit po inicializaci.

    Hint:
        x: Final[int] = 1
        x = 2  # Error: Cannot assign to final name "x"
    Rozdíl:
        x: int	x je proměnná typu int. Můžeš ji přepsat.
        x: Final[int]	x je proměnná typu int, ale nesmí být přepsána po prvním přiřazení.
    Kdy použít Final?
    Používáš Final ve chvílích, kdy chceš:
        - Zabránit změně konstanty – zejména na úrovni globálních hodnot nebo konfigurací.
        - Vytvořit neděditelnou třídu: class MyClass: ... → class MyFinalClass(Final): ...
        - Zabránit přetížení metody ve třídách – v OOP to lze dělat i na úrovni metod.
        - Zvýšit čitelnost a předvídatelnost: ostatní vývojáři (nebo ty sám později) víš, že daná hodnota nemá být měněna.
    """

    # Definice klíče pro registr
    VALIDATOR_KEY = "final"
    ANNOTATION = Final[Any]
    INFO = "Definuje, že daná hodnota se po inicializaci nemůže změnit."
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        # Final není určen k validaci hodnoty samotné,
        # ale k označení, že hodnota proměnné se nemůže změnit.
        # Pro účely validace hodnoty stačí validovat vůči vnitřnímu typu.

        # Načtení vnitřních anotací
        inner_args = self._get_inner_args(annotation)

        # Validace hodnoty vůči vnitřnímu typu
        return self.validate_typing(value, inner_args, depth_check, custom_types, bool_only)