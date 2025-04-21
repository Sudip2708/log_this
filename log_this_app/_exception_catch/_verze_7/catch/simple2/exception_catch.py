from .exception_handler_config import ExceptionConfig


def get_handler(config):
    # Určení konfigurace k použití
    # 1. Lokální konfigurace (pokud je poskytnuta)
    # 2. Globální konfigurace (pokud existuje)
    # 3. Nová výchozí konfigurace
    if config:
        return config
    global_config = ExceptionConfig.get_global_instance()
    return global_config if global_config else ExceptionConfig()


def exception_catch(*exceptions, config: ExceptionConfig = None):
    """
    Dekorátor pro zachytávání specifikovaných výjimek a logování chyb.

    Args:
        *exceptions: Typy výjimek, které mají být zachyceny
        config: Volitelná instance ExceptionHandlerConfig pro lokální konfiguraci
    """

    # Kontrola platnosti výjimek
    for _exc in exceptions:
        if not issubclass(_exc, BaseException):
            raise TypeError(f"{_exc} není platná výjimka")

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                _handle_exception(e, func, config)
        return wrapper

    return decorator


def _handle_exception(exception, func, config):
    
    # Načtení konfigurace pokud je předaná
    config = get_config(config)

    # Načtení konfigurace pro danou výjimku
    exc_config = config.get_exc_handler(exception)

    # Kontrola zda má výjinka nastavenou vlastní logiku
    if exc_config.action:

        # Zpuštění logyky
        exc_config.action()

    # Načtení zprávy
    message = exc_config.get_message(func, exception)

    # Kontrola zda se má vytvořit log
    if exc_config.log_level != "NO_LOG":

        # Vytvoření logu
        exc_config.log(message)

    # Kontrola, zda se má logovat i do souboru
    if exc_config.log_file_path:

        # Vytvoření zápisu do souboru
        exc_config.log_to_file(message)

    # Kontrola zda je nastaveno že se nemá vyvolat výjimka
    if exc_config.raise_exception:
        raise




def _get_message(exc_config, func, exception):
    # Vytvoření zprávy
    prefix = exc_config.prefix  # "[DB]"
    message = exc_config.message  # "Chyba při vykonávání "
    func_name = func.__name__  # "moje_funkce"

    # Přepis výjimky
    exc_name = exception.__class__.__name__
    exc_description = str(exception)

    # Doplňující informace
    # Načtení traceback u
    tb = traceback.extract_tb(exception.__traceback__)
    last_frame = tb[-1]  # Poslední krok v tracebacku (tato funkce)
    first_frame = tb[0] if len(tb) > 1 else "" # Původ výjimky

    # Definice textu
    filename = last_frame.filename  # "muj_soubor.py"
    line_number = last_frame.lineno  # 15
    line_code = last_frame.line  # "return 10 / 0"

    # Definice doplňujícího textu o počátku chyby
    origin = ""
    if first_frame:
        or_filename = last_frame.filename  # "muj_soubor.py"
        or_line_number = last_frame.lineno  # 15
        or_line_code = last_frame.line  # "return 10 / 0"
        origin = f"Původ: {or_filename}, řádek: {or_line_number}, kód: {or_line_code}. \n"

    # Definice ukončení
    end = '\n' if exc_config.blank_line else ''

    return (
        f"{prefix}{message}{func_name}. {exc_name} - {exc_description}. \n"
        f"Soubor: {filename}, řádek: {line_number}, kód: {line_code}. {origin}.{end}\n"
    )

def get_config(config):
    """Vrátí konfiguraci"""

    # Načtení konfigurace pokud je předaná
    if config:

        # Kontrola zda jde o validní data - mohlo by být nahrazeno metodou config.validate()
        if isinstance(config, ExceptionConfig):
            config.validate()
        else:
            raise ValueError("Předaná konfigurace není platnou konfigurací")

        return config

    # Volání metody, která buď vrátí globální konfiguraci (je-li) a nebo defaultní
    return ExceptionConfig.get_config()



