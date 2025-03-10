from typing import Union
from log_this_old.manager.config.cli.raise_with_extra import raise_with_extra


class ValidateKeyAndValueMixin:
    key_hint = {
    "skip_this": {
        "Popis": "Slovní definice modu pro přeskočení logování.",
        "Default": "Defaultní hodnota pro tento mod je 0 (přeskočt logování).",
    },
    "one_line": {
        "Popis": "Slovní definice modu pro jednořádkové logování.",
        "Default": "Defaultní hodnota pro tento mod je 1 (jednořádkový výpis).",
    },
    "simple": {
        "Popis": "Slovní definice modu pro základní mod umožňující vnořené logování (4 řádky).",
        "Default": "Defaultní hodnota pro tento mod je 2 (základní výpis).",
    },
    "detailed": {
        "Popis": "Slovní definice modu pro rozšířený mod umožňující vnořené logování (6 řádky).",
        "Default": "Defaultní hodnota pro tento mod je 3 (rozšířený výpis).",
    },
    "report": {
        "Popis": "Slovní definice modu pro podrobný výpis logování (10+ řádků).",
        "Default": "Defaultní hodnota pro tento mod je 4 (podrobný výpis).",
    },
    "true": {
        "Popis": "Nastavení pro zadání modu jako kladné boolean hodnty True.",
        "Default": "Defaultní hodnota pro tento mod je 1 (jednořádkový výpis).",
    },
    "false": {
        "Popis": "Nastavení pro zadání modu jako záporné boolean hodnty False.",
        "Default": "Defaultní hodnota pro tento mod je 0 (přeskočt logování).",
    },
    "none": {
        "Popis": "Nastavení pro zadání modu jako None hodnty.",
        "Default": "Defaultní hodnota pro tento mod je 0 (přeskočt logování).",
    },
    "empty": {
        "Popis": "Nastavení pro výchozí chování, pokud mod není zadán.",
        "Default": "Defaultní hodnota pro tento mod je 0 (přeskočt logování).",
    },
    "indent": {
        "Popis": "Nastavení počtu mezer odsazení od kraje pro zanořené logování.",
        "Default": "Defaultní hodnota pro tento mod je 2 (odsazení dvě mezery). Pro skrytí odsazení je potřeba zde nastavit hodnotu 0",
    },
    "blank_lines": {
        "Popis": "Nastavení, zda se mají mezi jednotlivými logy zobrazovat prázdné řádky.",
        "Default": "Defaultní hodnota pro tento mod je true (zobrazovat prázdné řádky)",
    },
    "docstring_lines": {
        "Popis": "Nastavení zobrazení docstringu v plném výpisu logování.",
        "Default": "Defaultní hodnota pro tento mod je 3 (z docstringu se zobrazí poze tři první neprázdné řádky).",
    },
    "max_depth": {
        "Popis": "Nastavení úrovně maximální rekurrze pro serializaci dat.",
        "Default": "Defaultní hodnota pro tento mod je 100 (Výjimka se vyvolá po 100 zanořených volání).",
    },
}

    @classmethod
    def _validate_key_and_value(
            cls,
            key: str,
            value: Union[int, str, bool]
    ) -> None:
        """
        Validates the configuration value for a given key.

        The method first checks if the key exists in the default dictionary.
        Then it verifies if the value has custom validation rules.
        If not, it checks if the value is present in the configuration dictionary
        and whether the value is in the range 0-4.

        Args:
            key (str): Configuration key
            value (Union[int, str, bool]): Value to validate

        Raises:
            KeyError: If key doesn't exist in defaults
            ValueError: If value is invalid for given key
        """

        # Check if the key exists in default dictionary
        if key not in cls.DEFAULTS:
            raise_with_extra(
                KeyError,
                f"Byl zadán neplatný klíč: '{key}'.",
                extra = {
                    "detail": f"Zde je seznam povolených klíčů: \n"
                              f"{list(cls.DEFAULTS.keys())}"   # vytvořit seznam s popisem klíčů
                    # Generovat seznam z aktuálního slovníku a načítat data s popisného slovníku.
                }
            )


        # Validate blank lines setting
        if key == 'blank_lines':
            if not isinstance(value, bool):
                raise_with_extra(
                    ValueError,
                    f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'.",
                    extra={
                        "detail": f"Povolené hodnoty pro klíč '{key}': \n"
                                  f"True (Nastavuje zobrazení prázdné řádky mezi jednotlivými logy.) \n"
                                  f"False (Nastavuje aby jednotlivé logy nebyli oddělené prázdnou řádkou.)",
                        "hint": f"Klíč '{key}' nastavuje zobrazení/skrytí prázdné řádky mezi jednotlivými logy."
                                f"Pro jednořádkové výpisy je přehlednější výstup bez prázdné řádky (hodnota: False). \n"
                                f"Pro víceřádkové výpisy je je přehlednější výstup s prázdnou řádkou (hodnota: True)."
                    }
                )

        # Validate docstring length display setting
        elif key == 'docstring_lines':
            if not (value == 'all'
                    or (isinstance(value, int)
                        and not isinstance(value, bool)
                        and value >= 0)):
                raise_with_extra(
                    ValueError,
                    f"Pro klíč 'docstring_lines' byla zadaná neplatná hodnota: '{value}'.",
                    extra={
                        "detail": f"Povolené hodnoty pro klíč 'docstring_lines': \n"
                                  f"Celé kladné číslo (Nastavuje počet řádků z docstringu, které se mají ve modu 'report' objevit.) \n"
                                  f"'all' (Nastavuje aby se při výpisu modu 'report' zobrazoval celý obsah docstringu.)",
                        "hint": f"Klíč 'docstring_lines' nastavuje zobrazení docstringu ve výstupu pro mod 'report'. \n"
                                f"Pokud je zadáná hodnota celé číslo, vztahuje se pouze na řádky s textem. Prázdné řádky jsou vynechány.  \n"
                                f"Pokud je zadaná hodnota 'all' docstring se oběví v podobě v jaké je zapsán."
                    }
                )

        # Validate maximum allowed nesting setting
        elif key == 'max_depth':
            if not (isinstance(value, int)
                    and not isinstance(value, bool)
                    and value >= 0):
                raise_with_extra(
                    ValueError,
                    f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'.",
                    extra={
                        "detail": f"Povolené hodnoty pro klíč 'max_depth': \n"
                                  f"Celé kladné číslo (Nastavuje maximální počet vnitřní rekurze při serializaci dat.)",
                        "hint": f"Klíč 'max_depth' nastavuje limit rekruze pro serializaci (bezpečnou extrakci obsahu) pro data uložená v zanořených sekvencích. \n"
                                f"Tato kontrola se hodí, pokud máte zájem zjistit zda nedochází v kodu k nadměrné rekurzi vnitřního volání.  \n"
                                f"Defaultně je nastavena na hodnotu 100, kde je již velká pravděpodobnost že se jedná o chybu rekurze.  \n"
                                f"Pro detailnější analízu kodu se však někdy mohou hodit i velmi malé hodnoty. ",
                        "warning": "Pokud necháte nastavenou malou hodnotu, může se vám stát, že být hlášen falešný error pro kod který je v pořádku. "
                    }
                )


        # For all other cases, check if value is between 0 and 4
        else:
            if not (value in (0, 1, 2, 3, 4) and not isinstance(value, bool)):
                raise ValueError(
                    f"The '{key}' setting accepts values from 0 to 4, where higher "
                    f"numbers show more detailed information in the logs. "
                    f"You provided: {value}"
                ).extra("Extra text navíc")