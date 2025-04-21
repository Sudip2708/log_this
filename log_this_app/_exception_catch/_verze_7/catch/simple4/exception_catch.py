from exception_handler import handle_exception, ExceptionConfig

def exception_catch(
        *exceptions,  # Deklarace zachytávaných výjimek (zatím jen kosmetická záležitost)
        config=None,  # Možnost přidat vlastní konfiguraci pro vyřízení
        ignore=None,  # Seznam výjimek které se mají ignorovat
):
    """
    Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

    Args:
        *exceptions: Typy výjimek, které mají být zachyceny (pokud prázdné, zachytí všechny)
        config: Volitelná instance ExceptionConfig pro lokální konfiguraci
        ignore: Možnost definovat výjimky které se nemají zpracovávat
    """
    # Validace vstupu
    if exceptions:
        for exc in exceptions:
            if not issubclass(exc, BaseException):
                raise TypeError(f"{exc} není platná výjimka")

    if config and not isinstance(config, ExceptionConfig):
        raise TypeError(f"Předaná konfigurace není platnou instancí třídy ExceptionConfig")

    if ignore:
        for exc in tuple(ignore):
            if not issubclass(exc, BaseException):
                raise TypeError(f"{exc} není platná výjimka")

    # Definice logiky dekorátoru
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:

                # Kontrola zda se má vyvolaná výjimka zpracovat
                if Exception.__class__.__name__ not in tuple(ignore):

                    # Volání metody pro nstavení výjimky
                    handle_exception(e, func, config)

        return wrapper

    return decorator