from abc import ABC
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from abc_helper import abc_property
from .._styles_settings import StyleBase

class StylePrinterMethodsMixin(ABC):

    # Atribut pro instanci StylesManager
    _get_style = abc_property("_get_style")

    # Atribut pro dočasné umístění instance stylu
    _style_instance = abc_property("_style_instance")


    def _load_style_instance(self, attr):
        """
        Metoda pro zpracování prvního průchodu metody __getattr__

        Načte instanci stylu, nebo vyvolá výjimku.
        """

        # Získání instance pro styl nebo None
        new_instance = getattr(self._get_style, attr, None)

        # Ověření instance
        if isinstance(new_instance, StyleBase):

            # Zápis instance do atributu
            self._style_instance = new_instance

            # Navrácení instance pro druhý průchod
            return self

        # Vyvolání výjimky pokud new_instance nebyla získaná, nebo ověřená
        raise AttributeError(f"Styl '{attr}' neexistuje.")


    def _print_styled_text(self, attr):
        """
        Metoda pro zpracování druhý průchodu metody __getattr__

        Vyhledá na načtené instaci druhý předaný atribut
        a předá ho jako první parametr metody _execute_print,
        a jako druhý ji předá zadaný text.
        Pokud atribut na třídě neexistuje, bude vyvolaná výjimka.
        """

        # Získání atributu odkazující na navázanou instanci StyleItems
        if hasattr(self._style_instance, attr):

            # Navrácení metody pro tisk do konzole
            return lambda text: self._execute_print(attr, text)

        # Vyvolání výjimky, pokud atribut neexistuje
        raise AttributeError(
            f"Atribut '{attr}' neexistuje "
            f"v '{self._style_instance.__class__.__name__}'."
        )


    def _execute_print(self, attr, text):
        """
        Pomocná metoda pro vytištění ostylovaného textu

        Metoda nejhprve získá tuple se stylem a doplněným textem.
        Ten pak mopocí metod prompt_toolkit vytiskne do konzole.
        Nakonec metoda resetuje stav pro instanci stylu.
        """

        # Získání tuple s ostylovaným textem
        styled_text = getattr(self._style_instance, attr)(text)

        # Vytištení tuple do konzole
        print_formatted_text(FormattedText([styled_text]))

        # Reset atributu pro instanci stylu
        self._style_instance = None
