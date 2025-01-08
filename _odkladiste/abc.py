import re

# def obal_neformatovane(retezec, nova_sekvence="\033[34m"):  # Zelená jako příklad
#     casti = re.split(r"(\033\[.*?m)", retezec)
#     vysledek = ""
#     obalovat = True  # Příznak, zda se má aktuální část obalovat
#     for cast in casti:
#         if cast.startswith("\033["):
#             vysledek += cast
#             obalovat = True # Po formátovací sekvenci se zase obaluje
#         elif cast:  # Neobalovat prázdné řetězce
#             if obalovat:
#                 vysledek += nova_sekvence + cast + "\033[0m"
#                 obalovat = False # Po obalení se už neobaluje do další formátovací sekvence dokud nenarazíme na jinou
#             else:
#                 vysledek += cast
#     return vysledek

# Testovací příklady
retezec1 = "Toto je \033[31mčervený\033[0m text."
retezec2 = "Začátek \033[31mčervený\033[0m uprostřed a konec."
retezec3 = "Jenom text bez formátování."
retezec4 = "\033[31mčervený\033[0m\033[32mzelený\033[0m"

# print(obal_neformatovane(retezec1))
# print(obal_neformatovane(retezec2))
# print(obal_neformatovane(retezec3))
# print(obal_neformatovane(retezec4))


import re

def obal_neformatovane_robustne(retezec, nova_sekvence="\033[34m"):
    vysledek = ""
    posledni_konec = 0
    for match in re.finditer(r"\033\[.*?m", retezec):
        start, end = match.span()
        if start > posledni_konec:
            # Přidáme neformátovaný text pouze s novou sekvencí
            neformatovany = retezec[posledni_konec:start]
            vysledek += f"{nova_sekvence}{neformatovany}\033[0m"
        # Přidáme aktuální formátovací sekvenci beze změny
        vysledek += match.group(0)
        posledni_konec = end
    if posledni_konec < len(retezec):
        # Přidáme zbývající neformátovaný text
        neformatovany = retezec[posledni_konec:]
        vysledek += f"{nova_sekvence}{neformatovany}\033[0m"
    return vysledek


# Testovací příklady (včetně vnořených sekvencí)
retezec5 = "Toto je \033[31m\033[4mčervený podtržený\033[0m\033[0m text."
retezec6 = "\033[31mprvní\033[0m test \033[32mdruhý\033[0m test"

print(obal_neformatovane_robustne(retezec1))
print(obal_neformatovane_robustne(retezec2))
print(obal_neformatovane_robustne(retezec3))
print(obal_neformatovane_robustne(retezec4))
print(repr(obal_neformatovane_robustne(retezec5)))
print(obal_neformatovane_robustne(retezec6))
print('\x1b[34mToto je \x1b[0m\x1b[31m\x1b[4mčervený podtržený\x1b[0m\x1b[0m\x1b[34m text.\x1b[0m'
)