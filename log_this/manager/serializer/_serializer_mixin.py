from typing import Any
from collections import namedtuple  # Pro ověření _asdict

from .mixin_data import (
    DictErrorCheckMixin,
    SerializeDunderDictMixin,
    SerializeDunderDataclassFieldsMixin,
    SerializeListTupleSetMixin,
    SerializeDictMixin,
)


class SerializerMixin(
    DictErrorCheckMixin,
    SerializeDunderDictMixin,
    SerializeDunderDataclassFieldsMixin,
    SerializeListTupleSetMixin,
    SerializeDictMixin,
):
    """
    Třída sdružující všechny mixiny pro třídu SafeSerializer.

    Mixins:
        DictErrorCheckMixin: Kontroluje zda slovník neobsahuje zanořený slovník s oznamem o rekurzivní chybě.
        SerializeDunderDataclassFieldsMixin: Serializuje objekty s __dict__ atributem.
        SerializeListTupleSetMixin: Serializuje seznamy, tuple a množiny.
        SerializeDictMixin: Serializuje slovníky.
        SerializeMethodMixin: Serializuje dataclass objekty.

    Methods:
        serialize: Hlavní metoda zpracovávající seralizaci.
        _dict_error_check: Kontrola slovníku na oznam o rekurzivní chybě.
        serialize_dunder_dataclass_fields: Serializace objektů s __dataclass_fields__
        serialize_list_tuple_set: Serializace seznamů, tuple a množin.
        serialize_dict: Serializace slovníků.
        serialize_dunder_dict: Serializace objektů s __dict__
    """


    def serialize(
            self,
            obj: Any,
            depth: int = 0
    ) -> Any:
        """
        Serializuje objekt s omezením hloubky rekurze a detekcí cyklických referencí.

        Tato metoda podporuje serializaci různých typů Python objektů, včetně základních typů, namedtuple,
        dataclass, seznamů, n-tic, množin a slovníků. Sleduje hloubku rekurze a detekuje cyklické reference,
        aby se předešlo nekonečným smyčkám nebo přetížení.

        Parametry:
            obj (Any): Objekt, který má být serializován. Tento parametr může obsahovat základní Python typy
                       (int, float, str, bool, None), iterovatelné struktury (list, tuple, set, dict), nebo
                       složitější typy jako namedtuple a dataclass.
            depth (int, volitelný): Aktuální hloubka rekurze. Tento parametr je využíván k monitorování
                                    a omezení hloubky zpracování. Výchozí hodnota je 0.

        Návratová hodnota:
            Any: Serializovaný objekt nebo řetězec s chybovou zprávou:
                 - Úspěšná serializace vrací převedený objekt, například slovník, seznam nebo jiný podporovaný formát.
                 - Pokud dojde k chybě (např. překročení maximální hloubky nebo cyklická reference), metoda vrací
                   chybovou zprávu ve formátu:
                   `<SerializationError: [popis chyby]>`.

        Výjimky:
            - Pokud je dosaženo maximální hloubky rekurze, metoda vrátí:
              `<SerializationError: Maximum serialization depth exceeded>`.
            - Pokud je detekována cyklická reference (stejný objekt v rámci rekurze), metoda vrátí:
              `<SerializationError: Cyclic reference detected>`.
            - Při jiné chybě během serializace vrací obecnou zprávu obsahující popis chyby.

        Příklad použití:
            Předpokládejme objekt `my_object` obsahující složité struktury:

            from dataclasses import dataclass

            @dataclass
            class Example:
                name: str
                values: list

            my_object = Example(name="Test", values=[1, 2, 3])

            serializer = SafeSerializer()
            serialized = serializer(my_object)
            print(serialized)

            Očekávaný výstup:
            {
                "name": "Test",
                "values": [1, 2, 3]
            }

            Pokud by `values` obsahovaly cyklickou referenci, např. `values = [my_object]`, výstup by mohl být:
            {
                "name": "Test",
                "values": "<SerializationError: Cyclic reference detected>"
            }

        Poznámky:
            - Metoda je navržena pro použití v kombinaci s dalšími metodami, jako je `serialize_dict`,
              `serialize_list_tuple_set` nebo `serialize_dunder_dataclass_fields`.
            - Hodnotu hloubky pro kontrolu maximální rekurze je možné měnit.
            - Základní typy (int, float, str, bool, None) jsou vráceny přímo bez dalších úprav.
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
                if hasattr(obj, '__dict__') and obj.__dict__:
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
