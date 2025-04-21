### **Fáze 1: Vytvoření logické struktury jazyka (běžící nad Pythonem)**  

Tento proces by měl **5 hlavních kroků**, které na sebe logicky navazují.  

---

### **1️⃣ Definice syntaxe jazyka**  
✅ **Cíl:** Vytvořit základní pravidla jazyka, která budou **čitelné, intuitivní a snadno parsovatelné**.  

🔹 **Postup:**  
- Určit, jak budou vypadat základní příkazy:  
  - Definice proměnných (`Set X to 10.`)  
  - Operace (`Add X and Y, store in Z.`)  
  - Řídící struktury (`If X is greater than Y, do something.`)  
  - Definice funkcí (`Define a function called "Multiply" that takes X and Y.`)  
- Určit, zda bude jazyk **case-sensitive** nebo ne.  
- Rozhodnout, jestli bude mít pevnou gramatiku nebo bude podporovat přirozenější věty.  

➡ **Výstup:** Návrh základní syntaxe jazyka.  

---

### **2️⃣ Implementace lexikálního analyzátoru (Tokenizace)**  
✅ **Cíl:** Vytvořit část programu, která rozloží text na **tokeny (slovní jednotky jazyka)**.  

🔹 **Postup:**  
- Napsat tokenizér, který převede větu na sadu tokenů:  
  ```  
  "Set X to 10."  
  ```  
  ➡ Se rozloží na:  
  ```json
  ["SET", "VAR:X", "EQUALS", "NUMBER:10"]
  ```
- Použít knihovnu **re (regular expressions)** pro rozpoznávání klíčových slov.  
- Testovat lexikální analýzu na jednoduchých větách.  

➡ **Výstup:** Tokenizér, který převede textový vstup do strukturované formy.  

---

### **3️⃣ Implementace syntaktického analyzátoru (Parser)**  
✅ **Cíl:** Vytvořit parser, který ověří správnost syntaxe a převede tokeny na **strukturu odpovídající programu**.  

🔹 **Postup:**  
- Použít knihovnu jako **Lark nebo PLY** pro sestavení parseru.  
- Vytvořit **AST (Abstract Syntax Tree)** – stromovou reprezentaci programu.  
- Například věta:  
  ```
  Set X to 10.
  ```
  ➡ Přeloží se na:  
  ```json
  {
    "type": "assignment",
    "variable": "X",
    "value": 10
  }
  ```
- Zajistit podporu pro řídící struktury (`if`, `while`, `for`).  

➡ **Výstup:** Parser, který převede tokeny na **stromovou reprezentaci programu**.  

---

### **4️⃣ Překlad AST na Python kód**  
✅ **Cíl:** Implementovat překladač, který vezme **AST** a vygeneruje **Python kód**.  

🔹 **Postup:**  
- Každý uzel AST odpovídá Python konstrukci:  
  ```json
  {
    "type": "assignment",
    "variable": "X",
    "value": 10
  }
  ```
  ➡ Přeloží se na:  
  ```python
  X = 10
  ```
- Použít rekurzivní metodu, která vygeneruje Python kód pro celý program.  
- Otestovat na několika příkazech a ověřit správnost výstupu.  

➡ **Výstup:** Překladač, který převede stromovou reprezentaci na spustitelný Python kód.  

---

### **5️⃣ Spuštění vygenerovaného Python kódu**  
✅ **Cíl:** Umožnit uživateli napsat kód v novém jazyce a **automaticky ho spustit**.  

🔹 **Postup:**  
- Po překladu do Pythonu **automaticky zavolat exec()** nebo uložit do `.py` souboru a spustit.  
- Umožnit spuštění **přímo z příkazové řádky**:  
  ```
  mylang run program.mylang
  ```
- Přidat ladící výstupy pro sledování průběhu překladu.  

➡ **Výstup:** Funkční běhové prostředí, kde lze spouštět kód napsaný v novém jazyce.  

---

### **Shrnutí celého procesu**  
1️⃣ **Definujeme syntax jazyka** (Jak budou vypadat příkazy?)  
2️⃣ **Vytvoříme lexikální analyzátor** (Rozloží text na tokeny)  
3️⃣ **Vytvoříme syntaktický analyzátor** (Ověří strukturu programu)  
4️⃣ **Napíšeme překladač do Pythonu** (Převede AST na spustitelný kód)  
5️⃣ **Spustíme vygenerovaný Python kód** (Umožníme program běžet)  

---

### **Kolik času by to zabralo?**  
🔹 **Základní prototyp** (jen jednoduché příkazy) → **2–3 týdny**.  
🔹 **Rozšířený prototyp** (s podporou funkcí a podmínek) → **měsíc**.  
🔹 **První veřejná verze** (s lepším chybovým hlášením) → **2–3 měsíce**.  

➡ Po této fázi bychom měli funkční jazyk **běžící nad Pythonem**, který bychom mohli začít **překládat do assembleru nebo binárního kódu** v další fázi.