"""
### 📂 `b_binary_types`

**Popis**:
Tato skupina obsahuje validátory pro **binární typy** – tedy typy pracující s _binárními daty_ (např. bajty), často používané při práci se soubory, binární komunikací, síťovými protokoly atd.

---

#### ✅ Obsah složky:

| Soubor | Zhodnocení |
|--------|------------|
| `bytearray.py` | ✅ Ano – mutable bajtové pole. |
| `bytes.py` | ✅ Ano – immutable bajtové pole. |
| `memoryview.py` | ✅ Ano – speciální binární typ umožňující přístup k paměťovým bufferům. |

"""
from .bytearray import ByteArrayValidator
from .bytes import BytesValidator
from .memoryview import MemoryViewValidator


__all__ = [
    "ByteArrayValidator",
    "BytesValidator",
    "MemoryViewValidator",
]
