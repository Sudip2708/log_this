class SingletonMeta(type):
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


class SingletonBase(metaclass=SingletonMeta):
    """
    Základní třída pro implementaci Singleton vzoru.

    Třída, která dědí od SingletonBase, bude mít zaručeno, že bude mít
    pouze jednu instanci po celé životnosti aplikace.

    Atributy:
        _instance (object): Instanci třídy, která je sdílena mezi všemi
                             pokusy o její vytvoření.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Zajišťuje, že bude vytvořena pouze jedna instance dané třídy.

        Pokud instance třídy ještě neexistuje, vytvoří ji. Pokud už
        instance existuje, vrátí ji.

        Args:
            *args: Pozice argumenty, které jsou předány konstruktoru třídy.
            **kwargs: Klíčové argumenty, které jsou předány konstruktoru třídy.

        Returns:
            object: Jediná instance dané třídy.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Testovací třída pro demonstrování použití SingletonMeta metatřídy.
class MySingleton(metaclass=SingletonMeta):
    """
    Ukázková třída používající metatřídu SingletonMeta pro implementaci
    Singleton vzoru.

    Tato třída bude mít pouze jednu instanci během života aplikace.
    """

    def __init__(self, value):
        """
        Inicializuje novou instanci třídy MySingleton.

        Parametry:
            value (str): Hodnota, která bude přiřazena k instanci.
        """
        self.value = value

    def __repr__(self):
        """
        Reprezentace instance jako řetězec.

        Returns:
            str: Textová reprezentace instance s hodnotou.
        """
        return f"MySingleton(value={self.value})"


# Testování použití
if __name__ == "__main__":
    # Vytvoření první instance
    instance1 = MySingleton("First Instance")
    print(instance1)  # MySingleton(value=First Instance)

    # Vytvoření druhé instance
    instance2 = MySingleton("Second Instance")
    print(instance2)  # MySingleton(value=First Instance) - stále ta samá instance

    # Ověření, že obě instance jsou identické
    print(instance1 is instance2)  # True
