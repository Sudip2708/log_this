# Log This 🛠️

**Log This** je jednoduchá a přizpůsobitelná Python knihovna pro logování funkcí a metod.  
Hlavní myšlenkou je zjednodušit proces logování během vývoje. 
Knihovna poskytuje tři přednastavené módy a snadné ovládání pomocí dekorátoru.

---

## 📖 Obsah

- [Ukázka použití](#-ukázka-použití)
- [Instalace](#-instalace)
- [Módy logování](#-módy-logování)
- [Požadavky](#-požadavky)
- [Testování](#-testování)
- [Licence](#-licence)
- [Kontakt](#-kontakt)

---

## 🚀 Ukázka použití

```python
from log_this import log_this

@log_this("simple")
def example_function(x, y):
    return x + y
```

### Výstup:
```plaintext
# START LogThis('simple') pro funkci 'example_function' | 2024-12-09 13:48:36.398274 |
# >>> Vstupní argumenty: [10, 20]
# >>> Výsledek: 30
# END LogThis('simple') | Doba běhu: 0.001 sec
```

---

## 🛠 Instalace

1. Klonujte repozitář nebo stáhněte zip:
   ```bash
   git clone https://github.com/Sudip2708/log_this.git
   cd log_this
   ```

2. Nainstalujte pomocí `pip`:
   ```bash
   pip install .
   ```

---

## 📋 Módy logování

1. **Přeskočení logování**:  
   ```python
   @log_this("skip_this")
   ```

2. **Stručný výpis**:  
   ```python
   @log_this("one_line")
   ```

3. **Obsáhlejší výpis** *(výchozí)*:  
   ```python
   @log_this("simple")
   ```

4. **Úplný výpis**:  
   ```python
   @log_this("all")
   ```

Další informace najdete v [podrobném popisu módů](about_data/mode_descriptions/mode_simple.md).

---

## 🔧 Požadavky

- Python 3.6+
- Standardní Python knihovny: `logging`, `functools`, `inspect`, `time`.

---

## ✅ Testování

1. Ujistěte se, že máte nainstalovány závislosti:
   ```bash
   pip install -r requirements.txt
   ```

2. Spusťte testy pomocí `pytest`:
   ```bash
   pytest
   ```

---

## 📜 Licence

Tato knihovna je volně k použití pod licencí **MIT**. Můžete ji upravovat a distribuovat dle potřeby.

---

## 📞 Kontakt

Autor: **Dalibor Sova**  
Email: [daliborsova@seznam.cz](mailto:daliborsova@seznam.cz)  
GitHub: [Sudip2708](https://github.com/Sudip2708)

---
