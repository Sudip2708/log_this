from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from ._styles_settings import StyleBase


class StylePrinter:
    """Spravuje všechny styly CLI a umožňuje tisknout stylované texty."""

    # Atribut pro dočasné umístění instance stylu
    _style_instance = None

    def __init__(self, get_style):
        # Načtení instance StylesManager pro získání stylu
        self._get_style = get_style


    def __getattr__(self, attr):
        """Dynamicky zpracuje požadovaný atribut."""

        # První průchod pro načtení instance stylu
        if self._style_instance is None:
            return self._load_style_instance(attr)

        # Druhý průchod pro vytištění stylovaného textu
        return self._print_styled_text(attr)



    def _load_style_instance(self, attr):
        """
        Metoda pro zpracování prvního průchodu metody __getattr__

        Načte instanci stylu, nebo vyvolá výjimku.
        """

        # Získání instance pro styl nebo None
        new_instance = getattr(self._get_style, attr, None)

        # Ověření instance a zápis instance do atributu
        if isinstance(new_instance, StyleBase):
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

        # Ověření atributu a navrácení metody pro tisk do konzole
        if hasattr(self._style_instance, attr):
            return lambda *text: self._execute_print(attr, *text)

        # Vyvolání výjimky, pokud atribut neexistuje
        raise AttributeError(
            f"Atribut '{attr}' neexistuje "
            f"v '{self._style_instance.__class__.__name__}'."
        )

    def _execute_print(self, attr, *texts):
        """
        Pomocná metoda pro vytištění ostylovaného textu.

        Podporuje jak jeden řetězec, tak více řetězců.
        """

        # Získání instance stylu
        style_method = getattr(self._style_instance, attr)

        # Pokud nejsou argun´menty předané jako tuple, převeď je na tuple
        if not isinstance(texts, tuple):
            texts = tuple(texts)


        # Iterace přes všechny řetězce a jejich výpis
        for text in texts:
            if text:
                styled_text = style_method(text)
                print_formatted_text(FormattedText([styled_text]))
            else:
                self.empty_line() # pro rozřádkování v textu - aktivuje se prázdným řetězcem

        # Vytisknutí odělujícího řádku (pouze pokud je více řádků)
        if len(texts) > 1:
            self.empty_line()

        # Po ukončení iterace resetujeme instanci stylu
        self._style_instance = None

    @staticmethod
    def empty_line():
        """Vytisknutí prázdného řádku"""
        print_formatted_text(FormattedText([('', '')]))


