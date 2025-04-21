### **Základní návrh jazyka inspirovaného přirozenou řečí**  

Pojďme nejdříve definovat **klíčové principy**, podle kterých budeme stavět.  
Tento jazyk budeme nazývat pracovně **"Přirozený kód"** (můžeme změnit později).

---

## **1. Principy jazyka**  

1. **Každý řádek je věta, která vykonává akci.**  
   - **Věty končí tečkou (`.`).**  
   - **Věty začínají velkým písmenem (není nutné pro stroj, ale pomáhá čitelnosti).**  
   - **Dvojtečka (`:`) vytváří nový blok.**  

2. **Objekty se definují přirozeně pomocí dvojtečky.**  
   - **Např.:** `Auto: Barva je červená.`  

3. **Instrukce jsou psány jako přirozené věty.**  
   - `Vypiš "Ahoj světe".` místo `print("Ahoj světe")`  

4. **Podmínky a cykly odpovídají lidské logice.**  
   - `Pokud číslo je větší než 10: Vypiš "Číslo je velké".`  
   - `Opakuj 5krát: Vypiš "Opakování".`  

5. **Všechna data jsou reprezentována v jednotné tabulkové struktuře.**  
   - Čísla, texty, seznamy a další struktury jsou uloženy stejným způsobem.  
   - Efektivní binární reprezentace na nízké úrovni.  

---

## **2. Základní syntaxe**  

### **2.1. Výpis hodnot**  
```plaintext
Vypiš "Ahoj světe".
```
➡️ Výsledek: `Ahoj světe`

### **2.2. Proměnné a výpočty**  
```plaintext
Číslo první je 5.
Číslo druhé je 10.
Výsledek je první plus druhé.
Vypiš výsledek.
```
➡️ Výsledek: `15`

### **2.3. Podmínky**  
```plaintext
Pokud výsledek je větší než 10:  
    Vypiš "Číslo je velké".
Jinak:  
    Vypiš "Číslo je malé".
```
➡️ Výsledek: `Číslo je velké`

### **2.4. Cykly**  
```plaintext
Opakuj 5krát:  
    Vypiš "Opakování".
```
➡️ Výsledek:  
```
Opakování  
Opakování  
Opakování  
Opakování  
Opakování  
```

### **2.5. Funkce**  
```plaintext
Sečti dvě čísla:  
    Výsledek je první plus druhé.  
    Vrať výsledek.

Vypiš Sečti 3 a 7.
```
➡️ Výsledek: `10`

### **2.6. Objekty**  
```plaintext
Auto:  
    Barva je červená.  
    Rychlost je 120.

Vypiš Auto.Barva.
```
➡️ Výsledek: `červená`

---

## **3. Jak by mohl vypadat překladač?**  

✅ **Lexikální analýza**: Rozpoznává klíčová slova (`Vypiš`, `Pokud`, `Opakuj`...)  
✅ **Syntaktická analýza**: Převádí věty do vnitřní struktury.  
✅ **Interpretace nebo kompilace**: Překládá do binární formy nebo existujícího jazyka.  

---

## **4. Další rozšíření**  
✅ Práce s textem a čísly je intuitivní.  
✅ Možnost definovat složitější struktury (seznamy, slovníky).  
✅ Podpora paralelního zpracování přirozeným způsobem.  

---

## **Co dál?**  
Můžeme:  
1. **Navrhnout formát pro tabulkovou reprezentaci dat.**  
2. **Vytvořit základní interpreter pro testování.**  
3. **Rozšířit syntax o složitější koncepty.**  

Co myslíš? Mám se pustit do konkrétní implementace základního překladače, nebo chceš ještě vyladit koncept?