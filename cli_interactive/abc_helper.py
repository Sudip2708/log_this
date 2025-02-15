from abc import abstractmethod

def abc_property(name):
    """
    Vytvoří abstraktní property s getterem a setterem.

    Použití:
    class MyABC:
        show_help = abc_property('show_help')
        response = abc_property('response')
    """

    def getter(self):
        pass

    def setter(self, value):
        pass

    return property(
        abstractmethod(getter),
        abstractmethod(setter)
    )

def abc_method(name, *args):
    """
    Vytvoří abstraktní metodu s definovanými parametry.

    Použití:
    class MyClass:
        my_method = abc_method("my_method", "param1", "param2")
    """
    def method_stub(self, *_args):
        pass

    return abstractmethod(method_stub)
