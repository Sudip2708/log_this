# cli_styler/settings/_formatting.py
"""
Definice pomocných formátovacích značek.
(použití přes tyto definice je čistě estetickou záležitostí)
"""
EMPTY_LINE   = "\n"   # Odskok na další řádek (vhodné pro vytváření mezer)
END_LINE     = " \n"  # Ukončení řádku s mezerou (vhodné pro menu)
# (Vhodné pro víceřádkové texty které jsou předávány jako řetězec - metoda get - a u kterých cheme aby byl každý na vlastním řádku)
CONTINUE     = ""     # Neukončení řádku (Vhodné pro víceřádkové popisy)
# (Vhodné pro jednořádkové printy u kterých nechceme aby se pod nima zobrazila mezera)