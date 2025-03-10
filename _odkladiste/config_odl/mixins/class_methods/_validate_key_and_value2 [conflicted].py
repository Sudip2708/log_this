from typing import Union
from log_this_old.manager.config.cli.raise_with_extra import raise_with_extra

# Sdílené texty
detail_for_mode = (
    "Povolené hodnoty pro klíč 'skip_this': \n"
    "- 0 (Nastavuje přeskočt logování.) \n"
    "- 1 (Nastavuje jednořádkový výpis.) \n"
    "- 2 (Nastavuje základní výpis (4 řádky).) \n"
    "- 3 (Nastavuje rozšířený výpis (6 řádky).) \n"
    "- 4 (Nastavuje podrobný výpis (10+ řádků).)"
)

hint_for_mode = (
    "Klíč 'skip_this' nastavuje cování stejnnojméné definice modu."
    "Pro dočasnou celopločnou změnu chování pro tento kod. \n"
    "Doporučuje se ponechat defaultní hodnotu."
)

def validate_mode(value):
    return value in (0, 1, 2, 3, 4) and not isinstance(value, bool)

def validate_indent(value):
    return isinstance(value, int) and 0 <= value <= 4

def validate_blank_lines(value):
    return isinstance(value, bool)

def validate_docstring_lines(value):
    return value == 'all' or (isinstance(value, int) and not isinstance(value, bool) and value >= 0

def validate_max_depth(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0

# Slovník s využitím sdílených textů
key_hint = {
    "skip_this": {
        "info": "Slovní definice modu pro přeskočení logování.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '0' (přeskočt logování).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "one_line": {
        "info": "Slovní definice modu pro jednořádkové logování.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '1' (jednořádkový výpis).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "simple": {
        "info": "Slovní definice modu pro základní mod umožňující vnořené logování (4 řádky).",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '2' (základní výpis).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "detailed": {
        "info": "Slovní definice modu pro rozšířený mod umožňující vnořené logování (6 řádky).",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '3' (rozšířený výpis).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "report": {
        "info": "Slovní definice modu pro podrobný výpis logování (10+ řádků).",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '4' (podrobný výpis).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "true": {
        "info": "Nastavení pro zadání modu jako kladné boolean hodnty True.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '1' (jednořádkový výpis).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "false": {
        "info": "Nastavení pro zadání modu jako záporné boolean hodnty False.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '0' (přeskočt logování).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "none": {
        "info": "Nastavení pro zadání modu jako None hodnty.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '0' (přeskočt logování).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "empty": {
        "info": "Nastavení pro výchozí chování, pokud mod není zadán.",
        "validate": validate_mode,
        "default": "Defaultní hodnota pro tento mod je '0' (přeskočt logování).",
        "detail": detail_for_mode,
        "hint": hint_for_mode
    },
    "indent": {
        "info": "Nastavení počtu mezer odsazení od kraje pro zanořené logování.",
        "validate": validate_indent,
        "default": "Defaultní hodnota pro tento mod je '2' (odsazení dvě mezery).",
        "detail": f"Povolené hodnoty pro klíč 'skip_this': \n"
                  f"- 0 (Skrytí odstzení.) \n"
                  f"- od 1 do 4 (Počet mezer pro jedno odsazení.) ",
        "hint": f"Klíč 'skip_this' nastavuje počet mezer odsazení od kraje pro zanořené logování."
                f"Pro skrytí odsazení slouží hodnota 0. \n"
                f"Více než 4 mezery pro jedno odsazení nelze zadat."
    },
    "blank_lines": {
        "info": "Nastavení, zda se mají mezi jednotlivými logy zobrazovat prázdné řádky.",
        "validate": validate_blank_lines,
        "default": "Defaultní hodnota pro tento mod je 'true' (zobrazovat prázdné řádky)",
        "detail": f"Povolené hodnoty pro klíč 'blank_lines': \n"
                  f"- True (Nastavuje zobrazení prázdné řádky mezi jednotlivými logy.) \n"
                  f"- False (Nastavuje aby jednotlivé logy nebyli oddělené prázdnou řádkou.)",
        "hint": f"Klíč 'blank_lines' nastavuje zobrazení/skrytí prázdné řádky mezi jednotlivými logy."
                f"Pro jednořádkové výpisy je přehlednější výstup bez prázdné řádky (hodnota: False). \n"
                f"Pro víceřádkové výpisy je je přehlednější výstup s prázdnou řádkou (hodnota: True)."
    },
    "docstring_lines": {
        "info": "Nastavení zobrazení docstringu v plném výpisu logování.",
        "validate": validate_docstring_lines,
        "default": "Defaultní hodnota pro tento mod je '3' (z docstringu se zobrazí poze tři první neprázdné řádky).",
        "detail": f"Povolené hodnoty pro klíč 'docstring_lines': \n"
                  f"- Celé kladné číslo (Nastavuje počet řádků z docstringu, které se mají ve modu 'report' objevit.) \n"
                  f"- 'all' (Nastavuje aby se při výpisu modu 'report' zobrazoval celý obsah docstringu.)",
        "hint": f"Klíč 'docstring_lines' nastavuje zobrazení docstringu ve výstupu pro mod 'report'. \n"
                f"Pokud je zadáná hodnota celé číslo, vztahuje se pouze na řádky s textem. Prázdné řádky jsou vynechány. \n"
                f"Pokud je zadaná hodnota 'all' docstring se oběví v podobě v jaké je zapsán."
    },
    "max_depth": {
        "info": "Nastavení úrovně maximální rekurrze pro serializaci dat.",
        "validate": validate_max_depth,
        "default": "Defaultní hodnota pro tento mod je '100' (Výjimka se vyvolá po 100 zanořených volání).",
        "detail": f"Povolené hodnoty pro klíč 'max_depth': \n"
                  f"- Celé kladné číslo (Nastavuje maximální počet vnitřní rekurze při serializaci dat.)",
        "hint": f"Klíč 'max_depth' nastavuje limit rekruze pro serializaci (bezpečnou extrakci obsahu) pro data uložená v zanořených sekvencích. \n"
                f"- Tato kontrola se hodí, pokud máte zájem zjistit zda nedochází v kodu k nadměrné rekurzi vnitřního volání. \n"
                f"- Defaultně je nastavena na hodnotu 100, kde je již velká pravděpodobnost že se jedná o chybu rekurze. \n"
                f"- Pro detailnější analízu kodu se však někdy mohou hodit i velmi malé hodnoty. \n"
                f"- Upozornění: Pokud necháte nastavenou malou hodnotu, může se vám stát, že být hlášen falešný error pro kod který je v pořádku. ",

    },
}

class CLIValueError(ValueError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, value: Union[int, str, bool], key_data: dict):
        # Inicializace základní výjimky
        message = f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'."
        super().__init__(message)

        # Načtení informací o klíči pro detail a hint
        self.extra = {
            "detail": key_data.get("detail", ""),
            "hint": key_data.get("hint", "")
        }

        # Nastavení extra atributu pro výjimku
        self.key = key
        self.value = value


class CLIKeyError(KeyError):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    def __init__(self, key: str, defaults: list[str]):
        # Inicializace základní výjimky
        message = f"Byl zadán neplatný klíč: '{key}'."
        super().__init__(message)

        # Načtení informací o klíči pro detail a hint
        info = key_hint.get(key, {})
        self.extra = {
            "detail": f"Zde je seznam povolených klíčů: \n{defaults}",
            "hint": f"Pro zobrazení seznamu klíčů i s popisem a nápovědou zadej v terminálu: \n"
                    f"$ log-this-config --help -key"
        }

        # Nastavení extra atributu pro výjimku
        self.key = key
        self.value = value


class ValidateKeyAndValueMixin:


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
        if key not in key_hint:
            raise CLIKeyError(key, list(key_hint.keys()))

        # Načtení dat ze slovníku
        key_data = key_hint[key]
        validate_func = key_data.get("validate", None)

        # validace hodnoty pro daný klíč
        if not validate_func(value):
            raise CLIValueError(key, value, key_data)

