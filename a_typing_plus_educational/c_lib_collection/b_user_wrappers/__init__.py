"""
### 📂 `d_collections_lib_types`

**Popis**:
Skupina obsahuje konkrétní implementace (ne abstrakce/ABC) z knihovny `collections` a `collections.abc`, které se *da(jí)* použít jako vstupní anotace – tedy validovat konkrétní instanci nějakého složitějšího typu.

---

#### ✅ Obsah složky:

| Soubor | Zhodnocení |
|--------|------------|
| `user_dict.py` | ✅ Správně – `collections.UserDict`. |
| `user_list.py` | ✅ Správně – `collections.UserList`. |
| `user_string.py` | ✅ Správně – `collections.UserStr`. |


"""
from .user_dict import UserDictValidator
from .user_list import UserListValidator
from .user_string import UserStringValidator

__all__ = [
    "UserDictValidator",
    "UserListValidator",
    "UserStringValidator",

]
