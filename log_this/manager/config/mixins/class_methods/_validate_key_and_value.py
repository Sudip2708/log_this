from typing import Union
from log_this.manager.config.cli.raise_with_extra import raise_with_extra


class ValidateKeyAndValueMixin:

    @classmethod
    def _validate_key_and_value(
            cls,
            key: str,
            value: Union[int, str, bool]
    ) -> None:
        """
        Validates the configuration value for a given key.

        The method first checks if the key exists in the default dictionary.
        Then it verifies if the value has custom validation rules.
        If not, it checks if the value is present in the configuration dictionary
        and whether the value is in the range 0-4.

        Args:
            key (str): Configuration key
            value (Union[int, str, bool]): Value to validate

        Raises:
            KeyError: If key doesn't exist in defaults
            ValueError: If value is invalid for given key
        """

        # Check if the key exists in default dictionary
        if key not in cls.DEFAULTS:
            raise_with_extra(
                KeyError, f"Byl zadán neplatný klíč: '{key}'.",
                extra = {
                    "detail": f"Zde je seznam povolených klíčů: \n"
                              f"{list(cls.DEFAULTS.keys())}"
                }
            )


        # Validate blank lines setting
        if key == 'blank_lines':
            if not isinstance(value, bool):
                raise ValueError(
                    f"The value for 'blank_lines' must be either True or False. "
                    f"You provided: {value}"
                )

        # Validate docstring length display setting
        elif key == 'docstring_lines':
            if not (value == 'all' or (isinstance(value, int)
                                       and not isinstance(value,
                                                          bool) and value >= 0)):
                raise ValueError(
                    f"The 'docstring_lines' setting accepts either a positive number "
                    f"(to show that many lines) or 'all' (to show the complete docstring). "
                    f"You provided: {value}"
                )

        # Validate maximum allowed nesting setting
        elif key == 'max_depth':
            if not (isinstance(value, int) and not isinstance(value, bool)
                    and value >= 0):
                raise ValueError(
                    f"The 'max_depth' setting needs a positive number to control "
                    f"how deeply nested objects can be logged. "
                    f"You provided: {value}"
                )

        # For all other cases, check if value is between 0 and 4
        else:
            if not (value in (0, 1, 2, 3, 4) and not isinstance(value, bool)):
                raise ValueError(
                    f"The '{key}' setting accepts values from 0 to 4, where higher "
                    f"numbers show more detailed information in the logs. "
                    f"You provided: {value}"
                ).extra("Extra text navíc")