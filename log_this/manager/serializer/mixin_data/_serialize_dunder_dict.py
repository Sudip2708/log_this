from typing import Any, Set, Dict


class SerializeDunderDictMixin:

    def serialize_dunder_dict(
            self,
            obj: Any,
            depth: int
    ) -> Dict[str, Any]:
        """
        Serializuje objekty s atributem `__dict__`.

        Tato metoda iteruje přes atributy objektu, které jsou dostupné v jeho `__dict__` slovníku. Pro každý atribut
        se pokouší o serializaci pomocí metody `serialize`, s přihlédnutím k aktuální hloubce rekurze. Pokud dojde
        k výjimce při serializaci konkrétního atributu, místo hodnoty se uloží chybová zpráva.

        Parametry:
            obj (Any): Objekt, jehož atributy budou serializovány. Tento objekt musí mít atribut `__dict__`,
                       což je typické pro instance běžných tříd v Pythonu.
            depth (int): Aktuální hloubka rekurze. Používá se pro řízení hloubky serializace a přidává se při každém
                         vnoření.

        Návratová hodnota:
            Dict[str, Any]: Slovník, kde klíče odpovídají názvům atributů objektu a hodnoty představují serializované
                             hodnoty těchto atributů. Pokud dojde k chybě při serializaci, místo hodnoty se uloží
                             zpráva o chybě.

        Výjimky:
            Pokud při pokusu o serializaci atributu dojde k výjimce, metoda zachytí tuto výjimku a uloží
            místo hodnoty atributu chybovou zprávu ve formátu:
                "<SerializationError: Failed to serialize attribute '{name}': {error_message}>"

        Příklad použití:
            Předpokládejme následující třídu:

            class Example:
                def __init__(self, name, value):
                    self.name = name
                    self.value = value

            instance = Example(name="Test", value=42)

            mixin = SerializeDunderDictMixin()
            serialized = mixin.serialize_dunder_dict(instance, depth=0)
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
        for k, v in obj.__dict__.items():
            try:
                # Kontrola proveditelnosti serializace
                if not callable(v) and not k.startswith('_'):
                    # Vytvoření klíče a hodnoty
                    result[k] = self.serialize(v, depth + 1)

            except Exception as e:
                result[k] = (
                    f"<SerializationError: "
                    f"Failed to serialize attribute '{k}': {str(e)}>"
                )

        # Kontrola zda nedošlo k chybě překročení maximální nastavené rekurze a předání výsledku
        return self._dict_error_check(result)