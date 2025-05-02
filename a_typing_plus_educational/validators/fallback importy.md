Výborná otázka, Dalibore! 😊  
Pojďme to rovnou pěkně rozebrat:

---

### 📚 Obecně k fallbackům u typových anotací

Ano, **existuje několik typových anotací**, které se **přidávaly postupně** do `typing`, a pokud chceš být kompatibilní i se starším Pythonem (hlavně 3.7–3.9), **někdy je potřeba dělat podobný fallback** jako u `Never`.

**Ale** —  
👉 **není jich moc**.  
👉 **nejčastěji** jde o **novější nebo méně používané typy**.

---

### 🧩 Typy, které si často vyžadují fallback/import opatrnosti

| Typ | Přidán v | Poznámka |
|:----|:---------|:---------|
| `Literal` | 3.8 | Starší Python nemá → fallback `typing_extensions` |
| `Final` | 3.8 | Stejné jako `Literal` |
| `TypedDict` | 3.8 | Stejné, často fallback přes `typing_extensions` |
| `Protocol` | 3.8 | Stejné |
| `Annotated` | 3.9 | Fallback v `typing_extensions` |
| `NotRequired`, `Required` | 3.11 | Nové v `typing` (předtím jen `typing_extensions`) |
| `Self` | 3.11 | Čistě nová v 3.11, jinak `typing_extensions` |
| `Never` | 3.11 | Přidáno v 3.11 (`typing`), dříve fallback |
| `Unpack`, `TypeVarTuple` | 3.11 | Hlubší typing, fallback v `typing_extensions` |

---

### ✨ Shrnutí

- **Běžné základní typy** (`List`, `Dict`, `Union`, `Optional`, `Any`, `Tuple`, `Callable` atd.) — **nepotřebují fallback** — jsou už od Pythonu 3.5–3.6.
- **Speciální nové typy** (zejména kolem **structural typingu**, **literálů**, **protokolů**) — tam fallbacky **někdy** potřeba jsou.
- **Celkově jich ale není mnoho** — pokud bys měl dělat plnou podporu od 3.7/3.8 výš, tak stačí fallback pro cca **5–8 typů**.
- **Když cílíš na 3.10+**, **nemusíš fallbacky řešit vůbec** kromě opravdu exotických případů.

---

### 🛡️ Doporučení podle situace

- **Chci 100% podporu 3.7+** → fallbacky na pár typů (`Literal`, `TypedDict`, `Final`, `Protocol`, `Annotated`).
- **Chci podporu 3.10+** → **prakticky nic fallbackovat nemusíš**. Můžeš psát čistě.

---

### 📦 Bonus: fallback moderně přes `typing_extensions`

Když bys chtěl fallback "čistěji", tak se používá vzor:

```python
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
```

nebo pokud chceš rovnou být moderní:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal  # for static analyzers
else:
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal
```

(Tento vzor se ale používá spíš v knihovnách, které hodně pečují o 100% statické analýzy.)

---

### 🔥 Mini shrnutí na konec

- **Ne**, není toho moc, jen pár specifických typů.
- **Pokud chceš být klidný a jednoduchý** — fallback řeš jen tam, kde už víš, že to dává smysl (`Never`, `Literal`, `TypedDict`, apod.).
- **Pokud cílíš moderně**, fakt to ani moc řešit nemusíš.

---

Chceš, že ti ještě sepíšu **úplný mini-seznam fallback typů**, co by stálo za to podporovat v takové knihovně jako tvoříš? 🚀 (byl by to super "checklist" třeba před releasem)  
Stačí říct! 🎯