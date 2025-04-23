"""
### 📂 `d_collections_lib_types`

**Popis**:
Skupina obsahuje konkrétní implementace (ne abstrakce/ABC) z knihovny `collections` a `collections.abc`, které se *da(jí)* použít jako vstupní anotace – tedy validovat konkrétní instanci nějakého složitějšího typu.

---

#### ✅ Obsah složky:

| Soubor | Zhodnocení |
|--------|------------|
| `chain_map.py` | ✅ Správně – `collections.ChainMap`. |
| `counter.py` | ✅ Správně – `collections.Counter`. |
| `default_dict.py` | ✅ Správně – `collections.defaultdict`. |
| `deque.py` | ✅ Správně – `collections.deque`. |
| `ordered_dict.py` | ✅ Správně – `collections.OrderedDict` (od Pythonu 3.7 je dict ordered, ale pořád má smysl pro explicitnost a starší verze). |


"""
from .chain_map import ChainMapValidator
from .counter import CounterValidator
from .default_dict import DefaultDictValidator
from .deque import DequeValidator
from .ordered_dict import OrderedDictValidator


__all__ = [
    "ChainMapValidator",
    "CounterValidator",
    "DefaultDictValidator",
    "DequeValidator",
    "OrderedDictValidator",
]
