def raise_with_extra(exc_type, message: str, extra: dict = None):
    """
    Raises an exception with an optional extra dictionary for additional context.

    Args:
        exc_type (Type[BaseException]): The exception class to be raised (e.g., ValueError, KeyError).
        message (str): The error message to include in the exception.
        extra (dict, optional): A dictionary of additional information to attach to the exception.
            Defaults to an empty dictionary if not provided.

    Raises:
        exc_type: The specified exception type with the provided message and extra attributes.

    Example:
        try:
            raise_with_extra(ValueError, "Invalid input", extra={"key": "value"})
        except ValueError as e:
            print(e.extra)  # {'key': 'value'}
    """
    # Validate that exc_type is a subclass of BaseException
    if not isinstance(exc_type, type) or not issubclass(exc_type, BaseException):
        raise TypeError(
            f"exc_type must be an exception class, got {type(exc_type).__name__}")

    # Validate that message is a string
    if not isinstance(message, str):
        raise TypeError(
            f"message must be a string, got {type(message).__name__}")

    # Validate that extra is a dictionary or None
    if extra is not None and not isinstance(extra, dict):
        raise TypeError(
            f"extra must be a dictionary or None, got {type(extra).__name__}")

    # Initialize extra if not provided
    if extra is None:
        extra = {}

    # Create and raise the exception
    e = exc_type(message)
    e.extra = extra
    raise e
