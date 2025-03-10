from log_this_old.config import get_config

def safe_serialize(obj, seen=None, depth=0,):
    """
    Bezpečná serializace objektů pro logging s kontrolou času.

    Args:
        obj: Objekt k serializaci
        seen: Sada zpracovaných objektů
        depth: Aktuální hloubka rekurze
        time_limit: Maximální povolený čas (v sekundách)

    Returns:
        Serializovaný objekt nebo chybovou zprávu
    """

    try:
        # Kontrola maximální hloubky
        max_depth = get_config().max_depth
        if depth >= max_depth:
            return f"<SerializationError: Maximum serialization depth of {max_depth} exceeded>"

        # Detekce rekurzivních struktur
        if seen is None:
            seen = set()

        if id(obj) in seen:
            return "<SerializationError: Cyclic reference detected>"

        # Přidání aktuálního objektu do `seen`
        seen.add(id(obj))

        try:
            # Objekty s __dict__
            if hasattr(obj, '__dict__'):
                result = {}
                for k, v in obj.__dict__.items():
                    if not callable(v) and not k.startswith('_'):
                        serialized_value = safe_serialize(v, seen, depth + 1)
                        if (isinstance(serialized_value, str)
                                and "SerializationError" in serialized_value):
                            return serialized_value
                        result[k] = serialized_value
                return result

            # Speciální typy (dataclass, namedtuple)
            if hasattr(obj, '_asdict'):  # namedtuple
                serialized = safe_serialize(obj._asdict(), seen, depth + 1)
                if (isinstance(serialized, str)
                        and "SerializationError" in serialized):
                    return serialized
                return serialized

            if hasattr(obj, '__dataclass_fields__'):  # dataclass
                result = {}
                for k in obj.__dataclass_fields__:
                    serialized_value = safe_serialize(getattr(obj, k), seen, depth + 1)
                    if (isinstance(serialized_value, str)
                            and "SerializationError" in serialized_value):
                        return serialized_value
                    result[k] = serialized_value
                return result

            # Iterovatelné struktury
            if isinstance(obj, (list, tuple, set)):
                result = []
                for item in obj:
                    serialized_value = safe_serialize(item, seen, depth + 1)
                    if (isinstance(serialized_value, str)
                            and "SerializationError" in serialized_value):
                        return serialized_value
                    result.append(serialized_value)
                return result

            # Slovníky
            if isinstance(obj, dict):
                result = {}
                for k, v in obj.items():
                    serialized_value = safe_serialize(v, seen, depth + 1)
                    if (isinstance(serialized_value, str)
                            and "SerializationError" in serialized_value):
                        return serialized_value
                    result[k] = serialized_value
                return result

            # Základní typy
            if isinstance(obj, (int, float, str, bool, type(None))):
                return obj

            # Poslední záchrana
            return str(obj)

        except Exception as e:
            return f"<SerializationError: {str(e)}>"

        finally:
            seen.remove(id(obj))

    except Exception as e:
        return f"<SerializationError: {str(e)}>"