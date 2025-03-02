# cli_styler/mixins/_set_sign_set.py
from abc import ABC
from abc_helper import abc_method, abc_property


class SetSymbolsModeMixin(ABC):
    """
    Mixin přidávající metody třídě CLIStyler.

    Jedná se o metody pro validaci a změnu barevného modu.

    Mixin používá interní atributy pro definici barevného modu
    a metodu pro nastavení aktuálně zvoleného modu.
    """

    # Atributy pro slovník defuinující možnosti pro zobrazení značek
    _symbols_modes = abc_property("_symbols_modes")

    # Atribut definující aktuálně používaný set značek
    _current_symbols_mode = abc_property("_current_symbols_mode")

    # Metoda pro změnu/nastavení atributů se styly
    _apply_styles_to_attributes = abc_method("_apply_styles_to_attributes")


    def set_symbols_mode(self, signs_set):
        """
        Metoda pro změnu setu značek pro instanci třídy CLIColor.

        Metoda očekává řetězec reprezentující název setu značek.

        Metoda nejprve validuje obdržený set.
        - Pokud není validní bude vyvolaná výjimka s výpisem validních hodnot.

        Následně metoda ověří, zda zadaný set není již aktuálně zvolen
        - Pokud ne, dojde k přepsání atributu pro aktuální set.
            a volání metody jenž přepíše obsah všech atributů pro styly.
        - Pokud ano, vypíše se oznam s informací o neprovedení žádné změny.
        """

        # Validace nově zadaného setu
        self._validate_symbols_mode(signs_set)

        # Kontrola zda nebyl vybrán již aktivní set
        if self._current_symbols_mode != signs_set:

            # Nastavení atributu pro aktuální set na nový set
            self._current_symbols_mode = signs_set

            # Volání metody pro přepsání všech atributů se styly
            self._apply_styles_to_attributes()

        # Pokud je set již aktuálně aktivní
        # Vypíše se pouze oznam
        else:
            print(
                "Požadovaný set značek je již aktivní. "
                "Žádná změna nebyla učiněna."
            )


    def _validate_symbols_mode(self, signs_set):
        """
        Metoda pro validaci setu značek.

        Metoda očekává řetězec reprezentující název setu značek.

        Následně v slovníku pro definici setu značek ověří,
        zda je zadaný název validní.
        - Pokud ne vyvolá výjimku s výpisem validních hodnot.
        """

        # Kontrola přítomnosti setu ve slovníku pro definici setů značek
        if not signs_set in self._symbols_modes.keys():
            raise ValueError(
                f"Byl zadán neplatný set pro značky. "
                f"Povolené sety: {self._symbols_modes.keys()}"
            )
