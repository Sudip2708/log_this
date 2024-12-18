Import závislostí:

    from typing import Callable, Union, Optional
    from functools import wraps
    
    from .data import log_simple, log_all, log_one_line, mode_error
    
Definice dekorátoru:

    def log_this(
            mode: Optional[Union[bool, str, int]] = 'simple'
    ) -> Callable:

Přednostní zachycení přeskočený logování:

        if mode in (0, "skip_this", None, False):
            return lambda func: func
    
Definice funkce pro logování:

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
    
Zachycení požadavků na jednořádkové logování:

                if mode in (1, 'one_line', True):
                    return log_one_line(func, args, kwargs)
    
Zachycení požadavků na rozšířené logování:

                elif mode in (2, 'simple'):
                    return log_simple(func, args, kwargs)
    
Zachycení požadavků na úplné logování:

                elif mode in (3, 'all'):
                    return log_all(func, args, kwargs)
    
Zpracování výjimky, pokud nebyl zadán správný parametr:

                else:
                    return mode_error(func, args, kwargs)
    
Navrácení funkce:

            return wrapper
        return decorator
