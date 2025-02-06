from typing import Union, Set, Dict

from ..validations import validate_key, validate_value
from ..errors import ValidateKeyError, ValidateValueError
from ..cli.interactive.runners import run_config_settings
from .print_exceptions_warning import print_exceptions_warning


def validate_key_and_value(
        key: str,
        value: Union[int, str, bool]
):

    try:

        # Validace klíče
        validate_key(key)

        # Validace hodnoty
        validate_value(key, value)

    # Zacycení zadání vadného klíče
    except ValidateKeyError as e:

        # Výpis do konzole
        print_exceptions_warning(
            exception=e,
            conclusion=(
                "Pokud si přejete pokračovat ve změně,",
                "vyberte klíč z násedující nabídky:",
            )
        )

        # Aktivace interaktivního výběru klíče
        run_config_settings()

    # Zachycení zadání vadné hodnoty (předpokládá že klíč je správně)
    except ValidateValueError as e:

        # Výpis do konzole
        print_exceptions_warning(
            exception=e,
            conclusion=(
                "Pokud si přejete pokračovat ve změně,",
                "vyberte hoodnotu z následující nabídky:",
            )
        )

        # Aktivace interaktivního výběru hodnoty pro daný klíč
        run_config_settings(key)