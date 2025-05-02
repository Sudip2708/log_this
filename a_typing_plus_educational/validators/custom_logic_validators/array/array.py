from array import array

from ...._bases import BaseCustomLogicValidator
from ...._verifiers import array_verifier


class ArrayValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci array.array

    Array reprezentuje efektivní homogenní pole primitivních hodnot stejného typu.
    Oproti seznamům (List) jsou pole array úspornější na paměť a rychlejší pro
    operace s velkým množstvím číselných dat stejného typu.

    Syntaxe:
        - array             # Obecná reference na typ array.array
        - array.array       # Plně kvalifikovaný zápis
        - Annotated[array, 'i']  # S typovým kódem (experimentální)

    Formát typových kódů:
        Array vyžaduje při vytváření typový kód, který určuje typ dat v poli:
        - 'b', 'B' - signed/unsigned char (1 byte)
        - 'h', 'H' - signed/unsigned short (2 bytes)
        - 'i', 'I' - signed/unsigned int (obvykle 4 bytes)
        - 'l', 'L' - signed/unsigned long (obvykle 4 bytes)
        - 'q', 'Q' - signed/unsigned long long (obvykle 8 bytes)
        - 'f', 'd' - float (4 bytes), double (8 bytes)
        a další dle implementace Pythonu.

    Příklady použití:
        - array.array('i')        # Pole celočíselných hodnot typu int
        - array.array('d')        # Pole hodnot s plovoucí desetinnou čárkou
        - array.array('u', 'abc') # Pole znaků Unicode
        - Annotated[array, 'i']   # Pro typovou kontrolu s konkrétním typovým kódem

    Validační proces:
        1. Validátor ověří, zda hodnota je instance typu array.array.
        2. Pokud je použita anotace Annotated[array, 'typecode'], validuje se i typový kód.
           Například: Annotated[array, 'i'] očekává array s typovým kódem 'i' (pole intů).

    Použití v kódu:
        - Jako parametr funkce: def process_data(data: array) -> None
        - S kontrolou typového kódu:
          IntArray = Annotated[array, 'i']
          def process_ints(data: IntArray) -> None: ...

    Výhody oproti seznamu:
        - Nižší paměťová náročnost díky homogenním typům
        - Vyšší výkon při operacích s velkým množstvím číselných dat
        - Přímá konverze na/z buffer protokolu (bytes, bytearray)

    Omezení:
        - Může obsahovat pouze primitivní typy (čísla, znaky)
        - Všechny prvky musí být stejného typu
        - Nelze ukládat složitější struktury (objekty, kolekce)

    Kdy použít:
        - Pro efektivní práci s velkým množstvím číselných dat
        - Při komunikaci s nízkoúrovňovými API a knihovnami (C, systémová volání)
        - Pro binární operace a FFI (Foreign Function Interface)

    Běžné chyby:
        - Zapomenutí importu: from array import array
        - Použití neplatného typového kódu
        - Pokus o uložení hodnot špatného typu do pole
        - Záměna s numpy.array, který má jiné vlastnosti a možnosti

    Reference:
        - https://docs.python.org/3/library/array.html
    """

    VALIDATOR_KEY = "array"
    ANNOTATION = array

    IS_INSTANCE = array
    HAS_ATTRS = "append", "extend", "insert", "__getitem__", "__setitem__", "__delitem__", "__len__"
    CALLABLE_ATTRS = HAS_ATTRS

    DESCRIPTION = "Pole s typem prvků"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí array.array. "
            "Jedná se o sekvenci číselných hodnot pevného typu (např. 'i' pro int), "
            "vhodnou pro efektivní uložení."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření array."""

        return array_verifier(
            value, self.ORIGIN, annotation, depth_check, bool_only
        )