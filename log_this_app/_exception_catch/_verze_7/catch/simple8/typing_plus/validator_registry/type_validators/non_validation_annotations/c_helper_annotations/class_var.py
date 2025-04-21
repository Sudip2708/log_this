from typing import ClassVar

from .._base_type_validator import TypeValidator


class ClassVarValidator(TypeValidator):
    """
    Validátor pro zápis ClassVar[T]

    ClassVar označuje třídní proměnné, které by neměly být použity jako atributy instance.

    Hint:
        class C:
            class_var: ClassVar[int] = 0  # Třídní proměnná
            instance_var: int = 0         # Instanční proměnná

    ClassVar[T] je typová anotace, která říká:
        "Tato proměnná je určena pouze pro třídu (class-level), nikoli pro instance."

    Shrnutí pro validátor
    Tvůj ClassVarValidator:
        Správně validuje hodnotu podle vnitřního typu.
        Nepokouší se analyzovat, zda se proměnná používá na úrovni třídy nebo instance – a to je správně, protože to se kontroluje staticky, ne za běhu.
    Tj. validátor má správnou odpovědnost: ověřit, že hodnota odpovídá typu, ale nepokoušet se zjišťovat kontext použití.
    """

    # Definice klíče pro registr
    VALIDATOR_TYPE = ClassVar

    def validate(self, value, annotation, depth_check, custom_types, bool_only):
        # ClassVar není určen k validaci hodnoty samotné,
        # ale k označení, že proměnná má být třídní, nikoli instanční.
        # Pro účely validace hodnoty stačí validovat vůči vnitřnímu typu.

        # Načtení vnitřních anotací
        inner_args = self._get_inner_args(annotation)

        # Validace hodnoty vůči vnitřnímu typu
        return self.validate_typing(value, inner_args, depth_check,
                                    custom_types, bool_only)