Import závislostí:

    import time
    import inspect
    from datetime import datetime
    
    from ._safe_serialize import safe_serialize
    from ._logger_settings import loger_settings
    
Definice funkce:

    def log_simple(func, args, kwargs):
    
Inicializace logeru a začátek měření jeho běhu:

        logger = loger_settings()
        logger_time = time.perf_counter()
    
Úvodní zpráva:

        logger.debug(f"\n# START LogThis('simple') "
                     f"| Function: '{func.__name__}' "
                     f"| {datetime.now()} |")
        logger.debug(f"# >>> File: {inspect.getfile(func)}")
        logger.debug(f"# >>> Arguments: {safe_serialize(args)}")
        logger.debug(f"# >>> Kwards: {safe_serialize(kwargs)}")
    
Volání funkce:

        try:
            result = func(*args, **kwargs)
            logger.debug(f"# >>> Result for '{func.__name__}': {result} (Type: {type(result).__name__})")
            return result
    
Zachycení výjimky:

        except Exception as e:
            logger.debug(f"# >>> Result for '{func.__name__}': An exception has been raised.")
            logger.debug(f"# >>> Exception: {type(e).__name__}: {str(e)}")
            raise
    
Dodatečné úkony:

        finally:

Oznam o ukončení:

            logger.debug(f"# END LogThis('simple') "
                         f"| Function: '{func.__name__}' "
                         f"| {datetime.now()} |"
                         f"\nLog duration: {time.perf_counter() - logger_time:.6f} seconds\n")