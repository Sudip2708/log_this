from ansi_formatter import ANSIFormatter, style, st

__all__ = [
    "ANSIFormatter",  # Hlavní třída pro ANSI formátování testu
    "style",  # Instance třídy pro explicitní zápis: style("string").set("red")
    "st",  # Instance třídy pro zkrácený zápis: st("string").s(31)
]