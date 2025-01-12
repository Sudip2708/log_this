from typing import Any, Dict

class SerializeDictMixin:

    def serialize_dict(
            self,
            obj: Any,
            depth: int
    ) -> Dict[Any, Any]:
        """
        Serializuje obsah slovníku, včetně klíčů a hodnot.

        Tato metoda iteruje přes všechny položky ve slovníku a pro každý klíč i hodnotu provádí serializaci
        pomocí metody `serialize`. Při zpracování je sledována hloubka rekurze, která slouží k omezení maximální
        hloubky serializace. Pokud dojde k výjimce během serializace, metoda vrátí zprávu o chybě.

        Parametry:
            obj (Any): Objekt, který má být serializován. Předpokládá se, že je typu `dict`, kde klíče i hodnoty
                       mohou být libovolného typu podporovaného metodou `serialize`.
            depth (int): Aktuální hloubka rekurze. Tento parametr se zvyšuje při každém vnoření, aby bylo možné
                         detekovat a omezit příliš hlubokou rekurzi.

        Návratová hodnota:
            Dict[Any, Any]: Serializovaný slovník, kde jsou všechny klíče a hodnoty zpracovány metodou `serialize`.
                            Pokud během serializace dojde k výjimce, metoda vrátí řetězec s popisem chyby ve formátu:
                            `<SerializationError: [popis chyby]>`.

        Výjimky:
            Pokud během serializace klíče nebo hodnoty dojde k výjimce, metoda tuto výjimku zachytí a místo konkrétní
            hodnoty nebo klíče uloží zprávu o chybě. Pokud je chyba obecná, například při iteraci nad slovníkem,
            vrátí metoda celý řetězec ve formátu:
                `<SerializationError: Failed to serialize dictionary item: [popis chyby]>`.

        Příklad použití:
            Předpokládejme následující slovník:

            data = {
                "key1": "value1",
                "key2": 123,
                "key3": ["a", "b", "c"]
            }

            mixin = SerializeDictMixin()
            serialized = mixin.serialize_dict(data, depth=0)
            print(serialized)

            Výstup může vypadat takto:
            {
                "key1": "value1",
                "key2": 123,
                "key3": ["a", "b", "c"]
            }

            Pokud by však například `key3` způsobil chybu během serializace, výstup může být:
            {
                "key1": "value1",
                "key2": 123,
                "key3": "<SerializationError: Failed to serialize dictionary item: [popis chyby]>"
            }
        """

        try:

            # Cyklus pro serializaci všech klíčů a hodnot
            result = {
                self.serialize(k, depth + 1): self.serialize(v, depth + 1)
                for k, v in obj.items()
            }

            # Kontrola zda nedošlo k chybě překročení maximální nastavené rekurze a předání výsledku
            return self._dict_error_check(result)

        except Exception as e:
            return (
                f"<SerializationError: "
                f"Failed to serialize dictionary item: {str(e)}>"
            )

