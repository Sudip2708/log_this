def format_expected(expected):
    """Vrácení naformátovaných očekávaných parametrů."""

    # Pokud jsou hodnoty zadány jako tuple
    if isinstance(expected, tuple):

        # Vrácení řetězce z jmen hodnot oddělenými čárkou
        return ', '.join(t.__name__ for t in expected)

    # Vrácení jména hodnoty (pokud je zadána samostatně)
    return expected.__name__