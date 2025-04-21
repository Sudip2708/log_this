def exception_catch(*exceptions, config=None):
    """
    Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

    Args:
        *exceptions: Typy výjimek, které mají být zachyceny (pokud prázdné, zachytí všechny)
        config: Volitelná instance ExceptionConfig pro lokální konfiguraci
    """
    # Validace výjimek
    for exc in exceptions:
        if not issubclass(exc, BaseException):
            raise TypeError(f"{exc} není platná výjimka")

    # Vytvoření výchozího handleru
    handler = ExceptionHandler(config)

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Pokud byly specifikovány výjimky a aktuální výjimka není v seznamu, nechej ji projít
                if exceptions and not any(
                        isinstance(e, exc) for exc in exceptions):
                    raise

                # Jinak zpracuj výjimku
                handler.handle_exception(e, func, config)

        return wrapper

    return decorator