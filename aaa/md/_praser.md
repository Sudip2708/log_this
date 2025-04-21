Super! Pojďme na to. První krok bude vytvořit **jednoduchý parser**, který dokáže přečíst základní příkazy v přirozeném jazyce a přeložit je do Pythonu.  

---

## **🟢 Krok 1: Parser – překládání přirozeného textu na Python**  
**Cíl:** Napíšeme program, který vezme větu jako **"Set X to 10."** a převede ji na Pythonový kód **`x = 10`**.

**🔹 Začneme s jednoduchým slovníkem klíčových slov:**
- **"Set X to 10."** ⟶ `x = 10`
- **"Add X and 5, store in Y."** ⟶ `y = x + 5`
- **"If X is greater than 10, print Hello."** ⟶ `if x > 10: print("Hello")`

Nejdřív napíšeme **funkci, která rozpozná klíčová slova a převede věty na Python kód**.

---

### **📝 Kód pro základní parser:**
```python
import re

def parse_command(command):
    """Převede příkaz v přirozeném jazyce na Python kód."""
    
    command = command.strip().lower()
    
    # Přiřazení hodnoty: "Set X to 10."
    match = re.match(r"set (\w+) to (\d+)", command)
    if match:
        var, value = match.groups()
        return f"{var} = {value}"
    
    # Sčítání: "Add X and 5, store in Y."
    match = re.match(r"add (\w+) and (\d+), store in (\w+)", command)
    if match:
        var1, num, var2 = match.groups()
        return f"{var2} = {var1} + {num}"
    
    # Podmínka: "If X is greater than 10, print Hello."
    match = re.match(r"if (\w+) is greater than (\d+), print (.+)", command)
    if match:
        var, num, text = match.groups()
        return f'if {var} > {num}: print("{text}")'
    
    return "Unknown command"

# TESTOVÁNÍ:
commands = [
    "Set X to 10.",
    "Add X and 5, store in Y.",
    "If X is greater than 10, print Hello."
]

for cmd in commands:
    print(f"Natural: {cmd}")
    print(f"Python: {parse_command(cmd)}\n")
```
---

## **🔵 Krok 2: Vykonání přeloženého kódu**
Nyní máme **parser**, který text převádí na Python kód. Teď ho můžeme rovnou vykonat pomocí funkce `exec()`.

```python
code = parse_command("Set X to 10.")
exec(code)
print(x)  # Očekáváme výstup: 10
```

---

## **🟠 Krok 3: Přidání dalších příkazů**
Teď můžeme postupně přidat:
- **Podporu dalších operací** (odčítání, násobení, dělení).
- **Smyčky** (`while`, `for`).
- **Podmínky** (`if-else`).
- **Funkce** (`Define function Add with parameters A and B. Return A plus B.`).

Než se pustíme dál, **chceš si nejdřív vyzkoušet, jestli ti tenhle parser funguje?** Ať si ověříme, že jsme na správné cestě.