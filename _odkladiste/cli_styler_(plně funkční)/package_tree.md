# Hlavní balíček knihovny
cli_styler  # Knihovna slouží pro stylování textů určených pro výstup do konzole
cli_styler/__init__.py  # Definice výstupních metod balíčku
cli_styler/cli_styler.py  # Definice třídy CLIStyler obsahující atributy jednotlivých stylů
cli_styler/how_to_add_style.md  # Návod jak přidávat nové styly
cli_styler/output.py  # Definice výstupních metod balíčku
cli_styler/tree.md  # Soubor popisující jednotlivé soubory (tento soubor)

# Balíček obsahující definice konstant
cli_styler/constants  # Balíček slouží k definici konstant které jsou dále v knihovně použity k definici stylů
cli_styler/constants/__init__.py  # Registrace stylů pro zpřístupnění prostřednictvým balíčku
cli_styler/constants/_colors.py  # Nastavení barev použitých ve stylech ["#hex_str_light", "#hex_str_dark"]
cli_styler/constants/_ends.py  # Nastavení potřebná pro ukončení řádků
cli_styler/constants/_styles.py  # Nastavení pro doplňující styly pro formátování textu
cli_styler/constants/_symbols.py  # Nastavení znakových sad používaných na začátku řádků [" - ", " - "]

# Balíček obsahující mixiny pro třídu CLIStyler
cli_styler/mixins  # Balíček s mixiny pro hlavní třídu CLIStyler
cli_styler/mixins/__init__.py  # Registrace mixinú pro zpřístupnění prostřednictvým balíčku
cli_styler/mixins/_apply_styles_to_attributes.py  # Mixin obsahující logiku pro aplykaci a reaplikaci stylů
cli_styler/mixins/_check_style_attributes.py  # Mixin obsahující logiku pro kontrolu hodnot konfiguračního slovníku a atributů
cli_styler/mixins/_get_current_ids.py  # Mixin obsahující logiku pro správu barevného modu a setu značek
cli_styler/mixins/_set_colors_mode.py  # Mixin obsahující logiku pro logiku pro změnu barevného modu
cli_styler/mixins/_set_sign_set.py  # Mixin obsahující logiku pro logiku pro změnu setu značek

# Balíček obsahující ošetření výjimek pro mixiny
cli_styler/mixins/exceptions  # Balíček s výjimkami pro mixiny hlavní třídy CLIStyler
cli_styler/mixins/exceptions/__init__.py  # Registrace výjimek pro zpřístupnění prostřednictvým balíčku
cli_styler/mixins/exceptions/_raise_attributes_error.py  # Definice výjimky pro případ, že obsah konfiguračního slovníku neodpovídá atributů

# Balíček obsahující definici třídy StyleClass
cli_styler/style_class  # Balíček pro třídu StyleClass pro vytváření instancí stylů
cli_styler/style_class/__init__.py  # Zpřístupnění třídy StyleClass prostřednictvým balíčku
cli_styler/style_class/_style_class.py  # Definice třídy StyleClass pro vytváření instancí stylů

# Balíček obsahující mixiny pro třídu StyleClass
cli_styler/style_class/mixins  # Balíček s mixiny pro třídu StyleClass pro vytváření instancí stylů
cli_styler/style_class/mixins/__init__.py  # Registrace mixinú pro zpřístupnění prostřednictvým balíčku
cli_styler/style_class/mixins/_style_get.py  # Definice metody pro získání tuple (styl, text)
cli_styler/style_class/mixins/_style_print.py  # Definice metody pro vytištění ostylovaného textu

# Balíček obsahující definice nastavení stylů
cli_styler/styles_settings  # Balíček obsahující definice stylů a hlavního přístupového slovníku STYLES_DICT
cli_styler/styles_settings/__init__.py  # Zpřístupnění slovníku STYLES_DICT prostřednictvým balíčku
cli_styler/styles_settings/_error.py  # Definice stylů pro chybové oznamy
cli_styler/styles_settings/_hint.py  # Definice stylů pro nápovědu k ovládání interaktivníhorežimu
cli_styler/styles_settings/_info.py  # Definice stylů pro informativní oznamy
cli_styler/styles_settings/_intro.py  # Definice stylů pro úvod a ukončení interaktivního režimu
cli_styler/styles_settings/_menu.py  # Definice stylů pro interaktivní menu
cli_styler/styles_settings/_prompt.py  # Definice stylů pro dialog uživateského vstupu
cli_styler/styles_settings/_success.py  # Definice stylů pro oznam o úspěšném provedení
cli_styler/styles_settings/_warning.py  # Definice stylů pro earovné oznamy a upozornění
cli_styler/styles_settings/styles_dict.py  # Definice hlavního přístupového slovníku STYLES_DICT předávající veškeré styly



### Hlavní balíček knihovny

cli_styler 
# Knihovna slouží pro stylování textů určených pro výstup do konzole

cli_styler/__init__.py  
# Definice výstupních metod balíčku

cli_styler/cli_styler.py  
# Definice třídy CLIStyler obsahující atributy jednotlivých stylů

cli_styler/how_to_add_style.md  
# Návod jak přidávat nové styly

cli_styler/output.py  
# Definice výstupních metod balíčku

cli_styler/tree.md  
# Soubor popisující jednotlivé soubory (tento soubor)



### Balíček obsahující definice konstant

cli_styler/constants  
# Balíček slouží k definici konstant které jsou dále v knihovně použity k definici stylů

cli_styler/constants/__init__.py  
# Registrace stylů pro zpřístupnění prostřednictvým balíčku

cli_styler/constants/_colors.py  
# Nastavení barev použitých ve stylech ["#hex_str_light", "#hex_str_dark"]

cli_styler/constants/_ends.py  
# Nastavení potřebná pro ukončení řádků

cli_styler/constants/_styles.py  
# Nastavení pro doplňující styly pro formátování textu

cli_styler/constants/_symbols.py  
# Nastavení znakových sad používaných na začátku řádků [" - ", " - "]



### Balíček obsahující mixiny pro třídu CLIStyler

cli_styler/mixins  
# Balíček s mixiny pro hlavní třídu CLIStyler

cli_styler/mixins/__init__.py  
# Registrace mixinú pro zpřístupnění prostřednictvým balíčku

cli_styler/mixins/_apply_styles_to_attributes.py  
# Mixin obsahující logiku pro aplykaci a reaplikaci stylů

cli_styler/mixins/_check_style_attributes.py  
# Mixin obsahující logiku pro kontrolu hodnot konfiguračního slovníku a atributů

cli_styler/mixins/_get_current_ids.py  
# Mixin obsahující logiku pro správu barevného modu a setu značek

cli_styler/mixins/_set_colors_mode.py  
# Mixin obsahující logiku pro logiku pro změnu barevného modu

cli_styler/mixins/_set_sign_set.py  
# Mixin obsahující logiku pro logiku pro změnu setu značek



### Balíček obsahující ošetření výjimek pro mixiny

cli_styler/mixins/exceptions  
# Balíček s výjimkami pro mixiny hlavní třídy CLIStyler

cli_styler/mixins/exceptions/__init__.py  
# Registrace výjimek pro zpřístupnění prostřednictvým balíčku

cli_styler/mixins/exceptions/_raise_attributes_error.py  
# Definice výjimky pro případ, že obsah konfiguračního slovníku neodpovídá atributů



### Balíček obsahující definici třídy StyleClass

cli_styler/style_class  
# Balíček pro třídu StyleClass pro vytváření instancí stylů

cli_styler/style_class/__init__.py  
# Zpřístupnění třídy StyleClass prostřednictvým balíčku

cli_styler/style_class/_style_class.py  
# Definice třídy StyleClass pro vytváření instancí stylů



### Balíček obsahující mixiny pro třídu StyleClass

cli_styler/style_class/mixins  
# Balíček s mixiny pro třídu StyleClass pro vytváření instancí stylů

cli_styler/style_class/mixins/__init__.py  
# Registrace mixinú pro zpřístupnění prostřednictvým balíčku

cli_styler/style_class/mixins/_style_get.py  
# Definice metody pro získání tuple (styl, text)

cli_styler/style_class/mixins/_style_print.py  
# Definice metody pro vytištění ostylovaného textu



### Balíček obsahující definice nastavení stylů

cli_styler/styles_settings  
# Balíček obsahující definice stylů a hlavního přístupového slovníku STYLES_DICT

cli_styler/styles_settings/__init__.py  
# Zpřístupnění slovníku STYLES_DICT prostřednictvým balíčku

cli_styler/styles_settings/_error.py  
# Definice stylů pro chybové oznamy

cli_styler/styles_settings/_hint.py  
# Definice stylů pro nápovědu k ovládání interaktivníhorežimu

cli_styler/styles_settings/_info.py  
# Definice stylů pro informativní oznamy

cli_styler/styles_settings/_intro.py  
# Definice stylů pro úvod a ukončení interaktivního režimu

cli_styler/styles_settings/_menu.py  
# Definice stylů pro interaktivní menu

cli_styler/styles_settings/_prompt.py  
# Definice stylů pro dialog uživateského vstupu

cli_styler/styles_settings/_success.py  
# Definice stylů pro oznam o úspěšném provedení

cli_styler/styles_settings/_warning.py  
# Definice stylů pro earovné oznamy a upozornění

cli_styler/styles_settings/styles_dict.py  
# Definice hlavního přístupového slovníku STYLES_DICT předávající veškeré styly