def verify_type(value, expected_type):
    """
    Jednoduchá funkce pro ověření typu hodnoty.

    Tato funkce slouží k ověření, zda zadaná hodnota odpovídá očekávanému typu.
    Pokud ne, vyvolá výjimku TypeError.

    Params:
        value – hodnota, kterou chceme zkontrolovat.
        expected_type – očekávaný typ hodnoty, například int, str, List[int], Union[str, int], atd.

    Kroky ověření:
        isinstance(value, expected_type) - Kontroluje, zda je value instancí typu expected_type.
        hasattr(expected_type, "__origin__") - Kontroluje, zda expected_type má atribut __origin__.
            - atribut __origin__ se používá pro generické typy, například pro List[str], Dict[int, str], atd.
            - Pokud expected_type není generický typ (např. int nebo str), nebude mít tento atribut, a hasattr vrátí False.
        isinstance(value, expected_type.__origin__) -
    """

    if (
        not isinstance(value, expected_type)
        and not (
            hasattr(expected_type, "__origin__")
            and isinstance(value, expected_type.__origin__)
        )
    ):
        raise TypeError(
            f"Očekáván typ {expected_type}, obdržen {type(value)}"
        )

    return True