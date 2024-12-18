class SerializationDepthError(Exception):
    pass


def safe_serialize(obj, seen=None, max_depth=5):
    """
    Bezpečná serializace objektů pro logging.

    Args:
        obj: Objekt k serializaci
        seen: Sada zpracovaných objektů
        max_depth: Maximální hloubka serializace

    Returns:
        Serializovaný objekt nebo chybovou zprávu
    """
    # Detekce rekurzivních struktur
    if seen is None:
        seen = set()

    # Detekce rekurze pomocí ID
    if id(obj) in seen:
        return "<SerializationError: Cyclic reference detected>"

    # Přidání aktuálního objektu do `seen`
    seen.add(id(obj))

    try:
        # Kontrola maximální hloubky
        if len(seen) > max_depth:
            print("### len(seen): ", len(seen))
            raise SerializationDepthError(
                f"Maximum serialization depth of {max_depth} exceeded"
            )


        # Objekty s __dict__
        if hasattr(obj, '__dict__'):
            serialized = {
                k: safe_serialize(v, seen.copy())
                for k, v in obj.__dict__.items()
                if not callable(v) and not k.startswith('_')
            }
            # Pokud je slovník prázdný, použij repr
            return serialized if serialized else repr(obj)

        # Speciální typy (dataclass, namedtuple)
        if hasattr(obj, '_asdict'):  # namedtuple
            return safe_serialize(obj._asdict(), seen.copy())

        if hasattr(obj, '__dataclass_fields__'):  # dataclass
            return {
                k: safe_serialize(getattr(obj, k), seen.copy())
                for k in obj.__dataclass_fields__
                if not k.startswith('_')
            }

        # Iterovatelné struktury
        if isinstance(obj, (list, tuple, set)):
            return [safe_serialize(item, seen.copy()) for item in obj]

        # Slovníky
        if isinstance(obj, dict):
            return {k: safe_serialize(v, seen.copy()) for k, v in obj.items()}

        # Základní typy
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj

        # Poslední záchrana
        return str(obj)

    except SerializationDepthError as e:
        print("### except SerializationDepthError as e:: ")
        return f"<SerializationError: {str(e)}>"

    except Exception as e:
        print("### except Exception as e:: ")
        return f"<SerializationError: {str(e)}>"

    finally:
        print("### finally: ")
        # Vyčištění aktuálního objektu ze seznamu seen
        seen.remove(id(obj))
