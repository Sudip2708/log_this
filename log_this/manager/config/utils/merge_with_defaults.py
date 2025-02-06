from typing import Dict, Union

from ..errors import MergeWithDefaultsError
from ..keys import default_values


def merge_with_defaults(
        new_config_dict: Dict[str, Union[int, str, bool]],
) -> Dict[str, Union[int, str, bool]]:
    """
    Sloučí načtený slovník s výchozími hodnotami a přidá chybějící klíče.

    Args:
        new_config_dict (Dict[str, Any]): Načtený konfigurační slovník.

    Returns:
        Dict[str, Any]: Aktualizovaný konfigurační slovník.

    Raises:
        MergeWithDefaultsError: Pokud dojde k chybě během slučování.
    """

    try:


        # Vytvoření nového slovníku na základě defaultních dat
        default = default_values()
        updated_config = default.copy()

        # Přepsání defaultních hodnot hodnotami ze slovníku
        updated_config.update({
            key: new_config_dict.get(key, default)
            for key, default in default.items()
        })

        # Navrácení slovníku se všemi klíči a aktuálními hodnotami
        return updated_config

    # Zachycení výjimky pro případ, že config_dict není validní slovník
    except AttributeError as e:
        raise MergeWithDefaultsError(
            AttributeError,
            error_info={
                "detail": "The provided object does not support the .get() method.",
                "hint": "Ensure both inputs are dictionaries or dictionary-like objects.",
            },
        )

    # Zachycení výjimky pro případ, že config_dict není validní slovník
    except TypeError as e:
        raise MergeWithDefaultsError(
            TypeError,
            error_info={
                "detail": "Invalid data type encountered during merging.",
                "hint": "Ensure the inputs are of type Dict[str, Any].",
            },
        )

    except Exception as e:
        raise MergeWithDefaultsError(
            Exception,
            error_info={
                "detail": f"Unexpected error: {type(e).__name__}({str(e)})",
                "hint": "Check the inputs for unexpected issues or invalid data.",
            },
        )
