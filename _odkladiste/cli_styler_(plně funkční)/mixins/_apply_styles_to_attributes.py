# cli_styler/mixins/_set_current_styles_attributes.py
from abc import ABC
from abc_helper import abc_method
from ..styles_settings import STYLES_DICT
from ..style_class import StyleClass

class ApplyStylesToAttributesMixin(ABC):
    """
    Mixin přidávající metody třídě CLIStyler.

    Jedná se o metody které na základě hodnot z konfiguračního slovníku
    vytvoří instance třídy StyleClass, definující nastavení konkrétního stylu,
    a přepíše jimi hodnoty příslučných atributů definovaných na třídě CLIStyler.

    Mixin používá interní metody pro kontrolu obsahu konfiguračního slovníku
    a získání aktuálně vybraného modu pro zobrazení znaků a barevného modu.
    """

    # Metoda pro kontrolu atributů.
    _check_style_attributes = abc_method("_check_style_attributes")

    # Metoda vrátí id pro aktuálně vybranou sadu znaků a barevný mod
    _get_current_ids = abc_method("_get_current_ids")


    def _apply_styles_to_attributes(self):
        """
        Metoda pro změnu/nastavení atributů se styly

        Metoda nejprve provede kontrolu konfiguračního slovníku,
        zda se všechny jeho klíče přesně shodují s atributy pro styl.
        - Pokud ne bude vyvolaná výjimka.

        Metoda násldně přepíše hodnoty atributů nově vytvořenými
        instancemi třídy StyleClass, definujích hodnoty pro konkrétní styly.

        Hint:
            STYLES_DICT:
                Slovník obsahující nastavení pro všechny styly.
        """

        # Volání metody pro kontrolu bsahu konfiguračního slovníku
        self._check_style_attributes(STYLES_DICT)

        # Volání metody pro přepis hodnot atributů stylů
        self._set_style_attributes(STYLES_DICT)


    def _set_style_attributes(self, styles_dict):
        """
        Metoda pro dianmické přidání/přepsání atributů třídy CLIStyler.

        Metoda nejprve načte id pro aktuální stadu značek a barevný mod,
        a následně prochází jednotlivé položky slovníku,
        a dle jejich klíčů přepisuje stejnojmené atributy třídy CLIStyler.

        Jako hodnotu pro atributy vytváří instance třídy StyleClass,
        obsahující definici pro získání ostylovaného textu požadovaným stylem,
        a pro jeho tisk do konzole.

        Metoda je interní metodou pro set_current_styles_attributes(self),
        takže očekává validní konfigurační slovník.

        Hint:
            STYLES_DICT:
                Slovník obsahující nastavení pro všechny styly.
            StyleClass:
                Třída pro vytváření instancí jednotlivých stylů.
        """

        # Načtení id pro aktuálně zvolené značky a barevný režim
        ids = self._get_current_ids()

        # Přepsání atributů třídy na základě jejich shody s názvy klíčů
        for key, style_dict in STYLES_DICT.items():
            setattr(self, key, StyleClass(style_dict, ids))



