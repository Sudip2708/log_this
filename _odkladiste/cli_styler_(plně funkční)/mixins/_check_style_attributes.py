# cli_styler/mixins/_check_style_attributes.py
from abc import ABC

from .exceptions import raise_attributes_error
from ..style_class import StyleClass


class CheckStyleAttributesMixin(ABC):
    """
    Mixin přidávající metody třídě CLIStyler.

    Jedná se o metody pro kontrolu zda se načítané styly ze slovníku
    se shodují se styli definovanými atributy třídy.
    """

    def _check_style_attributes(self, styles_dict):
        """
        Metoda pro kontrolu atributů.

        Metoda očekává interně předaný slovník se styly,
        očekává tedy validní data.

        Metoda porovná klíče slovníku s atributy stylů třídy CLIStyler.
        Pokud se klíče s atributy neshodují vyvolá výjimku
        s oznamem o chybějícíh, nebo přebytečných atributech.
        """

        # Získání množiny atributů stylů třídy CLIStyler
        attributes_set = self._get_style_attributes_set()

        # Získání množiny stylů ze slovníku
        styles_set = set(styles_dict.keys())

        # Porovnání zda se schodují
        if attributes_set != styles_set:

            # Pokud se neshodují dojde k vyvolání výjimky s oznamem
            raise_attributes_error(attributes_set, styles_set)


    def _get_style_attributes_set(self):
        """
        Metoda vrací množinu atributů pro styly definované v této třídě.

        Metoda nejprve načte názvy všech atributů a metod třídy.
        Následně odfiltruje ty metoda a atributy, které začínají podtržítkem,
        a vybere jen ty které neodkazují na metodu.

        Hlavní třída CLIStyler je koncipovaná tak, že veškeré atributy
        neobsahující definici stylu začínají podtržítke.

        Hint:
            dir(self):
                Vrací názvy všech atributů a metod třídy.
            key.startswith("_"):
                Vybrání metod a atributů začínajících podtržítkem.
            getattr(self, key):
                Získání hodnoty na které metoda nebo atribut odkazuje.
            isinstance():
                Ověří zda daná hodnota odpovídá dané instanci.
            StyleClass:
                Základní třída přes kterou se definují atributy stylů.
        """

        return {

            # Získání názvů atributů a metod třídy CLIStyler
            key for key in dir(self)

            # Filtrace atributů odkazujících na instanci StyleClass
            if not key.startswith("_")
               and not callable(getattr(self, key))

        }




