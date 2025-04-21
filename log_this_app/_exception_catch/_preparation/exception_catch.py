import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def exception_catch(*exceptions):
    """Dekorátor pro zachytávání specifikovaných výjimek a logování chyb."""

    # Kontrola platnosti výjimek
    for _exc in exceptions:
        if not issubclass(_exc, BaseException):
            raise TypeError(f"{_exc} není platná výjimka")

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_message = f"Chyba při vykonávání {func.__name__}: {e}"

                # Pokud máme specifikované výjimky, kontrolujeme je
                if exceptions:
                    for exc in exceptions:
                        if isinstance(e, exc):
                            logging.error(error_message, exc_info=True)
                            raise

                # Pokud žádná výjimka nesedí, nebo nejsou specifikovány, logujeme vše
                logging.error(error_message, exc_info=True)
                raise

        return wrapper

    return decorator
