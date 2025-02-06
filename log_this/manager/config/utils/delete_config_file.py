from pathlib import Path

from ..errors import DeleteConfigFileError


def delete_config_file(config_file_path: Path) -> None:
    """
    Smaže konfigurační soubor.

    Args:
        config_file_path (Path): Cesta ke konfiguračnímu souboru.

    Raises:
        DeleteConfigError: Pokud nastane chyba při mazání souboru.
    """

    try:

        # Smazání aktuálního souboru
        config_file_path.unlink()


    # Pokud soubor na umístění neexistuje
    except FileNotFoundError as e:
        raise DeleteConfigFileError(
            message="Soubor na daném umístění nebyl nalezen.",
            detail=(
                "Zachycený typ výjimky: FileNotFoundError",
                f"Popis: {str(e)}"
            ),
            hint=(
                f"Je-li to možné zkontrolujte umístění souboru: {config_file_path}",
                "Dle zachycené výjimky se dá předpokládat, že na zadaném umístění soubor neexistuje."
            )
        )

    # Pokud nemáme potřebná oprávnění k smazání souboru
    except PermissionError as e:
        raise DeleteConfigFileError(
            message="Nepovedlo se odstranit konfigurační soubor",
            detail=(
                "Zachycený typ výjimky: PermissionError",
                f"Popis: {str(e)}"
            ),
            hint=(
                f"Je-li to možné zkontrolujte soubor na umístění: {config_file_path}",
                "Dle zachycené výjimky, pravděpodobně nemáte nastenena oprávnění pro jeho smazání."
            )
        )

    # Všechny ostatní případy
    except Exception as e:
        raise DeleteConfigFileError(
            message="Nepovedlo se odstranit konfigurační soubor",
            detail=(
                "Došlo k vyvolání všeobecné výjimky, zachycující nepodchycené výjimky.",
                f"Popis: {str(e)}"
            ),
            hint=(
                f"Je-li to možné zkontrolujte soubor na umístění: {config_file_path}",
                "Pokud soubor existuje, je pravděpodobné že chybu způsobuje nekonzistentí kod."
            )
        )



