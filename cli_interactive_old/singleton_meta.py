from abc import ABCMeta

class SingletonMeta(ABCMeta):
    """
    Metatřída pro implementaci Singleton vzoru.

    Singleton vzor zajišťuje, že třída má pouze jednu instanci,
    která je sdílena mezi všemi, kdo se na tuto třídu odkazují.
    Metatřída SingletonMeta je určena k tomu, aby se na každé volání třídy
    vrátila vždy stejná instance.

    Atributy:
        _instances (dict): Slouží k uložení jediné instance každé třídy,
                           která používá tuto metatřídu.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Zajišťuje, že bude vytvořena pouze jedna instance dané třídy.

        Tato metoda je volána při každém pokusu o vytvoření nové instance
        třídy, která používá tuto metatřídu. Pokud již instance existuje,
        vrátí se ta existující. Pokud ne, vytvoří se nová.

        Args:
            *args: Pozice argumenty, které jsou předány konstruktoru třídy.
            **kwargs: Klíčové argumenty, které jsou předány konstruktoru třídy.

        Returns:
            object: Jediná instance dané třídy, která používá tuto metatřídu.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


