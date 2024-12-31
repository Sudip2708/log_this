from typing import Any, List

class SerializeListTupleSetMixin:

    def serialize_list_tuple_set(
            self,
            obj: Any,
            depth: int
    ) -> List[Any]:
        """
        Serializuje slovník včetně všech klíčů a hodnot pomocí rekurzivního procesu.

        Tato metoda iteruje přes všechny položky slovníku a pro každý klíč i hodnotu volá metodu `serialize`.
        Rekurzivní zpracování umožňuje serializaci vnořených struktur, přičemž je sledována hloubka rekurze
        pomocí parametru `depth`. Pokud hloubka překročí povolený limit, může být serializace přerušena
        nebo ošetřena chybovou zprávou.

        Parametry:
            obj (Any): Objekt, který má být serializován. Očekává se slovník (`dict`), kde klíče a hodnoty
                       mohou být jakéhokoliv typu podporovaného metodou `serialize`.
            depth (int): Aktuální hloubka rekurze. Tento parametr se při každém vnoření zvyšuje a slouží
                         k monitorování a řízení hloubky serializace.

        Návratová hodnota:
            Dict[Any, Any]: Serializovaný slovník, kde klíče a hodnoty byly zpracovány metodou `serialize`.
                            Pokud během serializace nastane chyba, metoda vrátí chybovou zprávu ve formátu:
                            `<SerializationError: [popis chyby]>`.

        Chybové scénáře:
            - Pokud dojde k výjimce během serializace konkrétního klíče nebo hodnoty, metoda tuto chybu
              zachytí a výstupem může být náhradní hodnota reprezentující chybu.
            - Pokud nelze iterovat přes vstupní objekt (například kvůli špatnému typu), vrátí metoda obecnou
              chybovou zprávu, například:
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

            Očekávaný výstup:
            {
                "key1": "value1",
                "key2": 123,
                "key3": ["a", "b", "c"]
            }

            Pokud by však `key3` způsobil chybu během serializace (například kvůli nepodporovanému typu),
            výstup může být:
            {
                "key1": "value1",
                "key2": 123,
                "key3": "<SerializationError: Failed to serialize dictionary item: [popis chyby]>"
            }

        Poznámky:
            - Metoda očekává, že její implementace je rozšířena o specifickou logiku v metodě `serialize`.
            - Hloubku rekurze je vhodné nastavovat na základě složitosti a velikosti vstupního slovníku.
        """

        try:
            # Načtení rekurzivního volání
            result = [self.serialize(item, depth + 1) for item in obj]

            # Kontrola přítomnosti rekurzního erroru
            if (
                    len(result) == 1
                    and isinstance(result[0], str)
                    and result[0].startswith('<SerializationError')
            ):
                # Vrácení pouze erroru
                result = result[0]

            # Navrácení hodnoty
            return result


        except Exception as e:
            return f"<SerializationError: Failed to serialize iterable item: {str(e)}>"

