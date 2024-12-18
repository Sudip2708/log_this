Definice funkce:

    def safe_serialize(obj):
    
Pro objekty vrátí jejich slovníkovou reprezentaci:

        if hasattr(obj, '__dict__'):
            return {k: safe_serialize(v) for k, v in obj.__dict__.items()
                    if not callable(v) and not k.startswith('_')}
    
Pro iterovatelné objekty rekurzivní serializace:

        elif isinstance(obj, (list, tuple, set)):
            return [safe_serialize(item) for item in obj]
    
Pro slovníky rekurzivní serializace hodnot:

        elif isinstance(obj, dict):
            return {k: safe_serialize(v) for k, v in obj.items()}
    
Základní typy lze serializovat přímo:

        elif isinstance(obj, (int, float, str, bool, type(None))):
            return obj
    
Pro ostatní typy vrátí string reprezentaci:

        else:
            return str(obj)
