from typing import Any, Set, Dict
from dataclasses import fields

class SerializeDunderDataclassFieldsMixin:


    def serialize_dunder_dataclass_fields(
            self,
            obj: Any,
            depth: int
    ) -> Dict[str, Any]:
        """
        Serializuje datové třídy pomocí jejich atributů definovaných jako `dataclass` pole.

        Tato metoda iteruje přes pole definovaná pomocí dekorátoru `@dataclass` v objektu a pokouší se
        o serializaci každého pole pomocí metody `serialize`. Pokud dojde k chybě při serializaci pole,
        uloží se chybová zpráva místo hodnoty pole.

        Parametry:
            obj (Any): Objekt, který musí být instancí datové třídy. Metoda předpokládá, že objekt obsahuje
                       pole definovaná jako `dataclass` atributy.
            depth (int): Aktuální hloubka rekurze. Tento parametr se používá pro řízení hloubky serializace
                         a zvyšuje se při každém vnoření.

        Návratová hodnota:
            Dict[str, Any]: Slovník, kde klíče jsou názvy polí datové třídy a hodnoty jsou serializované hodnoty
                             těchto polí. Pokud dojde k chybě při serializaci, místo hodnoty pole se uloží chybová zpráva.

        Výjimky:
            Pokud dojde k chybě při serializaci pole, zachytí se výjimka a místo hodnoty pole se uloží
            zpráva o chybě.

        Příklad použití:
            Předpokládejme následující datovou třídu:

            @dataclass
            class Example:
                name: str
                value: int

            instance = Example(name="Test", value=42)

            mixin = SerializeDunderDataclassFieldsMixin()
            serialized = mixin.serialize_dunder_dataclass_fields(instance, depth=0)
            print(serialized)

            Výstup:
            {
                "name": "Test",
                "value": 42
            }
        """

        # Definice slovníku pro výstup
        result = {}

        # Cyklus pro položky objektu
        for field in fields(obj):
            try:
                # Vytvoření klíče a hodnoty
                result[field.name] = self.serialize(getattr(obj, field.name), depth + 1)

            except Exception as e:
                result[field.name] = (
                    f"<SerializationError: "
                    f"Failed to serialize field '{field.name}': {str(e)}>"
                )

        # Kontrola zda nedošlo k chybě překročení maximální nastavené rekurze a předání výsledku
        return self._dict_error_check(result)