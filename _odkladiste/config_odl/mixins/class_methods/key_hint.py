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

# Metody pro validaci
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


