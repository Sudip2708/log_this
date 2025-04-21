"""
### 📂 `c_standard_collection`

**Popis**:
Obsahuje validátory pro klasické vestavěné kolekce v Pythonu, které přijímají jiné hodnoty – tedy složené typy jako seznamy, slovníky, množiny apod.

---

#### ✅ Obsah složky:

| Soubor | Zhodnocení |
|--------|------------|
| `dict.py` | ✅ Ano – vestavěný asociativní kontejner. |
| `frozen_set.py` | ✅ Ano – immutable množina. |
| `list.py` | ✅ Ano – mutable sekvence. |
| `set.py` | ✅ Ano – mutable množina. |
| `tuple.py` | ✅ Ano – immutable sekvence, podporuje heterogenní typy. |


"""
from .dict import DictValidator
from .frozen_set import FrozenSetValidator
from .list import ListValidator
from .set import SetValidator
from .tuple import TupleValidator


__all__ = [
    "DictValidator",
    "FrozenSetValidator",
    "ListValidator",
    "SetValidator",
    "TupleValidator",
]
