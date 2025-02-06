from prompt_toolkit.shortcuts import radiolist_dialog
from typing import Optional

from log_this.manager.config.keys_data import KEYS_DATA
from log_this.manager.config.styler import dialog_style
from ..exceptions import ExitInteractiveMode

def config_key_picker() -> Optional[str]:
    """
    Zobrazí menu pro výběr konfiguračního klíče.

    Returns:
        Optional[str]: Vybraný klíč nebo None při zrušení
    """

    # Načtení klíčů a info textu pro podrobnosti k výběru
    values = [
        (key, f"{key} - {KEYS_DATA[key].info}")
        for key in KEYS_DATA
    ]

    # Přidání položky pro opuštění konfigurace
    values.append(
        ('exit', 'Ukončit interaktivní režim')
    )

    # Vytvoření pickeru
    result = radiolist_dialog(
        title='Výběr konfiguračního klíče',
        text='(Pohybujte se šipkami a volbu potvrďte entrem.)',
        values=values,
        style=dialog_style
    ).run()

    # Kontrola zda nebylo vybrané ukončení interaktivního modu
    if result == 'exit':
        raise ExitInteractiveMode("Opouštím proces změny konfigurace.")

    # Kontrola zda nebyla zmáčknutá klávesnice pro přerušení zadávání
    if result is None:
        raise KeyboardInterrupt

    return result