def reduce_depth_check(depth_check):
    """
    Pomocná interní funkce pro řízení hloubky rekurzivní validace vnitřních struktur.

    Používá se ve funkcích `iterable_validator` a `dictionary_validator`, kde umožňuje postupné
    snižování hodnoty zanoření (`depth_check`) při rekurzivním procházení vnořených položek (např. seznamů,
    slovníků, zanořených struktur atd.).

    Pokud je `depth_check` zadán jako celé číslo (např. 3), funkce jej sníží o 1 při každém volání,
    čímž efektivně omezuje hloubku kontroly. Pokud je hodnota již 0 nebo záporná, zůstává 0.
    Pokud je `depth_check` typu `bool`, hodnota se nezmění a je vrácena beze změny.

    Args:
        depth_check (Union[bool, int]): Aktuální stav řízení hloubky validace – buď logická hodnota,
            nebo celé číslo vyjadřující počet zbývajících kroků rekurze.

    Returns:
        Union[bool, int]: Upravená hodnota `depth_check` se sníženou hloubkou (pokud je typu `int`).
    """

    # Kontrola zda je hodnota depth_check zapsaná jako číslo
    if isinstance(depth_check, int):

        # Snížení číselné hodnoty
        depth_check = depth_check - 1 if depth_check >= 0 else 0

    # Navrácení stejné, nebo upravené hodnoty
    return depth_check