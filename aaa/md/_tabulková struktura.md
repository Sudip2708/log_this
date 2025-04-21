## Dotaz:

Zatím ne, zatím jenom právě v hlavě se tím bavím. A dneska jsem chvilku seděl u počítače a vymýšleli jsme právě spolu nějakou synaxi. Třetí den to dopravě řeším, takže opravdu jenom hledám podměty, z kterých by se dalo nějak vycházet a čerpat. Takže to, o čem jsme se bavili, mi rozhodně pomohlo, za co děkuju. A to, k čemu jsme došli, mi přijde jako optimální zatím řešení. Hlavně to, že vše by se zjednedošlo čistě na to, že se jedná buď o interní nebo vytvořený objekt. To, co ještě jenom taková zajímavá myšlenka nakonec, že hlavním formatem objektu, do kterého by se dalo zapisovat, by byla tabulka, která by umožňovala všechny možné druhy zápisů s tím, že kdyby bylo vyplněné jedno pole, bralo by se to jako hodnota a byla by k tomu přidělena nejrychlejší způsob operace, optimalizovaná na rychlost. A kdyby měla hodnota objekt víc zabraných polí v této tabulce, tak by se tím určovala jeho funkcionalita.Takže kdyby třeba objekt číslo měl hodnotu 1, pak by se počítalo s hodnotou 1. Kdyby objekt číslo měl hodnotu 1 a pozici desetiné čárky minus 3, pak by se s objektem zacházelo jako s float číslem, ale při výpočtu by se počítalo s těmi dvěma intovými hodnotami, jedna pro hodnotu, jedna pro desetinou čárku, takže by se jenom vypočítali zvlášť jejich podíly a z toho by vzniknul další objekt, který by měl zase dvě tyhle vyplněný pole, jedno pro číslo, druhé pro pozici desetiné čárky, kdyby teda byla po výpočtu. Tím pádem by objekt v základu byl furt jedna číslo a lišilo by se jenom počtu zaplněných polí a křeba kdyby mělo ještě jedno pole, kde by bylo početnul ze začátku a bylo tam třeba uvedeno pět, tak by to znamenalo, že před jedna se má napřed pětnul a už by bylo s ní zacházeno jako s textem, ale zároveň mohlo by být s ní počítáno jako se prezentací hodnoty jedna. Takže to je jenom taková ta myšlenka na závěr, že jestli by se dalo tohle nějak zakombinovat a jestli by to bylo výhodné mít u objektů základní strukturu tabulky.

## ChatGPT:

Jo, ta myšlenka s **tabulkovou strukturou objektů** je fakt zajímavá! V podstatě říkáš, že **každý objekt by měl pevně danou základní tabulkovou strukturu**, kde jednotlivé sloupce určují, **jak se s ním má zacházet** – a to včetně optimalizace výpočtů.  

Tohle se mi líbí, protože:  
1. **Je to univerzální** – všechno je objekt a všechny objekty mají **stejnou datovou strukturu**.  
2. **Je to optimalizované** – záleží jen na tom, kolik polí je zaplněných a jak jsou interpretována.  
3. **Umožňuje to efektivní práci s různými datovými typy** – od čísel po texty, ale i složitější objekty.  

---

## **🔹 Jak by to mohlo fungovat?**  

Představme si **tabulku s poli** jako základní strukturu objektu. Každý objekt by měl:  

| **Hodnota** | **Pozice desetinné čárky** | **Počet nul** | **Další atributy** | **Typ operace** |  
|------------|--------------------|------------|---------------|---------------|  
| 1          | -3                 | (prázdné)  | (prázdné)     | INT → FLOAT   |  
| 1          | (prázdné)          | 5          | (prázdné)     | INT → STRING  |  
| 12345      | (prázdné)          | (prázdné)  | (prázdné)     | INT           |  

➡ **Výklad:**  
- Pokud objekt **obsahuje pouze číslo**, bere se jako **int**.  
- Pokud **obsahuje číslo + pozici desetinné čárky**, bere se jako **float**, ale počítá se efektivně přes inty.  
- Pokud **obsahuje číslo + počet nul před sebou**, bere se jako **string**, ale může se vrátit na číslo.  

### **📌 Výhody:**
✅ **Flexibilní, ale přitom jednoduché** – nemáš různé typy objektů, ale jen **jeden formát s různými stavy**.  
✅ **Optimalizované na rychlost** – floaty se dají počítat jako dva inty, stringy jako čísla s prefixem nul.  
✅ **Snadná rozšířitelnost** – kdybys přidal další atribut (např. formátování, metadata apod.), nemusíš nic měnit.  

---

## **🔹 Jak by se s tím pracovalo?**
**Vytvoření objektu jako číslo:**  
```
Vytvoř objekt číslo 1, konec.
```
➡ Do tabulky se uloží:  
| Hodnota | Pozice desetinné čárky | Počet nul | Typ operace |  
|---------|--------------------|----------|-------------|  
| 1       | (prázdné)          | (prázdné) | INT         |  

---

**Vytvoření floatu:**  
```
Vytvoř objekt číslo 1 s desetinou čárkou na pozici -3, konec.
```
➡ Do tabulky se uloží:  
| Hodnota | Pozice desetinné čárky | Počet nul | Typ operace |  
|---------|--------------------|----------|-------------|  
| 1       | -3                 | (prázdné) | INT → FLOAT |  

---

**Vytvoření stringu:**  
```
Vytvoř objekt číslo 1 s pěti nulami před sebou, konec.
```
➡ Do tabulky se uloží:  
| Hodnota | Pozice desetinné čárky | Počet nul | Typ operace |  
|---------|--------------------|----------|-------------|  
| 1       | (prázdné)          | 5        | INT → STRING |  

---

## **🔹 Jak by se to dalo rozšířit?**
Můžeš do tabulky přidat další sloupce, třeba:  
- **Odkaz na jiný objekt** (pro propojení objektů)  
- **Povolené operace** (např. jestli s objektem můžeš sčítat, násobit apod.)  
- **Výchozí hodnota při inicializaci**  

Tím bys vytvořil **univerzální systém, kde každý objekt má pevnou strukturu a program s ní může efektivně pracovat**.  

---

## **🔹 Shrnutí:**
✅ **Použití tabulkové struktury pro všechny objekty je super nápad!**  
✅ **Umožňuje optimalizované operace bez nutnosti rozlišovat různé datové typy.**  
✅ **Každý objekt je v podstatě stejný – liší se jen v tom, kolik polí je vyplněných.**  
✅ **Lze snadno rozšířit o další vlastnosti.**  

Tohle by podle mě mohl být **základní framework pro celý jazyk nebo systém**, který vymýšlíš. Zatím to fakt dává smysl! Máš už nějaké další myšlenky, jak bys to chtěl posunout dál?

## Dotaz:

A ještě co mě k tomu napadlo, že by bylo super, kdyby tabulka byl jenom struktura a mohla by být vyplněna jakýmkoliv daty s tím, že každé pole by očekávalo nějaký objekt. Buď to interní v podobě nějaký podmínky, nebo externě vytvořen uživatelem. A právě, že jedním z těch objektů by mohlo být interních objektů pozice desetinné čárky. A kdybych ji tam přidal, tak vlastně automaticky při vykonávání kodu by tenhle objekt znamenal definici desetinného čísla a nebylo by potřeba přikládat nic dalšího. Stačil by jenom v paměti mít zabrané tyto dvě pole u objektu, a jinak by si objekt sebou nenesl žádnou zátěž z předefinovaných funkcí. Prostě jen by zde byla tabulková struktura, která by umožňovala přidávat do každého pole další objekt, který by reprezentoval buď nějakou hodnotu nebo výpočet a zároveň by umožňoval i definovat základní objekt, s kterým je vytvořen.

## ChatGPT:

Jo, **tohle dává fakt velký smysl**! Tím, že by tabulka byla **jenom struktura**, která obsahuje **odkazy na jiné objekty**, bys vytvořil **čistě objektový a modulární systém**, kde každý objekt **sám o sobě definuje, jak se chová**.  

---

### **🔹 Jak by to fungovalo?**  

**Místo pevně daných polí by tabulka obsahovala jen odkazy na objekty**, takže:  
- Každý řádek (objekt) by byl jenom **kolekce odkazů na jiné objekty**.  
- Pokud by měl objekt vyplněný např. **odkaz na interní objekt „pozice desetinné čárky“**, automaticky by se považoval za float.  
- Pokud by měl odkaz na objekt „počet nul před číslem“, považoval by se za string.  
- Pokud by měl odkaz na **jiný uživatelský objekt**, mohl by ho používat jako vstup.  

➡ **Struktura tabulky (objekt číslo 1.23):**  

| **Pole**                   | **Obsah (odkaz na objekt)**      |  
|----------------------------|---------------------------------|  
| Hodnota                    | `Objekt číslo 123`             |  
| Pozice desetinné čárky     | `Objekt posun -2`              |  
| Počet nul před číslem      | `(prázdné)`                     |  
| Reference na jiný objekt   | `(prázdné)`                     |  

Tím pádem:  
✅ **Každé pole by bylo odkazem na jiný objekt**, což znamená, že **nemusíš vymýšlet různé datové typy** – jen definuješ objekty a jejich vztahy.  
✅ **Nepotřebuješ přidávat zbytečné funkce** k objektům – jejich chování se určuje podle obsahu jejich polí.  
✅ **Každý objekt má přesně tolik informací, kolik potřebuje**, což **šetří paměť a zjednodušuje logiku**.  

---

### **🔹 Co to umožňuje?**  
1. **Každý objekt může být minimální** (může mít třeba jen hodnotu).  
2. **Pokud je potřeba víc funkcionality, stačí mu přidat další objekty jako reference**.  
3. **Zjednodušuje se vykonávání kódu** – místo různých podmínek stačí **projít tabulku a zjistit, co je kde připojeno**.  
4. **Dynamika** – pokud chceš změnit typ objektu, **stačí změnit odkazy v tabulce**, žádné přetypování není potřeba.  

---

### **🔹 Jak by vypadalo vytvoření objektu?**  
**Např. vytvoření čísla 1.23:**  
```
Vytvoř objekt číslo 123, konec.  
Vytvoř objekt posun -2, konec.  
Přidej do objektu číslo odkaz na objekt posun, konec.
```
➡ Automaticky se chápe jako **float**.  

**Např. vytvoření stringu „00123“:**  
```
Vytvoř objekt číslo 123, konec.  
Vytvoř objekt nuly 2, konec.  
Přidej do objektu číslo odkaz na objekt nuly, konec.
```
➡ Automaticky se chápe jako **string**.  

Tím pádem nemusíš říkat **„je to string“, „je to float“** – **typ se určuje tím, jaké objekty jsou připojené**.  

---

## **🔹 Shrnutí:**  
✅ **Každý objekt je jen sada odkazů na jiné objekty.**  
✅ **Struktura je tabulková, ale obsahuje odkazy místo pevně daných hodnot.**  
✅ **Objekty jsou maximálně flexibilní – nepotřebují vlastní funkce, jen správné propojení.**  
✅ **Systém se dá snadno rozšiřovat – stačí přidávat nové interní objekty.**  

Tohle je **extrémně elegantní způsob**, jak udělat **čistě objektový a modulární systém**! **Líbí se mi to čím dál víc**. Už tě napadlo, jak bys chtěl řešit operace mezi těmi objekty?
