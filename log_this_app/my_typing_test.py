import typing
from typing import get_origin

# # Získání všech názvů typů v `typing`
# typing_types = {name for name in dir(typing) if not name.startswith("_")}
# print(typing_types)

# print(dir(typing))
# help(typing)


# # Získání všech atributů z modulu typing
# typing_members = dir(typing)
# # Filtrování pouze těch, které nejsou privátní (nezačínají "__")
# typing_members = [name for name in typing_members if not name.startswith("__")]
# # Výpis všech názvů
# print(typing_members)

import typing

typing_types = {
    name: getattr(typing, name)
    for name in dir(typing)
    if not name.startswith("__")  # Odstraníme privátní atributy
    and isinstance(getattr(typing, name), (type, typing._SpecialForm))
}

# Výpis názvů všech dostupných typů
typing_items = typing_types.items()
print("value \t key \t get_origin(key) \t type(key) \t getattr(key, __module__)")
for key, value in typing_items:
    obj = typing_types[key]
    print(f"{key}\t{value}\t{type(obj)}\t{getattr(obj, '__module__', '')}")