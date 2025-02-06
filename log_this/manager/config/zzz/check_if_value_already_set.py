from typing import Union

from ..cli.styler import cli_print

def check_if_value_already_set(
        key: str,
        new_value: Union[int, str, bool],
        current_value: Union[int, str, bool]
) -> bool:
    """
    Zkontroluje, zda není zadaná již existující hodnota.
    Pokud ano, vypíše varování do konzole a vrátí True.

    Args:
        key (str): Název klíče v konfiguraci.
        new_value (Union[int, str, bool]): Nově zadaná hodnota.
        current_value (Union[int, str, bool]): Aktuální hodnota.

    Returns:
        bool: True, pokud je hodnota již nastavena, jinak False.
    """

    # Kontrola, zda se jedná o shodnou položku
    if new_value == current_value:

        # Oznam o zadání již existující položky
        cli_print(
            style="warning",
            info=f"Pro klíč '{key}' byla zadaná již nastavená hodnota: '{new_value}'.",
            detail=(
                "Konfigurační klíč již má aktuálně nastavenou hodnotu, kterou se snažíte nastavit."
            ),
            hint="Žádná změna nebyla učiněna.",
            conclusion=(
                "Pokud si přejete pokračovat ve změně, využijte interaktivní režim: ",
                "log-this-config interactive"
            )
        )

        return True

    return False
