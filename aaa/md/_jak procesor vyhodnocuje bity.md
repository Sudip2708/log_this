## Dotaz:

Ahojky. Včera jsme nakousli čistě teoreticky téma, že by bylo dobré vytvořit novou ANSI tabulku, která by byla zaměřená čistě na programování a umožňila by zadávat programovací přikazy přímo binárně, takže by se zrychlil výpočet jednotlivých kroků. A samozřejmě narazili jsme na náročnost takového projektu, tak je to zatím čistě ve fázi teorie, ale já bych pozbíral další informace. A jedna myšlenka, která mě napadla, na co jsem se chtěl zeptat, je jak v procesoru probíhá vyhodnocevání bytů, a zda je, nebo spíš tak, abych pochopil víc proces, který je zatím, a tak, abych si dokázal představit, zda se dá aktuální procesor, tak jak je podstaven, využít pouze změnou instrukcí, které binární kody představují.

## ChatGPT:

Ahojky! To, co zmiňuješ, je hodně zajímavé téma, které se vlastně dotýká návrhu instrukční sady procesorů a optimalizace výpočetního procesu. Pokusím se to vysvětlit krok za krokem, abychom se mohli zaměřit na to, jestli by se dalo dosáhnout tvého cíle jen změnou instrukční sady, nebo zda by to vyžadovalo hlubší zásah do architektury procesorů.

---

### **Jak procesor vyhodnocuje byty?**
Procesor pracuje s binárními daty v několika fázích, které odpovídají cyklu zpracování instrukcí:

1. **Fetch (Načtení instrukce)**  
   - Procesor si z paměti (RAM nebo cache) načte instrukci, která je zakódovaná jako binární číslo.  
   - Každá instrukce má specifický formát, který definuje operaci (např. sčítání, přesun dat, skok) a operand(y) (např. registr nebo paměťová adresa).  

2. **Decode (Dekódování instrukce)**  
   - Řídicí jednotka procesoru analyzuje binární kód instrukce a rozhodne, jaké akce je potřeba provést.  
   - Instrukční sada (např. x86, ARM, RISC-V) definuje, jak procesor interpretuje konkrétní sekvenci bitů jako operaci.  

3. **Execute (Provedení instrukce)**  
   - Procesor provede operaci, například sčítání dvou registrů, přesun hodnoty z paměti do registru, skok na jinou instrukci atd.  
   - Výsledek se uloží do registru, paměti nebo jiného výstupu.  

4. **Writeback (Zápis výsledku)**  
   - Výsledek operace je zapsán zpět do registru nebo paměti, aby mohl být využit dalšími instrukcemi.  

---

### **Lze změnit jen instrukční sadu, aby se programování dalo provádět binárně?**
Teoreticky ano, ale je tam pár zásadních problémů:

1. **Instrukční sada není jen software, ale je zakódovaná v hardwaru**  
   - Procesor má pevně daný způsob, jak dekóduje binární instrukce. Pokud bychom změnili význam jednotlivých bitů, museli bychom přeprogramovat řídicí jednotku CPU.  
   - Moderní procesory s mikroprogramovatelnou architekturou (např. některé RISC-V procesory) umožňují upravit instrukční sadu, ale běžné x86 a ARM procesory ne.  

2. **Optimalizace už dnes existují (RISC vs. CISC)**  
   - Existují dvě hlavní architektury:  
     - **CISC (Complex Instruction Set Computing)** – typicky x86, kde jedna instrukce dělá hodně práce.  
     - **RISC (Reduced Instruction Set Computing)** – ARM, RISC-V, kde instrukce jsou jednoduché, ale rychlejší.  
   - Moderní procesory se již snaží optimalizovat výkon překladem instrukcí do mikrokódů nebo paralelizací.  

3. **Programování v binárním kódu by bylo složité**  
   - Dnes máme programovací jazyky, které jsou vyšší abstrakcí nad binárním kódem, což umožňuje snadnější psaní a optimalizaci kódu.  
   - I kdyby se vytvořila nová ANSI tabulka pro programování, stále bychom potřebovali nástroj, který by ji dokázal přeložit do něčeho, co procesor rozumí.  

---

### **Alternativní přístup – můžeme obejít nutnost úpravy procesoru?**
Pokud bys chtěl vytvořit systém, kde programy běží přímo v binární formě, můžeš to zkusit jinak:
- **Použít FPGA (Field-Programmable Gate Array)** – čip, kde si můžeš definovat vlastní instrukční sadu a změnit její význam bez nutnosti vyrábět nový procesor.  
- **Emulátor** – napsat softwarový emulátor, který by interpretoval binární instrukce podle nové logiky (např. jak to dělá QEMU pro různé CPU architektury).  
- **Jazyk blízký binárnímu kódu** – například WebAssembly (WASM) umožňuje kód spustit v optimalizované binární podobě nezávisle na CPU.  

---

### **Shrnutí**
- Procesor interpretuje binární kód podle pevně dané instrukční sady, která je hardwarově zakódovaná.  
- Lze změnit instrukční sadu, ale ne u běžných procesorů – potřeboval bys speciální architekturu (např. RISC-V, FPGA, nebo vlastní emulátor).  
- Přímé binární programování by bylo složité, ale optimalizované prostředí, které by binární kód efektivně interpretovalo, by mohlo být zajímavou cestou.  

Můžeš třeba zkusit napsat jednoduchý emulátor, který by binární kód vykonával podle vlastních pravidel – tím by sis mohl pohrát s tím, jak efektivně vykonávat jednotlivé instrukce. Co si o tom myslíš?
