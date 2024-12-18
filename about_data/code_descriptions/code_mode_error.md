Import závislostí:

    import inspect

    from ._logger_settings import loger_settings
    
Definice funkce:

    def mode_error(func, args, kwargs):

Inicializace logeru:

        logger = loger_settings()

Chybová zpráva:

        logger.error(f"# LogThis ERROR:"
                     f"\n# >>> A valid mode for the @log_this decorator is not defined"
                     f"\n# >>> Function name: {func.__name__}"
                     f"\n# >>> File location: {inspect.getfile(func)}")

Navrácení volané funkce:

        return func(*args, **kwargs)
