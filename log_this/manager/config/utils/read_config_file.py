from pathlib import Path
import json

class CLIReadConfigFileError(Exception):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, exception_type, config_file_path, error_info: dict):
        # Inicializace základní výjimky
        self.exception_type = exception_type
        message = f"An error occurred while reading config file: '{config_file_path}'."
        super().__init__(message)

        # Přidání extra informací o klíči pro CLI logging
        self.extra = {
            "detail": error_info.get("detail", ""),
            "hint": error_info.get("hint", "")
        }


def read_config_file(
        config_file_path: Path
) -> config_dict:
    """
    Reads a configuration file and returns a dictionary with configurations.

    The method first tries to load the content of the file.
    If successful, it logs a confirmation message and returns the content.

    Args:
        config_file_path (Path): Path to the file.

    Returns:
        dict: Dictionary with the configuration.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """

    try:

        # Open and load data from the file
        with config_file_path.open('r') as config_file:
            config_data = json.load(config_file)

        return config_data


    except FileNotFoundError as e:
        """
        Proč je v kódu: Tato výjimka se vyhazuje, pokud cesta k souboru, kterou se pokoušíš otevřít, neexistuje.
        Zda může nastat: Ano, tato výjimka je zcela relevantní. Pokud soubor, který se pokoušíš načíst, neexistuje, Python vyhodí tuto výjimku.
        Doporučení: Tento blok by měl zůstat v kódu.
        """
        raise CLIReadConfigFileError(
            exception_type=FileNotFoundError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"The file path does not exist: {type(e).__name__}({str(e)})",
                "hint": "Zkontrolujte, zda cesta ke konfiguračnímu souboru existuje."
            }
        )

    except PermissionError as e:
        """
        Proč je v kódu: Tato výjimka nastává, pokud nemáš oprávnění k otevření souboru (například při pokusu o zápis do souboru bez příslušného oprávnění).
        Zda může nastat: Ano, pokud soubor existuje, ale nemáš oprávnění k jeho čtení, tato výjimka nastane.
        Doporučení: Tento blok by měl zůstat v kódu.
        """
        raise CLIReadConfigFileError(
            exception_type=PermissionError,
            config_file_path=config_file_path,
            error_info={
                "detail": f"Permission denied: {type(e).__name__}({str(e)})",
                "hint": "Zkontrolujte oprávnění k souboru."
            }
        )


    except json.JSONDecodeError as e:
        """
        Proč je v kódu: Tato výjimka je vyvolána, pokud soubor obsahuje nevalidní JSON.
        Zda může nastat: Ano, pokud soubor není validní JSON (například má syntaktickou chybu), vyvolá se tato výjimka.
        Doporučení: Tento blok by měl zůstat v kódu, protože je zaměřen na konkrétní problém s deserializací JSON.
        """
        raise CLIReadConfigFileError(
            json.JSONDecodeError,
            config_file_path,
            error_info={
                "detail": (
                    f"Error during JSON deserialization: {e.msg}: "
                    f"line {e.lineno} column {e.colno} (char {e.pos})"
                ),
                "hint": "Ensure the JSON syntax in the file is correct.",
            },
        )

    except OSError as e:
        """
        Proč je v kódu: OSError je obecná výjimka pro chyby související se soubory, například problémy s přístupem k souboru nebo s operačním systémem při čtení souboru.
        Zda může nastat: Ano, pokud dojde k nějakým nečekaným problémům při práci se souborem (například soubor je zamčený nebo došlo k nějaké jiní IO chybě).
        Doporučení: Tento blok může být zachován pro obecné chyby s I/O operacemi.
        """
        raise CLIReadConfigFileError(
            OSError,
            config_file_path,
            error_info={
                "detail": f"An I/O error occurred: {type(e).__name__}({str(e)})",
                "hint": "Check file permissions or possible locks on the file.",
            },
        )

    except Exception as e:
        """
        Proč je v kódu: Tato výjimka zachytí všechny jiné výjimky, které nejsou specifikovány výše.
        Zda může nastat: Ano, tato výjimka slouží jako „záchyt“ pro všechny nečekané chyby, které by mohly nastat.
        Doporučení: Tento blok je dobrý jako poslední záchyt pro neznámé chyby.
        """
        raise CLIReadConfigFileError(
            exception_type=type(e),
            config_file_path=config_file_path,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Kontaktujte správce systému."
            }
        )

