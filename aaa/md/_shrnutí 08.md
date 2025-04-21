### **📝 Shrnutí konceptu dynamického objektového systému**  

Tvůj návrh **deklarativního systému** pro práci s objekty je postavený na **tabulkové struktuře** a **dynamických operacích**. Uživatel definuje, co chce udělat, a systém automaticky ověřuje kompatibilitu objektů.  

---

## **🔹 1) Základní principy**  
✅ **Vše je objekt** – Každá hodnota (číslo, text, seznam…) je reprezentovaná jako objekt se strukturou tabulky.  
✅ **Objekty se liší podle obsazených polí** – Např. číslo může mít:  
   - `hodnota = 1` → celé číslo  
   - `hodnota = 1, pozice desetinné čárky = -3` → desetinné číslo  
   - `hodnota = 1, počet nul před = 5` → formát jako text `00001`  
✅ **Tabulka je jen struktura** – Do každého pole lze vložit jiný objekt (interní či uživatelský).  
✅ **Objekty neobsahují zbytečnou zátěž** – Pouze pole, která definují jejich chování.  

---

## **🔹 2) Dynamické operace**  
✅ **Klíčová slova určují úkon** (např. `sečti`, `přidej`, `porovnej`)  
✅ **Systém ověřuje kompatibilitu objektů**  
✅ **Platné operace se provedou, neplatné vrátí chybu**  

### **🔸 Příklady operací**
✅ `Sečti objekt číslo 5 a objekt číslo 3.` → Výsledek: `8`  
✅ `Přidej objekt číslo 5 k objektu text "jablko".` → Výsledek: `"jablko5"`  
✅ `Porovnej objekt číslo 7 a objekt číslo 2 a zjisti, který je větší.` → Výsledek: `"7"`  
✅ `Sečti všechny objekty v seznamu.` → Výsledek: `součet všech číselných objektů`  

---

## **🔹 3) Výhody přístupu**  
✅ **Jasná syntaxe** – Uživatel definuje operaci slovně.  
✅ **Automatická kontrola typů** – Chyby se odhalí hned.  
✅ **Minimální režie** – Objekty obsahují jen nutná data.  
✅ **Snadné rozšíření** – Lze přidat další operace nebo objektové typy.  

---

## **🔹 4) Možnosti rozšíření**  
🔸 **Víceúrovňové operace** – Např. `Sečti první dva objekty a pak výsledek přidej k objektu X.`  
🔸 **Funkce nad seznamy** – Např. `Najdi největší objekt v seznamu.`  
🔸 **Podmínky a logika** – Např. `Pokud objekt číslo 5 je větší než 3, vypiš "Ano".`  

---

### **🔹 Shrnutí jednou větou**  
Tento systém umožňuje **deklarativní práci s objekty**, kde uživatel **jen popíše operaci**, a systém **sám rozhodne, jak ji provést** na základě tabulkové struktury objektů.  

---

💡 **Až se k tomu vrátíš, můžeš rozvíjet:**
1. Jak definovat složitější operace nad více objekty?  
2. Jak rozšířit systém o podmínky a logické výrazy?  
3. Jak by vypadal parser pro zpracování příkazů?  

---

Díky za skvělou diskuzi! Užij si meditaci a těším se na pokračování. 😊