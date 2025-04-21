Z toho, co psal na začátku, tak mě napadlo, že v případě přirozeného zápisu jazyka by se dalo využít toho, že jednotlivá slova jsou oddělena mezerou větů končené tečkou či čárkou a z toho třeba tak nějak vycházet, nevím teda přesně svou tečkou nebo čárkou, ale ta mezera mi přijde jako dobrý způsob, jak od sebe oddělit jednotlivé příkazy, které by tak vlastně mohly tvořit přímé věty.
---

Ano, mezery a interpunkce by mohly sloužit jako přirozený způsob strukturování jazyka, což by umožnilo jeho **čitelnost** a zároveň jednodušší **parsování**.  

Dalo by se to koncipovat tak, že:  
- **Každé slovo odpovídá určitému klíčovému slovu nebo operátoru.**  
- **Mezery oddělují jednotlivé argumenty.**  
- **Tečka nebo čárka slouží jako oddělovač příkazů.**  

---

### **Jak by mohl vypadat zápis v takovém jazyce?**  
Příklad programu v přirozeném jazyce:  
```  
Set X to 10.  
Add X and 5, store in Y.  
If Y is greater than 10, print "Hello".  
```
➡ **Tento zápis je čitelný, ale zároveň přesně definovaný.**  

---

### **Jak by se to dalo naparsovat?**  
✅ **První rozdělení na příkazy** (podle teček a čárek):  
```  
["Set X to 10", "Add X and 5 store in Y", "If Y is greater than 10 print 'Hello'"]
```
✅ **Druhé rozdělení na tokeny (podle mezer):**  
```json
[
  ["SET", "X", "TO", "10"],
  ["ADD", "X", "AND", "5", "STORE", "IN", "Y"],
  ["IF", "Y", "IS", "GREATER", "THAN", "10", "PRINT", "\"Hello\""]
]
```
➡ **To už je struktura, se kterou se dá snadno pracovat v parseru.**  

---

### **Výhody tohoto přístupu**  
✔ **Snadná čitelnost pro lidi:** Příkazy vypadají jako normální věty.  
✔ **Přirozená struktura:** Mezery a interpunkce už přirozeně rozdělují věty.  
✔ **Jednodušší parsování:** Méně složitých pravidel, stačí jen lexikální analýza.  

---

Tento přístup by se dal skvěle použít v **první fázi vývoje jazyka**, protože umožňuje snadno vytvořit **jednoduchý překladač nad Pythonem**, a následně lze přidat další optimalizace.

