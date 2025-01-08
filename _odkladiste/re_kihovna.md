### **1. Co je knihovna `re` a k čemu slouží?**

Knihovna **`re`** je součástí standardní knihovny Pythonu a poskytuje nástroje pro práci s **regulárními výrazy (regular expressions)**. Regulární výrazy jsou mocný nástroj pro hledání, porovnávání nebo manipulaci s textem na základě vzorů.

- **Kdo vytvořil `re`?**  
  Regulární výrazy jako koncept pocházejí od matematiků, například Stephena Kleeneho (v 50. letech). Knihovnu `re` vytvořili vývojáři Pythonu, aby poskytli nástroje pro práci s textovými vzory. První implementace byla inspirována Perl regex syntaxí.

- **Účel knihovny `re`:**  
  - Hledání specifických vzorů v textu.  
  - Nahrazování částí textu.  
  - Rozdělování textu podle vzorů.  
  - Extrahování podřetězců, které odpovídají vzoru.

---

### **2. Syntaxe knihovny `re`**

Nejprve načteme knihovnu pomocí:
```python
import re
```

**Hlavní funkce knihovny `re`:**

| Funkce         | Popis                                                                 |
|----------------|----------------------------------------------------------------------|
| `re.match`     | Hledá vzor na začátku řetězce.                                        |
| `re.search`    | Hledá první výskyt vzoru kdekoliv v řetězci.                          |
| `re.findall`   | Vrací všechny výskyty vzoru jako seznam.                              |
| `re.finditer`  | Vrací iterátor s výskyty vzoru jako objekty `Match`.                  |
| `re.sub`       | Nahrazuje výskyty vzoru jiným textem.                                 |
| `re.split`     | Rozděluje text podle vzoru.                                           |
| `re.compile`   | Kompiluje vzor pro opakované použití (zrychluje práci s regexy).       |

---

### **3. Základy regulárních výrazů**

Regulární výrazy popisují **vzor** textu. Některé základní symboly:

| Symbol       | Popis                                       |
|--------------|---------------------------------------------|
| `.`          | Jakýkoliv jeden znak (kromě nového řádku).  |
| `*`          | Opakuje předchozí znak 0 až nekonečněkrát. |
| `+`          | Opakuje předchozí znak 1 až nekonečněkrát. |
| `?`          | Opakuje předchozí znak 0 nebo 1 krát.      |
| `[]`         | Libovolný znak ze seznamu (např. `[abc]`). |
| `[^]`        | Libovolný znak **mimo** seznam.            |
| `{n}`        | Přesný počet opakování (např. `a{3}`).     |
| `|`          | Logické OR (např. `a|b`).                 |
| `()`         | Skupina (umožňuje zachytit části textu).   |
| `\d`         | Jakékoliv číslo (digit).                  |
| `\w`         | Jakýkoliv alfanumerický znak.             |
| `\s`         | Jakýkoliv bílý znak (mezera, tabulátor).  |

---

### **4. ESC sekvence `\033`**

Sekvence `\033` označuje znak **ESC** (escape), používaný k ovládání terminálu. ESC sekvence se často využívají k přidání formátování, jako je barva textu, pozadí, nebo resetování stylu.

- Například:  
  - `\033[31m` – nastaví text na červenou barvu.  
  - `\033[0m` – resetuje formátování.

V Pythonu můžeme ESC sekvence použít pro ovládání vzhledu výstupu v terminálu.

---

