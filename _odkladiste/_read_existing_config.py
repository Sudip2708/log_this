"""
Závislosti:
- _config_path: Atribut definující cestu ke konfiguračnímu souboru
- _load_and_validate_config: Metoda pro načtení a validaci konfiguračního souboru
- valid_keys: Property vracející všechny klíče slovníku keys_data
- _merge_with_defaults: Metoda pro odstranění nadbytečných klíčů a doplnění chybějících
- _create_config_file: Boolena atribut pro nastavení oprávnění k vytvoření nového konfiguračního souboru (bez tohoto atributu s hodnotu True vytvoření nového souboru neprojde)
- cli_log: Konfigurační loger pro CLI komunikaci

Zachytávání výjimek:
- ReadConfigFileError: Výjimky vyvolané při načítání konfiguračního souboru (_load_and_validate_config < read_config_file)
- ValidateDictFormatError: Výjimky vyvolané při ověření, že se jedná o slovník s daty (_load_and_validate_config < validate_dict_format)
- ValidateKeyError: Výjimka vyvolana při ověření klíčů obsažených ve slovníku (_load_and_validate_config < _validate_key_and_value)
- ValidateValueError: Výjimka vyvolana při ověření hodnot daných klíčů obsažených ve slovníku (_load_and_validate_config < _validate_key_and_value)
- MergeWithDefaultsError: Výjimky vyvolané při snaze o kompletaci klíčů dle defaultních hodnot
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Union, Optional, Set

from ..utils import load_and_validate_config_file, merge_with_defaults
from ..keys import KEYS_DATA

from ..errors import (
    ValidateKeyError,
    ValidateValueError,
    MergeWithDefaultsError,
    ReadConfigFileError,
    ValidateDictFormatError
)


def _read_existing_config(
        config_path: Path,

) -> Optional[Dict[str, Union[int, str, bool]]]:
    """
    Pokusí se načíst existující konfiguraci.

    Metoda nejprve ověří, zda existuje konfigurační soubor.
    Pokud ano, načte z něj data a ověří jejich platnost.
    Pokud nějaká data chybý, bude nastaven pokyn pro přepsání konfiguračního souboru.
    Metoda dále je zodpovědná za zpracování všech případných výjimek
    a jejich zprostředkování vývojáři skrze CLI.

    Returns:
        Optional[Dict]: Načtená konfigurace nebo None v případě chyby
    """

    # Kontrola, zda konfigurační soubor existuje
    if not config_path.exists():

        # Navrácení hodnoty None jako potvrzení, že se konfiguraci nepovedlo načíst
        return None

    # Blok kodu
    try:

        # Načtení a validace konfiguračního souboru
        config_dict = load_and_validate_config_file(config_path)

        # Kontrola zda konfigurační soubor obsahuje všechny klíče
        if set(config_dict.keys()) != set(KEYS_DATA.keys()):

            # Doplnění chybějícíh klíčů
            config_dict = merge_with_defaults(config_dict)

            # Nastavení atribut deklarujícího vytvoření nového souboru
            self._create_config_file = True

        # Navrácení slovníku se všemi klíči a aktuálními hodnotami
        return config_dict

    # Zachycení všech výjimek které mohu nastat
    except (
            ReadConfigFileError,
            ValidateDictFormatError,
            ValidateKeyError,
            ValidateValueError,
            MergeWithDefaultsError
    ) as e:

            # Vytvoření logu popisující výjimku
            self.cli_log.warning(f"{e}", extra=e.extra)

            # Navrácení hodnoty None jako potvrzení, že se konfiguraci nepovedlo načíst
            return None