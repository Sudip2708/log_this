Import závislostí:

    import time
    import inspect
    import tracemalloc
    from datetime import datetime

    from ._safe_serialize import safe_serialize
    from ._logger_settings import loger_settings
    
Definice funkce:

    def log_all(func, args, kwargs):
    
Inicializace logeru a začátek měření jeho běhu:

        logger = loger_settings()
        logger_time = time.perf_counter()
    
Úvodní zpráva:

        logger.debug(f"\n# START LogThis('all') "
                     f"| Function: '{func.__name__}' "
                     f"| {datetime.now()} |")
        logger.debug(f"# >>> File: {inspect.getfile(func)}")
        logger.debug(f"# >>> Annotations: {func.__annotations__ or 'N/A'}")
        logger.debug(f"# >>> Arguments: {safe_serialize(args)}")
        logger.debug(f"# >>> Kwards: {safe_serialize(kwargs)}")
        logger.debug(f"# >>> Docstring: {func.__doc__ or 'N/A'}")
    
Spuštění tracemalloc pro měření paměti (pouze pokud ještě neběží):

        tracing_was_active = tracemalloc.is_tracing()
        if not tracing_was_active:
            tracemalloc.start()
    
Vytvoření záznamu paměti před spuštěním fuknce:

        snapshot_before = tracemalloc.take_snapshot()
    
Zahájení měření času běhu funkce:

        function_time = time.perf_counter()
    
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
    
Zaznamenání měření času běhu funkce:

            function_duration = time.perf_counter() - function_time
    
Zpracování využití paměti:

            snapshot_after = tracemalloc.take_snapshot()
            stats = snapshot_after.compare_to(snapshot_before, 'lineno')
            memory_used = sum(stat.size_diff for stat in stats)
    
Ukončení tracemalloc (pouze pokud nebyl aktivní před voláním):

            if not tracing_was_active:
                tracemalloc.stop()
    
Závěrečná zpráva:

            logger.debug(f"# >>> Processing time: {function_duration:.6f} seconds ")
            logger.debug(f"# >>> Memory usage: {memory_used} bytes")
            logger.debug(f"# >>> Memory allocation listing:")

Cyklus pro výpis využití paměti:

            for stat in stats:
                logger.debug(f"# >>> > Allocated: {stat.size_diff} bytes, "
                             f"Line: {stat.traceback[0].lineno}, "
                             f"File: {stat.traceback[0].filename}")

Oznam o ukončení:

            logger.debug(f"# END LogThis('all') | Function: '{func.__name__}' "
                         f"| {datetime.now()} "
                         f"| Log duration: {time.perf_counter() - logger_time:.6f} seconds\n")
