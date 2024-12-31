from typing import Any
from collections import namedtuple

class SerializeMethodMixin:

    def serialize(
            self,
            obj: Any,
            depth: int = 0
    ) -> Any:
        """
        Serializuje objekt s omezením hloubky a detekcí cyklických referencí.

        Tato metoda se snaží serializovat objekty různých typů, včetně standardních Python objektů,
        namedtuple, dataclass, seznamů, n-tic, množin a slovníků. Kontroluje rekurzivní hloubku
        a cyklické reference, a pokud jsou detekovány, vrací chybovou zprávu.

        Parametry:
            obj (Any): Objekt, který má být serializován. Tento parametr může obsahovat jakýkoliv objekt
                       podporující serializaci, včetně slovníků, seznamů, dataclass objektů, atd.
            depth (int, volitelný): Aktuální hloubka rekurze, která je automaticky nastavena na 0.
                                    Tento parametr je využíván pro kontrolu maximální hloubky rekurze.

        Return:
            Any: Serializovaný objekt nebo chybová zpráva. Pokud je objekt úspěšně serializován, metoda vrací
                 jeho serializovanou verzi (např. slovník, seznam, hodnotu). Pokud dojde k chybě během serializace,
                 vrací chybovou zprávu ve formátu řetězce.

        Výjimky:
            Pokud je dosaženo maximální hloubky rekurze nebo je detekována cyklická reference, metoda vrací
            příslušnou chybovou zprávu. V opačném případě je návratová hodnota serializovaným objektem.

        Příklad použití:
            serialize(my_object)
        """

        try:

            # Kontrola maximální hloubky rekurze
            if depth >= self.max_depth:
                return "<SerializationError: Maximum serialization depth exceeded>"

            # Kontrola přímé rekurze (objekty mají shodné ID)
            if id(obj) in self.seen:
                return "<SerializationError: Cyclic reference detected>"

            # Přidání ID objektu do `seen`
            self.seen.add(id(obj))

            try:
                # Objekty s __dict__
                if hasattr(obj, '__dict__'):
                    return self.serialize_dunder_dict(obj, depth)

                # Speciální typ namedtuple
                if hasattr(obj, '_asdict'):
                    return self.serialize(obj._asdict(), depth + 1)

                # Speciální typ dataclass
                if hasattr(obj, '__dataclass_fields__'):
                    return self.serialize_dunder_dataclass_fields(obj, depth)

                # Iterovatelné struktury
                if isinstance(obj, (list, tuple, set)):
                    return self.serialize_list_tuple_set(obj, depth)

                # Slovníky
                if isinstance(obj, dict):
                    return self.serialize_dict(obj, depth)

                # Základní typy
                if isinstance(obj, (int, float, str, bool, type(None))):
                    return obj

                # Poslední záchrana
                return str(obj)


            except Exception as e:
                return f"<SerializationError: {str(e)}>"

            finally:
                if id(obj) in self.seen:
                    self.seen.remove(id(obj))

        except Exception as e:
            return f"<SerializationError: {str(e)}>"