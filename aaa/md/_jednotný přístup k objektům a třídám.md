Zde bych zase chtěl zkusit, zda by se dalo obejít bez dvojího rozdělení funkce na vnitří (jako metodu) a ne vnější (jako funkce) a rozdíl mezi vnitřní metodu a vnější funkcí by byl čistě v parametrech. Prakticky tak je to i teď, takže v otm by se moc neměnilo.

A co se týká objektů, tak zde se asi na chvilku zastavíme, protože rád bych dohledal optymální řešení, které by bylo použitelné nejen pro třídu ale pro všechny další objekty. Přeci jenom bych rád aby to byl čistě objektový jazyk. Jestli si ještě vzpomeneš, tak jsem psal že i mysl přemýšlí objektově, a tak slovo jablko je objekt který může mít rozdílné parametry (chuť, barva, velikost) ale stále je to jeden objekt jablko.

Takže když si představíme třeba definici jablka  to že někde bychom chtěli zjistit jeho barvu,
Pak by zde byla nějaký základní objekt jablko, z kterého by se vytvořil nový objekt:
Vytvoř nový objekt z "jablko" a nazvi ho "granátové jablko"
případně
Vytvoř objekt "granátové jablko" použij základ "jablko"
nebo 
Vytvoř objekt "granátové jablko" a vycházej z "jablko"
či nějaká podobná kombinace.

A přístup k atributům nebo funkcím by mohl být:
"x" = "granátové jablko", "barva"
případně:
"x" = ("granátové jablko", "barva")
případně ještě i více slovně:
"x" = "barva" z objektu "granátové jablko"

A stejně tak přiřazení by se mohlo definovat:
Přiřaď "modrá" jako "barva" do objektu "granátové jablko"
případně:
("granátové jablko", "barva") = "modrá"

A volání funkce by mohlo být:
Proveď ("moje auto", "zrychli") o 10

Případně:
Volej funkci "zrychli" z objektu "moje auto", parametr "zrychlení" nastav na 10

Co na to říkáš, dává to smysl a dá se to nějak ještě více dopracovat?

---

💡 **Tohle je velký krok k objektovému myšlení v jazyce!** A musím říct, že tenhle přístup se mi hodně líbí. **Tvoříme opravdu přirozený objektový model, kde se všechno chová jako objekt!** 🔥  

## 🔍 **Co se mi líbí na tomto přístupu?**  
✅ **Jednotný přístup k objektům a třídám** – Není třeba dělit na „třídu“ a „objekt“, místo toho máme **základní objekt** a z něj **odvozené objekty**. To je krásně přirozené.  
✅ **Přirozené slovní zápisy** – *„barva z objektu granátové jablko“* zní jako běžná řeč a je naprosto pochopitelné, co znamená.  
✅ **Objektově čisté** – Každý objekt může mít vlastní parametry a metody, což je v souladu s tím, jak přemýšlíme.  

---

## 🔥 **Návrh finální podoby zápisu**  

### **1️⃣ Vytvoření objektu**  
Máme několik variant, které bychom mohli použít:  

```text
Vytvoř nový objekt z "jablko" a nazvi ho "granátové jablko".
Vytvoř objekt "granátové jablko" použij základ "jablko".
Vytvoř objekt "granátové jablko" a vycházej z "jablko".
```

🎯 **Osobně se mi nejvíc líbí:**  
```text
Vytvoř objekt "granátové jablko" z "jablko".
```
✔ Krátké  
✔ Přehledné  
✔ Přirozené  

---

### **2️⃣ Přístup k atributům**  
Získání hodnoty atributu může mít různé formy:  
```text
"x" = "granátové jablko", "barva".
"x" = ("granátové jablko", "barva").
"x" = "barva" z objektu "granátové jablko".
```

🎯 **Osobně bych volil:**  
```text
"x" = "barva" z objektu "granátové jablko".
```
✔ Přirozené  
✔ Dobře čitelné  

---

### **3️⃣ Změna hodnoty atributu**  
Tady máme opět několik možností:  
```text
Přiřaď "modrá" jako "barva" do objektu "granátové jablko".
("granátové jablko", "barva") = "modrá".
```

🎯 **Moje volba:**  
```text
Nastav "barva" na "modrá" v objektu "granátové jablko".
```
✔ Přirozené  
✔ Čitelné  
✔ Konzistentní se čtením atributu  

---

### **4️⃣ Volání metody objektu**  
Můžeme mít varianty jako:  
```text
Proveď ("moje auto", "zrychli") o 10.
Volej funkci "zrychli" z objektu "moje auto", parametr "zrychlení" nastav na 10.
```

🎯 **Osobně bych volil:**  
```text
Proveď "zrychli" v objektu "moje auto" s parametrem 10.
```
✔ Přirozené  
✔ Dobře čitelné  
✔ Flexibilní pro více parametrů  

---

## 🔥 **Celkový přehled návrhu**  

```text
Vytvoř objekt "Auto".
Nastav "barva" na "červená" v objektu "Auto".
Nastav "rychlost" na 0 v objektu "Auto".

Vytvoř funkci "zrychli" v objektu "Auto" s parametrem "o kolik": (
    Nastav "rychlost" na "rychlost" + "o kolik" v objektu "Auto".
).

Vytvoř objekt "moje auto" z "Auto".
Proveď "zrychli" v objektu "moje auto" s parametrem 10.
```

---

## 💬 **Co myslíš? Je to přehledné a použitelné?** 😊

