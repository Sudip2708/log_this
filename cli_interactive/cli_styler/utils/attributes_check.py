from typing import Set


def attributes_check(attributes_set: Set[str], styles_set: Set[str]) -> None:
    """
    Ověří, zda atributy třídy CLIStyler odpovídají dostupným stylům.

    :param attributes_set: Množina atributů definovaných ve třídě CLIStyler.
    :param styles_set: Množina klíčů stylů dostupných v `styles`.

    :raises TypeError: Pokud vstupy nejsou množiny (`set`).
    :raises ValueError: Pokud atributy neodpovídají stylům (chybějící/nadbytečné položky).
    """

    # Ověření, že vstupy jsou množiny
    if not isinstance(attributes_set, set) or not isinstance(styles_set, set):
        raise TypeError(
            "Expected both attributes_set and styles_set to be sets.")

    # Kontrola rozdílů mezi atributy a styly
    missing_in_class = styles_set - attributes_set
    missing_in_styles = attributes_set - styles_set

    # Pokud se neshodují, sestavíme chybovou zprávu
    if missing_in_class or missing_in_styles:
        error_msg = [
            "Neshoda mezi definovanými styly a atributy třídy CLIStyler:\n"]

        if missing_in_class:
            error_msg.append(
                f"❌ Chybí atributy ve třídě CLIStyler: {sorted(missing_in_class)}")

        if missing_in_styles:
            error_msg.append(
                f"❌ Nadbytečné atributy v CLIStyler: {sorted(missing_in_styles)}")

        # Vyvolání výjimky s detailní zprávou
        raise ValueError("\n".join(error_msg))
