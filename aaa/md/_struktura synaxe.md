Přesně tak, klíčové je nejdřív vyřešit **jednoznačnost příkazů** a až potom ladit estetiku a zkracování zápisu. Takže by to chtělo stanovit **jasná pravidla syntaxe**, která:  

1. **Eliminují dvojsmyslnost** – každý příkaz by měl mít jen jeden význam.  
2. **Mají přirozenou strukturu** – aby lidé mohli programovat běžnou řečí.  
3. **Jsou konzistentní** – stejný vzorec zápisu pro všechny objekty a operace.  

---

## **📝 První návrh základní syntaxe příkazů**
Zkusím navrhnout pár základních pravidel, která by mohla pomoct vytvořit **jasný systém mluvených příkazů**:  

### **1️⃣ Deklarace objektů**
- **Mluveně**: *Vytvoř objekt auto. Objekt očekává parametry rychlost a barva.*  
- **Jasná struktura**:  
  - **Vytvoř objekt [název]** → definuje nový objekt.  
  - **Objekt očekává parametry [seznam]** → definuje atributy objektu.  
- **Alternativní zápis**: *Vytvoř objekt auto s parametry rychlost, barva.*  

### **2️⃣ Dědičnost (propojování objektů)**
- **Mluveně**: *Vytvoř objekt závodní auto. Závodní auto je typem auta a má turbo.*  
- **Jasná struktura**:  
  - **[Objekt] je typem [jiný objekt]** → Dědí vlastnosti.  
  - **Má [další vlastnost]** → Přidává nové atributy.  
- **Alternativní zápis**: *Závodní auto je auto s turbem.*  

### **3️⃣ Podmínky (logické operace)**
- **Mluveně**: *Pokud rychlost auta je větší než 100, vypiš "rychlé auto". Jinak vypiš "pomalé auto".*  
- **Jasná struktura**:  
  - **Pokud [podmínka], udělej [akce]**.  
  - **Jinak udělej [akce]** → volitelná větev.  
- **Alternativní zápis**: *Pokud auto.rychlost > 100, vypiš "rychlé auto". Jinak "pomalé auto".*  

### **4️⃣ Cykly (opakování instrukcí)**
- **Mluveně**: *Opakuj 5krát: vypiš "Ahoj".*  
- **Jasná struktura**:  
  - **Opakuj [počet]krát: [akce]**  
- **Alternativní zápis**: *Opakuj 5×: vypiš "Ahoj".*  

### **5️⃣ Akce a metody**
- **Mluveně**: *Auto nastav rychlost na 80.*  
- **Jasná struktura**:  
  - **[Objekt] [akce] [hodnota]**  
- **Alternativní zápis**: *Auto.rychlost = 80.*  

---

## **📌 Další kroky**
1. **Upevnit pravidla syntaxe** – najít hraniční případy, kde by mohla vzniknout dvojsmyslnost.  
2. **Rozšířit pokrytí** – vytvořit pravidla i pro složitější operace (např. vstupy, výstupy, pole, soubory).  
3. **První testovací parser** – jednoduchý program, který přečte větu a převede ji do struktury (např. Python AST).  

Co na to říkáš? Chtěl bys něco přidat, nebo máš nějaké konkrétní případy, kde by mohla být nejasnost?