# cli_styler/mixins/_set_colors_mode.py
from abc import ABC
from abc_helper import abc_method, abc_property

class SetColorsModeMixin(ABC):
    """
    Mixin přidávající metody třídě CLIStyler.

    Jedná se o metody pro validaci a změnu barevného modu.

    Mixin používá interní atributy pro definici barevného modu
    a metodu pro nastavení aktuálně zvoleného modu.
    """

    # Atributy pro slovník defuinující možnosti pro zobrazení barevného modu
    _colors_modes = abc_property("_colors_modes")

    # Atribut definující aktuálně používaný barevný mod
    _current_colors_mode = abc_property("_current_colors_mode")

    # Metoda pro změnu/nastavení atributů se styly
    _apply_styles_to_attributes = abc_method("_apply_styles_to_attributes")


    def set_colors_mode(self, colors_mode: str):
        """
        Metoda pro změnu barevného modu pro instanci třídy CLIColor.

        Metoda očekává řetězec reprezentující název barevného modu.

        Metoda nejprve validuje obdržený mod.
        - Pokud není validní bude vyvolaná výjimka s výpisem validních hodnot.

        Následně metoda ověří, zda zadaný mod není již aktuálně zvolen
        - Pokud ne, dojde k přepsání atributu pro aktuální mod
            a volání metody jenž přepíše obsah všech atributů pro styly.
        - Pokud ano, vypíše se oznam s informací o neprovedení žádné změny.
        """

        # Validace nově zadaného modu
        self._validate_colors_mode(colors_mode)

        # Kontrola zda ybraný mod není již aktivní
        if self._current_colors_mode != colors_mode:

            # Nastavení atributu pro aktuální mod na nový mod
            self._current_colors_mode = colors_mode

            # Volání metody pro přepsání všech atributů se styly
            self._apply_styles_to_attributes()

        # Pokud je vybraný mod již aktivním
        # Vypíše se pouze oznam
        else:
            print(
                "Požadovaný barevný mod je již aktivní. "
                "Žádná změna nebyla učiněna."
            )


    def _validate_colors_mode(self, colors_mode):
        """
        Metoda pro validaci barevného režimu.

        Metoda očekává řetězec reprezentující název barevného modu.

        Následně v slovníku pro definici modu ověří,
        zda je zadaný název validní.
        - Pokud ne vyvolá výjimku s výpisem validních hodnot.
        """

        # Kontrola přítomnosti modu ve slovníku pro definici barevných modů
        if not colors_mode in self._colors_modes.keys():
            raise ValueError(
                f"Byl zadán neplatný set barvy. "
                f"Povolené sety: {self._colors_modes.keys()}"
            )