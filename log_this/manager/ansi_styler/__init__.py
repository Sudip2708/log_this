print("log_this/manager/ansi_styler/__init__.py")
from log_this.manager.ansi_styler.ansi_formatter import ANSIFormatter, style, color, cli_format

__all__ = [
    "ANSIFormatter",  # Hlavní třída pro ANSI formátování testu
    "style",  # Instance třídy pro explicitní zápis: style("string").set("red")
    "color",  # Metoda pro definici vlastní barvy, či schématu
    "cli_format",  # Nastavení pro cli
]

if __name__ == "__main__":
    # Testovací vstupy
    vstup1 = "Toto je text."
    vstup2 = "Toto je \033[1;31mčervený text\033[0m a další část."
    vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."
    print("aaa_init")
    print(style(vstup1).set(31, 1))
    print(style(vstup2).set("bold", "34"))
    print(style(vstup3).set("4", "35"))
    print("bbb_init")