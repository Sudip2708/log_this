def format_missing(missing):
    """Vrácení naformátovaných očekávaných parametrů."""

    # Pokud jsou hodnoty zadány jako tuple
    if isinstance(missing, tuple):

        # Vrácení řetězce z jmen hodnot oddělenými čárkou
        return ', '.join(missing)

    # Vrácení jména hodnoty (pokud je zadána samostatně)
    return missing