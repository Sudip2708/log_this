from typing import Dict, Any




def validate_dict_format(config_data: Any) -> bool:
    """
    Validates that the input data is a dictionary and not empty.
    Raises a custom exception if the validation fails.
    """
    if not isinstance(config_data, dict):
        raise ValidateDictFormatError(
            TypeError,
            error_info={
                "detail": f"Validation failed: Expected a dictionary. "
                          f"Received type: {type(config_data).__name__}",
                "hint": "Ensure the input is a dictionary.",
            },
        )

    if not config_data:
        raise ValidateDictFormatError(
            ValueError,
            error_info={
                "detail": "Validation failed: Received an empty dictionary. "
                          "The configuration dictionary is empty.",
                "hint": "Ensure the configuration contains valid key-value pairs.",
            },
        )


