# log_this/modes/utils/_safe_serialize.py

from typing import Any
from .serializer_mixin import SerializerMixin


class SafeSerializer(SerializerMixin):
    """
    Bezpečný serializátor pro objekty, který kontroluje hloubku a cyklické reference.

    Třída SafeSerializer umožňuje serializovat různé typy objektů s kontrolou rekurze
    a ochrany před cyklickými referencemi. Implementuje singleton vzor, takže existuje
    pouze jedna instance této třídy.

    Mixiny:
        SerializerMixin: Obsahuje základní metody a logiku potřebnou pro serializaci objektů.

    Atributy:
        _instance (SafeSerializer): Singleton instance třídy SafeSerializer.
        max_depth (int): Maximální povolená hloubka serializace, aby nedošlo k přetečení zásobníku.
        seen (set): Množina identifikátorů objektů, které již byly zpracovány, aby se předešlo cyklickým referencím.

    Použití:
        SafeSerializer se používá ke serializaci různých datových struktur a uživatelských objektů,
        přičemž zachovává bezpečnost a ochranu před přetížením systému rekurzí nebo nekonečnými cykly.

    Příklad:
        ```python
        serializer = SafeSerializer()

        # Serializace jednoduchého objektu
        data = {"key": "value"}
        serialized = serializer(data)  # Výstup: '{"key": "value"}'

        # Serializace objektu s omezením hloubky
        serializer.max_depth = 5
        deep_data = {"a": {"b": {"c": {"d": {"e": "value"}}}}}
        serialized_deep = serializer(deep_data)  # Výstup: Např. '{"a": {"b": {"c": {"d": {...}}}}}'
        ```
    """


    # Atribut pro singleton instanci třídy:
    _instance = None


    # Vytvoření instance:
    def __new__(cls, *args, **kwargs):
        """
        Implementace singleton vzoru pro SafeSerializer.

        Metoda zajistí, že bude vytvořena pouze jedna instance třídy SafeSerializer.
        Pokud instance již existuje, vrátí ji, jinak vytvoří novou instanci.

        Args:
            *args: Nepovinné poziční argumenty (pro budoucí rozšíření).
            **kwargs: Nepovinné pojmenované argumenty (pro budoucí rozšíření).

        Returns:
            SafeSerializer: Singleton instance této třídy.

        Příklad:
            ```python
            serializer1 = SafeSerializer()
            serializer2 = SafeSerializer()
            assert serializer1 is serializer2  # Obě proměnné odkazují na stejnou instanci
            ```
        """

        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    # Základní inicializace instance
    def __init__(self):
        """
        Inicializuje instanci SafeSerializer.

        Tato metoda inicializuje atributy třídy při prvním vytvoření instance.
        Pokud instance již byla inicializována, metoda tuto operaci přeskočí.

        Atributy:
            max_depth (int): Nastavuje maximální povolenou hloubku serializace.
                             Výchozí hodnota je 100.
            seen (set): Množina pro sledování ID objektů, které byly zpracovány,
                        aby se předešlo cyklickým referencím.

        Poznámky:
            - Metoda je navržena tak, aby byla idempotentní, tj. opakované volání
              nebude měnit stav instance.

        Příklad:
            ```python
            serializer = SafeSerializer()
            print(serializer.max_depth)  # Výstup: 100
            print(serializer.seen)       # Výstup: set()
            ```
        """

        if not hasattr(self, '_initialized'):
            self.max_depth = 100
            self.seen = set()
            self._initialized = True


    # Nastavení metody pro přímé volání funkce
    def __call__(self, obj: Any, max_depth: int = None) -> Any:
        """
        Umožňuje použít instanci SafeSerializer jako funkci.

        Metoda slouží k přímému volání metody `serialize`, která provádí serializaci
        zadaného objektu. Tato metoda umožňuje použít instanci třídy SafeSerializer
        přímo jako funkci, což zjednodušuje její použití.

        Args:
            obj (Any): Objekt k serializaci. Podporované typy zahrnují:
                - Základní datové typy (např. int, float, str, bool)
                - Složité struktury (např. list, tuple, dict, set)
                - Uživatelské objekty s atributy, které jsou serializovatelné.

        Returns:
            Any: Serializovaný výstup. Formát výstupu závisí na konkrétní implementaci
            metody `serialize`.

        Raises:
            ValueError: Pokud objekt nelze serializovat (např. kvůli cyklickým referencím
            nebo překročení maximální hloubky).
            TypeError: Pokud je zadaný objekt nepodporovaného typu.

        Examples:
            ```python
            serializer = SafeSerializer(max_depth=10)

            # Serializace základního typu
            serialized = serializer(123)  # Výstup: 123

            # Serializace seznamu
            serialized_list = serializer([1, 2, 3])  # Výstup: "[1, 2, 3]"

            # Serializace vlastního objektu
            class Example:
                def __init__(self):
                    self.value = 42

            obj = Example()
            serialized_obj = serializer(obj)  # Výstup: např. '{"value": 42}'
            ```
        """

        return self.serialize(obj, max_depth)


serializer = SafeSerializer()