Import závislostí:

    from ._safe_serialize import safe_serialize
    from ._logger_settings import loger_settings
    from datetime import datetime
    
Definice funkce:

    def log_one_line(func, args, kwargs):

Inicializace logeru:
    
        logger = loger_settings()

Zpráva:

        logger.info(f"# INFO LogThis('one_line') "
                    f"| Function: {func.__name__} "
                    f"| {datetime.now()} "
                    f"| Arguments: {safe_serialize(args)} ")
    
Navrácení volané funkce:

        return func(*args, **kwargs)