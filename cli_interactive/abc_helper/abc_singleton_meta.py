from abc import ABCMeta
from threading import Lock


class AbcSingletonMeta(ABCMeta):
    """
    Thread-safe implementace Singleton vzoru pro ABC třídy.

    Bezpečná pro více vláken (thread-safe) a pro vícevláknové aplikace.
    
    Obsahuje synchronizační zámek (Lock),
    takže v případě souběžného volání konstruktoru z více vláken zajistí,
    že pouze jedno vlákno vytvoří instanci.

    Používá double-checked locking pattern, což znamená, že:
    - Nejprve se kontroluje, zda instance již existuje (mimo zámek).
    - Pokud neexistuje, získá se zámek (with cls._lock:).
    - Poté se ještě jednou zkontroluje, zda instance stále neexistuje
    (protože jiná vlákna mezitím mohla instanci vytvořit).
    - Pokud stále neexistuje, vytvoří se a uloží do _instances.

    Obsahuje clear_instance(),
    která umožňuje odstranit instanci singletonu – což je užitečné zejména
    při testování, kdy chceš mít možnost vytvořit novou instanci.
    """

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                # Double-checked locking pattern
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear_instance(cls):
        """
        Vymaže instanci singletonu - užitečné pro testování.
        """
        with cls._lock:
            if cls in cls._instances:
                del cls._instances[cls]