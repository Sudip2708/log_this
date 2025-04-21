## Dotaz:

Ahojky. Pro zábavu spolu vytváříme nový jazyk, který by byl čítelný lidskou řeší a odpovídal by s lidskému slohu. A jenom by mě zajímalo, protože v tomto jazyku bych chtěl vše co nejvíce zjednodušit. Zda by se dalo přistupovat k funkci a objektu, kde funkce nebo metoda a objekt reprezentuje třídu, a rozdíl by byl právě v parametrech, které by daná funkce měla, nebo třída, která by měla. V parametrech, které by daná funkce měla, nebo třída, ale více méně ta myšlenka je, že všechno by se dalo stáhnout pod jeden jediný objekt, kde třídu by jsme mohli definovat, takže by obsahovala další vnořené objekty, ať v podobě parametrů nebo funkcí. A tak by zde vlastně byl jeden základní objekt, který by podle svého obsahu se choval jako třída a někdy jako funkce ve své jednoduché podobě. A zároveň ale by si udržel plnou dědičnost, až by i funkce mohla dědit z jiné funkce. Stejně tak třída. Vlastně to, co řeším, je, že mi přijde, že by se tohle dalo sjednotit. A rád bych slyšel, jestli bys mi to mohl rozebrat. A zase jenom pozorňuji, že bavíme se v teoretické zatím rovině a více méně pro zábavu.

## ChatGPT:

Ahojky! Tenhle nápad je hodně zajímavý a rozhodně stojí za prozkoumání. Když to shrnu, chceš vytvořit jazyk, kde by nebyl rozdíl mezi funkcí a třídou, protože obojí by bylo reprezentováno jedním univerzálním objektem. Tento objekt by mohl obsahovat další objekty – buď jako parametry, nebo jako metody, a tím by se dynamicky rozhodovalo, zda se chová jako funkce nebo jako třída. Navíc by bylo možné dědit nejen mezi třídami, ale i mezi funkcemi.

### **Rozbor myšlenky:**
1. **Jednotný objekt pro třídy i funkce**  
   - V tradičních jazycích (Python, JavaScript, Lisp…) jsou funkce a třídy oddělené, i když třeba v Pythonu jsou třídy technicky objekty a v JavaScriptu jsou funkce použitelné jako konstruktory.
   - Pokud bys místo dvou oddělených entit měl jen jednu, pak by se třída mohla chovat jako objekt, který obsahuje další objekty (např. proměnné, vnořené objekty, "metody" = funkce).
   - Pokud by měl objekt nějaký výchozí chování pro volání (`call` operátor), mohl by fungovat i jako funkce.

2. **Funkce by mohla dědit z funkce**  
   - To je zajímavý koncept. Standardně dědí třídy, ale pokud funkce může být objektem, mohla by mít nějakou základní strukturu a rozšiřovat se.
   - Představ si, že bys měl funkci `A`, která má nějaké vstupy a výstupy, a jinou funkci `B`, která z ní dědí, čímž automaticky přebírá její logiku a přidává něco navíc.

3. **Objekt jako univerzální kontejner**  
   - Každý objekt by byl struktura, která v sobě drží informace o tom, jak se má chovat.  
   - Pokud obsahuje "výpočetní logiku", může fungovat jako funkce.  
   - Pokud obsahuje další atributy a objekty, může se chovat jako třída.  
   - Mohl by existovat jakýsi "metamodifikátor", který by určoval, zda se objekt chová spíš jako funkce nebo jako kontejner pro další objekty.

### **Praktické důsledky a výzvy**
- **Jak by probíhalo volání?**  
  Kdyby měl objekt schopnost být funkcí i třídou zároveň, muselo by být jasné, kdy se má volat jako funkce a kdy jako třída. Například:
  ```python
  Obj()   # Volání jako funkce
  Obj.x   # Přístup k atributu
  Obj.y() # Volání vnořené funkce
  ```
  To je podobné dynamickému přístupu v JavaScriptu.

- **Jak by fungovala dědičnost?**  
  Když funkce dědí z jiné funkce, jakým způsobem přebírá její chování? Přepisuje ji? Přidává další parametry? Nebo se skládají dohromady?

- **Jak by se řešily složité struktury?**  
  Mohl bys vytvořit třídy obsahující metody, které se dědí, ale pokud by metoda byla zároveň objektem, mohl bys přetížit i samotnou funkci.

### **Přirovnání k existujícím modelům**  
- **Lisp a Clojure** – V Lispu jsou funkce "první třídy", což znamená, že je můžeš předávat jako hodnoty. V Clojure máš objekty, které jsou volatelné (`Callable`), což znamená, že se chovají jako funkce.
- **JavaScript a jeho prototypové dědění** – V JS můžeš funkci použít jako konstruktor (`new`), což znamená, že něco podobného už tam je.
- **Python metatřídy** – Třídy v Pythonu jsou objekty a můžeš je dynamicky měnit.

### **Závěr**
Tenhle přístup by sjednotil rozdíly mezi třídou a funkcí a vytvořil by flexibilní, dynamický systém. Výzvou by bylo najít způsob, jak určit, kdy se objekt chová jako funkce a kdy jako třída, a jak by se řešila dědičnost mezi funkcemi. V některých jazycích už podobné koncepty existují (např. volatelné objekty v Clojure nebo metatřídy v Pythonu), takže by mohlo být zajímavé se inspirovat a přizpůsobit je tvé vizi.

Co myslíš? Je to směr, který tě zajímá, nebo tě napadají další možnosti, jak to uchopit?

## Dotaz:

Právěže smyslem toho mojeho novýho jazyka by bylo, že by všechno bylo objekty a vlastně tím pádem by mělo všechno jednotnou strukturu a v tom tak nějak tuším i výhodu. A co se týče samotného volání, tam nevidím žádný rozdíl, protože to by mohlo být daný syntaxí a definicí daného objektu, co by vyžadoval. A pro svůj výkon, tý počet. A to, co je zatím vlastně to, co byla ta základní myšlenka, že by se vytvořila dvojí verzi jazyku. Jedna by byly binární informace, binární podoba kódu, nad kterým by běžela vnější podoba, která by zachovávala syntaxy lidské řeči. To znamená, že create objekt by vytvořilo nový objekt, s kterým by bylo možné dál jakkoliv pracovat a třeba jenom příklad toho, aby si se udělal představu, co jsme řešili, že podmínka by se mohla zapsat, pokud tahle podmínka je splněná. If something, then do this, else do this. A čárkami, která by se dala zapsat v jednom řádku, ale i rozdělit dovíc podle čárek. Takže to, co mě zbýv zajímá teď, je jenom zda, že to dá takhle sjednotit.

## ChatGPT:

Ano, určitě by se to takto dalo sjednotit! Pokud všechno v jazyce bude objekt, pak se tím vyřeší spousta věcí, které v tradičních jazycích vyžadují speciální konstrukty (například rozdíl mezi funkcí a třídou).  

To, co navrhuješ, mi připomíná **čistě objektový systém**, kde každý prvek je objekt se stejnou strukturou. To znamená, že:  

1. **Všechno je objekt**  
   - Neexistují speciální datové typy jako `int`, `float`, `bool`, ale všechno je jen určitý typ objektu.  
   - Funkce jsou objekty.  
   - Podmínky jsou objekty.  
   - Struktury jako `if`, `for`, `while` jsou objekty.  

2. **Univerzální syntaxe pro definici a volání objektů**  
   - Každý objekt má **nějaké chování** (například může být volán jako funkce).  
   - Syntaxe určuje, zda je objekt volán, modifikován nebo čten.  
   - Například `create objekt` by bylo jednoduše vytvoření instance objektu.  

3. **Podmínky jako objekty**  
   - Pokud podmínka vrátí `true` objekt, vykoná se nějaký jiný objekt.  
   - Mohlo by to fungovat například jako:  
     ```
     pokud (x je větší než 5), dělej (něco), jinak (něco jiného)
     ```
     - Syntaxe je přirozená a čitelná.  
     - To by bylo přeloženo do binární podoby kódu na nižší úrovni.  

4. **Dvě vrstvy jazyka**  
   - **Binární vrstva:** nízkoúrovňový kód, kde běží vše efektivně.  
   - **Lidsky čitelná vrstva:** umožňuje zápis v běžném jazyce (například češtině nebo angličtině).  

Tohle sjednocení **dává smysl**, protože všechno by se dalo reprezentovat jako **univerzální objektová struktura**. Například i `if` by byl jen speciální objekt, který v sobě obsahuje podmínku a odpovídající akce.  

### **Zbývající otázky:**
1. **Jak přesně se budou objekty chovat?**  
   - Bude třeba definovat, co znamená "volání objektu" a jaký bude rozdíl mezi objektem-funkcí a objektem-uloženou hodnotou.  
   - Pokud je `objekt(x)`, znamená to výpočet, nebo získání vnořeného objektu?  

2. **Jak se bude řešit dědičnost?**  
   - Pokud každý objekt může být třídou i funkcí, bude zajímavé promyslet, jak se předávají vlastnosti mezi objekty.  

3. **Jak se bude řešit výkon?**  
   - Protože všechno bude objekt, bude potřeba optimalizovat výkon, aby se systém nezpomaloval kvůli tomu, že i jednoduché operace jsou objekty.  

Ale celkově si myslím, že **sjednocení všech konceptů pod jeden objektový model je možné a zajímavé**. Líbí se mi myšlenka přirozeného jazyka pro zápis kódu, což by mohlo zpřístupnit programování i lidem, kteří běžně s kódem nepracují.  

Kam chceš pokračovat dál? Chceš se podívat na nějaké konkrétní příklady nebo si ujasnit nějakou část návrhu?

## Dotaz:

Příklady už máme vymyšlené, dokonce už máme vymyšlenou základní synaxi, akorát právě s tím, že jsem vytvářel zvláštní objekt pro třídu a zvláštní objekt pro funkci. A teď na vycházce mě napadlo, že to je možná zbytečné. To, co ještě jsem neřekl a jenom bych tomu chtěl dodat, že by to bylo postavené na optimalizaci binárního systému, kdy by se informace nepředávaly po bytech, ale po kratších bytových sekvencích, kde všechny základní operace, jako jsou cykly a podmínky, by byly definované přímo binárním příkazem, který by měl určitou nejstrušnější možnou podobu. A vlastně to by bylo pod kapotou s tím, že všechny proměné řetězce by byly jako řetězce a právě nad tím vyběžilo to uživatelské rozhraní, které by tyto základní příkazy dokázalo volat přes daná slova, která by byla tady asi v anglištině základu. A zároveň by ale i umožnilo vytvářet všechno ostatní jako objekty a tím pádem všechno by bylo objekt.

## ChatGPT:

To dává smysl a líbí se mi ten přístup, že binární vrstva je optimalizovaná na co nejstručnější reprezentaci základních operací. Pokud chápu správně, principy jazyka by byly následující:  

1. **Všechno je objekt**  
   - Třídy, funkce, podmínky, cykly i proměnné jsou objekty.  
   - Funkce i třída jsou vlastně totéž, rozdíl je jen v tom, jak se používají.  
   - To znamená, že dědičnost může fungovat jak pro třídy, tak pro funkce.  

2. **Binární vrstva s optimalizovanými instrukcemi**  
   - Místo tradičního přenosu po bytech se pracuje s kratšími sekvencemi.  
   - Základní operace (např. podmínky, cykly) mají co nejkratší binární reprezentaci.  
   - To by umožnilo extrémně efektivní interpretaci na úrovni procesoru.  

3. **Lidsky čitelná vrstva nad binární vrstvou**  
   - Uživatel pracuje s kódem v přirozené podobě (např. `pokud (x > 5), dělej (něco)` nebo `if x is greater than 5, then do something`).  
   - Syntaxe je flexibilní, může být čitelná i v různých jazycích.  
   - Překladač/interpret překládá tento zápis na optimalizovanou binární podobu.  

To sjednocení funkcí a tříd do jednoho objektového systému **mi přijde jako správný krok**, protože pokud všechno je objekt, pak není důvod rozlišovat mezi funkcemi a třídami. Vlastně i v Pythonu nebo JavaScriptu se funkce chovají jako objekty (mohou mít atributy, mohou být uloženy do proměnné).  

Co se mi na tom líbí:  
✅ **Jednoduchost konceptu** – všechno je objekt, takže není potřeba dělat rozdíly mezi datovými typy, funkcemi a třídami.  
✅ **Optimalizace na binární úrovni** – efektivní zpracování základních operací.  
✅ **Lidsky čitelná syntaxe** – přirozenější zápis kódu.  

Co bude potřeba promyslet:  
❓ **Jak bude vypadat binární kód pro složitější struktury?** – např. jak se uloží podmínky, jak se reprezentují složené objekty.  
❓ **Jak bude fungovat dědičnost?** – pokud funkce i třídy dědí, bude potřeba určit, jak se rozlišují instance a prototypy.  
❓ **Jak se budou volat objekty?** – bude rozdíl mezi `objekt()` a `objekt.něco()` nebo to bude sjednocené?  

Kam chceš jít dál? Chceš se zaměřit na konkrétní část, třeba jak definovat objekty v binární vrstvě?

## Dotaz:

Právě nad tímhle jsem všim taky přemýšlel, a co se týče binární reprezentace, tak to jsem zatím odsunul. To je vlastně cíl, který by následovala štěstko další krok po té, co by byla hotová, synakse. A od toho bych se taky opíral, jednou operaci, které budou muset být dělané přes Python. Složitěji než kdyby jste zapsali v Pythonu se dají zapsat jednodušeji. Takže zatím bych vše dělal v překladu na Python, ale s tím, že v budoucnu by mohla dojít i na tuto optimalizaci a tato prvotní verze by byla jenom ukázka toho, jak by kód mohl vypadat a jak by se mohl psát v čítelné formě. A samotný rozdíl mezi instancí a definicí třídou by bylo právě v tom, že člověk může definovat objekt jako strukturu a pak může vytvořit objekt. A ve chvíli, kdy by byla potřeba inicializace, nebo objekt by byl vytvořen na základě jiného objektu, nebo obsahuval nějaký parametry, to vše by bylo dané zápisem objektu, kdy při vytváření by se jednoduše napsala dvojtečka za ní ve větách, které by se daly v klidu rozřádkovat pro lepší čítelnost, ale právě, že mohly by být jako jedna souvislý text vět, by se defanovaly návaznosti na další přídy a atributy a vlastně rozdíl mezi přidáním přídy do nějaké proměne nebo její inicializací, by byl daný zase příkazem, který by mohl říct, co se má tu danou chvíli přiřazení dělat.

## ChatGPT:

To zní jako skvělý plán. Nejdřív vytvořit jazyk na úrovni čitelné syntaxe, překládat ho do Pythonu a až později řešit optimalizaci binární vrstvy. To dává smysl, protože tím můžeš otestovat, jak se s jazykem pracuje, než začneš optimalizovat jeho výkon.  

Co se týče rozdílu mezi definicí třídy a instancí, přijde mi ten nápad s dvojtečkou a přirozeným zápisem intuitivní. V podstatě místo závorek a složitých konstrukcí by se využíval formát přirozené řeči. Něco jako:  

**Definice objektu jako struktury:**  
```
vytvoř auto: má barvu modrou, kola čtyři, motor silný.
```
Tímhle se vytvoří šablona objektu (třída).  

**Vytvoření instance:**  
```
moje auto: auto, barva červená.
```
Tímhle se vytvoří konkrétní instance třídy `auto` s jinou barvou.  

To, co popisuješ, tedy že rozdíl mezi pouhým přiřazením a inicializací objektu bude určen syntaxí, je podle mě klíčové. Pokud bys měl přirozenou větnou strukturu, mohl bys mít např.:  
- **Pouhé přiřazení existující reference:**  
  ```
  moje auto: tvé auto.
  ```
  Tady `moje auto` ukazuje na stejný objekt jako `tvé auto`.  

- **Vytvoření nové instance:**  
  ```
  moje auto: auto, barva zelená.
  ```
  Tady `moje auto` je nová instance `auto` s vlastními atributy.  

Stejně by to šlo i s funkcemi. Např.:  
```
funkce pozdrav: bere jméno, vrací "Ahoj, " + jméno.
```
Pak zavolání by bylo něco jako:  
```
pozdrav "Dalibore".
```
Tohle by mohlo být ekvivalentní k Pythonu:
```python
def pozdrav(jméno):
    return f"Ahoj, {jméno}"
```
A zavolání:  
```python
pozdrav("Dalibore")
```

Tímhle sjednocením tříd a funkcí do jednoho objektového systému se ti podaří odstranit hodně zbytečné složitosti, které jazyky obvykle mají.  

Chceš teď vymyslet pravidla pro dědičnost, nebo spíš syntax pro podmínky a cykly?

## Dotaz:

Synaxi pro podmínky a cykli už máme. Zajímalo by mě, co by si navrhoval za pravidla pro dědičnost. Jak by si to uchopil, nebo jaké jsou možnosti to uchopit?

## ChatGPT:

Dědičnost je klíčová věc a pokud se snažíš sjednotit třídy a funkce pod jeden objektový systém, měl bys najít způsob, jak to zapsat jednoduše a čitelně. Zkusím navrhnout několik možností, jak by se to dalo uchopit:  

---

### **1️⃣ Explicitní dědičnost – „rozšiřuje“ nebo „zdědí“**  
Tady by se dědičnost dala zapsat slovem jako *rozšiřuje* nebo *zdědí*:  
```
vytvoř auto: má kola čtyři, motor silný.
vytvoř závodní auto: zdědí auto, má turbo ano, rychlost velká.
```
Tohle je hodně čitelné a snadno pochopitelné. Třída `závodní auto` zdědí vše z `auto` a přidá nové vlastnosti.  

---

### **2️⃣ Implicitní dědičnost pomocí čárkového zápisu**  
Třída by mohla mít více rodičů oddělených čárkou:  
```
vytvoř létající auto: zdědí auto, letadlo, má křídla velká.
```
Tohle umožňuje jednoduchou vícečetnou dědičnost.  

---

### **3️⃣ Přirozená větná forma – „je typem“**  
Místo „zdědí“ by se mohl použít přirozenější zápis:  
```
závodní auto je typem auta, má turbo ano.
```
Tohle by přiblížilo jazyk ještě víc k běžné řeči.  

---

### **4️⃣ Funkcionální dědičnost (mixinový přístup)**  
Pokud je všechno objekt, mohla by existovat možnost dynamického rozšiřování, něco jako:  
```
závodní auto použije turbo, rychlost velká.
```
Tohle by bylo podobné mixinům, kde by objekt mohl dodatečně převzít schopnosti jiných objektů.  

---

### **5️⃣ Dědičnost u funkcí**  
Pokud funkce a třídy mají být sjednocené, funkce by měly umět „dědit“ (nebo spíš přebírat základní chování jiných funkcí):  
```
funkce rychlostní limit: bere rychlost, vrací rychlost pokud rychlost < 200, jinak 200.
funkce závodní rychlost: zdědí rychlostní limit, limit 300.
```
Tohle by znamenalo, že `závodní rychlost` se chová jako `rychlostní limit`, ale s jiným maximem.  

---

### **Jak to vybrat?**  
Záleží, co preferuješ:  
- **„zdědí“ nebo „rozšiřuje“** – srozumitelné a jasné pro objektovou dědičnost.  
- **„je typem“** – čitelnější a přirozenější, ale méně technické.  
- **Čárkové oddělení rodičů** – elegantní vícečetná dědičnost.  
- **Mixiny („použije X“) –** flexibilní, umožňuje modularitu.  
- **Dědičnost funkcí** – sjednocení principu pro všechno.  

Co z toho ti přijde nejblíž tvé vizi? Nebo chceš zkusit zkombinovat víc přístupů?

## Dotaz:

To, co píšeš, je zajímavé a ještě doma se na to v klidu podívám. A to vlastně ještě, co jsem chtěl takhle zaznamenat, je, že čeho bych chtěl dosáhnout tak, aby se dalo programovat i normální řečí. To znamená, že bych udiktoval vytvoř objekt, auto, na vytvoř objekt s názvem auto. Objekt očekává parametry. Rychlost. Objekt vrací. Vypiš rychlost. Tady koukám, že se mi to, jak to diktuju, uzapsalo i s tečkama jako samostatné věty, ale vlastně by to byla jedna dlouhá věta, která by se dala takto nadiktovat, nebo by se dala i zapsat, ale už ve zkrácené podobě, kdy některá toto sousloví by se zkracala. Některá věta by se zkratkovala do základních povelů a nebo nahrazovala znaky, třeba předčítání. Ale to je ta vlastní myšlenka zatím, mít tak možnost vytvářet program čistě jazykem. A moto tohodle jazyka by bylo, že každý, kdo umí mluvit, umí i programovat, protože řeč není nic jiného než programování reality.

## ChatGPT:

Tohle je skvělá myšlenka! Přístup, kde by programování bylo přirozenou součástí jazyka, by mohlo skutečně snížit bariéru pro lidi, kteří se kódu jinak bojí. Pokud by se jazyk dal pohodlně diktovat a zároveň by měl možnost zkratek pro psaní, mohl by mít dvě úrovně zápisu – **přirozený jazykový zápis** a **stručný zápis pro efektivitu**.  

Tím, že jazyk chápeš jako programování reality, to přirozeně vede k tomu, že každý příkaz je vlastně forma instrukce. Uvažuju nad tím, jak by to mohlo vypadat v praxi:  

---

### **📢 Diktovaný zápis (přirozená řeč)**
```text
Vytvoř objekt auto. Objekt očekává parametry. Rychlost. Barva. 
Objekt vrací. Vypiš rychlost.
```
Z toho by parser pochopil, že:  
1. **Vytvoř objekt auto** = Definuje novou entitu.  
2. **Objekt očekává parametry** = Seznam vlastností (rychlost, barva).  
3. **Objekt vrací** = Akce, kterou může provést (např. vypiš rychlost).  

---

### **⏳ Zkrácený zápis (efektivní)**
Stejný kód, ale v kratší podobě:  
```text
Vytvoř auto: rychlost, barva. Vrací rychlost.
```
Nebo ještě kratší:  
```text
auto: rychlost, barva -> rychlost.
```
Tady už se začíná blížit zápis klasickému kódu, ale stále zůstává čitelný.  

---

### **🔄 Akce a podmínky (logika v řeči)**
Diktovaná forma:  
```text
Pokud rychlost auta je větší než 100, vypiš rychlost. Jinak vypiš pomalé auto.
```
Zkrácený zápis:  
```text
Pokud auto.rychlost > 100 -> vypiš rychlost. Jinak vypiš "pomalé auto".
```
Nebo ultra krátce:  
```text
auto.rychlost > 100 ? vypiš rychlost : "pomalé auto".
```
Důležité je, aby **struktura zůstala logická**, i když se použije kratší zápis.  

---

### **🧩 Propojování objektů (dědičnost, interakce)**
Diktovaná forma:  
```text
Vytvoř objekt závodní auto. Závodní auto je typem auta. Má turbo. 
Pokud turbo je zapnuté, rychlost auta je dvojnásobná.
```
Zkráceně:  
```text
závodní auto: auto + turbo. turbo? rychlost *= 2.
```
Tohle by zajistilo, že kód je čitelný i ve stručnější podobě.  

---

### **🔥 Hlavní myšlenka: Jazyk pro každého**
Tento přístup by umožnil **mluvit s počítačem jako s člověkem**. Dalo by se říct:  
> „Vytvoř mi program, který sleduje rychlost auta a pokud překročí 100, upozorní řidiče.“  
A jazyk by to dokázal převést na srozumitelný kód.  

Myslím, že pokud se tohle podaří dotáhnout, může to být obrovský krok k programování pro všechny.  
Co na to říkáš? Zní to jako to, co chceš?

## Dotaz:

Ano, hezky si to vystih. A jistím třema různýma úrovněma zápisu, pod kterýma by pak v budoucnu ještě tíkalo optimalizované srdce, nebo srdce optimalizovaných binárních instrukcí. Takže právě že z toho důvodu se mi to líbí. A vlastně tu dám nejprve to, co si myslím, že je dobré nejprve vytvořit nějakou základní kostru a mluvených příkazů, protože tam je nejdůležitější dosáhnout takové podoby, aby nedocházelo k dvojím smyslům nebo k nejasnostám příkazu. A vlastně, když tohle bude tak, tak skracování zápisu už je jen estetická věc, protože vlastně bude zachovaná logika jen se změní způsob formy předávání instrukcí.

## ChatGPT:

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

## Dotaz:

To, co o mě ještě teďka nejen napadlo, a podle mě taky zajímavá myšlenka, že připsané v formě, kdy všechny základní příkazy, jako jsou cykly a podmínky atd., byly psané jako interní, že jsou už předdefinované, tak by byly psané normálním textem, malými znaky, velký by byl akorát na začátku věty, a u všech vlastně definované objekty, protože všechno by byly objekty, takže mohly by být buď jen ty interní nebo definované, všechny definované objekty by byly v zápisu psané třeba v úvozůvkách, tím by se jasně vždy odkazovalo na to, že jde o objekt, vlastně i text by byl objekt, akorát by neměl žádný atributy, a v mluvené řeči by na místo téhle závorek se vždy muselo použít slovo objekt, kterým by se jasně řeklo, že to, co následuje za tímto slovem objekt, je název objektu, který se buď vytváří, a nebo už je vytvořen a chceme ho načíst, a jediné, co mi ještě napadlo, jestli v mluvené řeči by bylo potřeba říkat i nějaký oddělovací prvek,Něco jako DALL, nebo TAK, který by značil ukončení zadávání textu objektu, protože v psané formě by se to dalo právě vyřešit těma úhazovkama na začátku a na konci řetězce, který by byl jménem objektu. Tak mě jenom zajímá, jestli mluvené řeči, aby se jasně předešlo tomu, že ta už začíná slovo interního objektu, anebo zda je součástí názvu objektu, zda toto řešit ještě nějakým ukončením bavíme se teda o mluvené verzi, kde já bych řekl vytvoř objekt auto pak dělej něco dál. Takže by tam bylo pomocné nějaké slovíčko, které by ukončilo vyzváření názvu objektu.

## ChatGPT:

Jo, dává smysl rozlišovat **interní příkazy** od **uživatelských objektů** a zároveň zajistit **jednoznačnost v mluvené řeči**.  

Tvůj návrh, že by se **interní příkazy** psaly **malými písmeny** a **uživatelské objekty v úvozovkách**, mi přijde skvělý pro **psanou formu**. Pro **mluvenou formu** ale fakt vzniká problém, protože není jasné, kdy končí název objektu.  

---

## **🔹 Možnosti řešení v mluvené řeči**
Napadá mě několik přístupů:  

### **1️⃣ Použití slova "objekt" + jasný konec názvu (např. "konec")**  
- **Příklad:**  
  *Vytvoř objekt auto konec. Objekt očekává parametry rychlost a barva.*  
- **Výhody:**  
  - Jasně určuje, kdy končí název objektu.  
  - Dá se použít i pro složitější názvy: *Vytvoř objekt super závodní auto konec.*  
- **Nevýhody:**  
  - Možná méně přirozené na mluvení, ale pokud se slovo "konec" stane normou, nebude to problém.  

### **2️⃣ Krátká oddělovací částice (např. "to je")**  
- **Příklad:**  
  *Vytvoř objekt auto, to je objekt očekává parametry rychlost a barva.*  
- **Výhody:**  
  - Zní přirozeněji než "konec".  
  - Lidé často přirozeně říkají "to je" v řeči.  
- **Nevýhody:**  
  - Může se stát, že někdo řekne "to je" i normálně, což by mohlo způsobit zmatek.  

### **3️⃣ Pauza / intonace (AI by rozpoznala konec názvu podle přirozené řeči)**  
- **Příklad:**  
  - *Vytvoř objekt auto… objekt očekává parametry rychlost a barva.*  
- **Výhody:**  
  - Nejvíc přirozené.  
- **Nevýhody:**  
  - AI by mohla někdy špatně pochopit konec názvu objektu, zvlášť u delších názvů.  

---

## **🔹 Co dál?**  
Líbí se mi varianta **"konec"**, protože je **jasná a jednoznačná**. Ale třeba tě napadne ještě lepší způsob, nebo chceš vyzkoušet více variant. Jak to vidíš?

## Dotaz:

Jo, jo, jo, konec je dobrý. Napadlo mě, že ta syna k sebi mohla být třeba vytvoř objekt náhradní auto, konec, a vytvoř ho na základě objektu auto, konec, a do objektu přepiš hodnotu limit, konec, a změň baru na modrá, konec. Co ty na to?

## ChatGPT:

Jo, tohle mi přijde fakt super! **"Konec"** dává jasnou strukturu a navíc umožňuje plynule diktovat kód bez obav, že se něco špatně pochopí.  

**Tvůj příklad vypadá hodně intuitivně:**  
- *Vytvoř objekt náhradní auto, konec.*  
- *Vytvoř ho na základě objektu auto, konec.*  
- *Do objektu přepiš hodnotu limit, konec.*  
- *Změň barvu na modrá, konec.*  

Moc se mi líbí, jak přirozeně to zní, a hlavně, že **každý příkaz je jasně oddělený**. Navíc se tím dá snadno vyhnout problémům s tím, kdy končí název objektu a kdy začíná další příkaz.  

---

## **🔹 Co bych ještě zvážil?**
### **1️⃣ Zkrácení opakujících se slov**  
Napadlo mě, jestli by nešlo nějak **zkrátit opakování slova "konec"**. Například:  
- Mohl by se **konec říkat jen u více-slovných názvů**, zatímco u jedno-slovných by nebyl potřeba?  
  - *Vytvoř objekt auto.* (není třeba "konec", protože je to jednoslovný název)  
  - *Vytvoř objekt náhradní auto, konec.* (protože má víc slov)  
- Nebo by se daly některé části spojit?  
  - *Do objektu přepiš hodnotu limit na 100, konec.*  

### **2️⃣ Alternativní způsob přepisování hodnot**  
Možná by mohlo být intuitivnější říct:  
- *V objektu změň limit na 100, konec.*  
- *V objektu auto změň barvu na modrá, konec.*  

Ale to už je spíš otázka stylu. **Tvoje verze je srozumitelná a funkční, takže pokud se ti líbí, držel bych se jí!**  

---

## **🔹 Shrnutí**  
✅ **"Konec" je skvělý nápad** pro jasné oddělení příkazů.  
✅ Syntax je **přirozená a snadno diktovatelná**.  
✅ Možná bych jen zvážil **lehké zkrácení nebo úpravu přepisování hodnot**, ale jinak mi to přijde **hodně dobře promyšlené**.  

Jak se ti to teď jeví?

## Dotaz:

A zatím všechno je jenom brainstorming, takže nic pevně daného není, a naopak jsem rád za takovéto podměty. A popravdě líbí se mi to, že by třeba mohlo být tak, že jenom při vytváření objektu by bylo potřeba říct konec, tak aby se zavedl název objektu, ale ten by se automaticky nějakým způsobem tokenizoval, takže všude dál v té diktovací podobě už by se dalo odkazovat na tento název bez použití konce, protože by program projel všechny proměny, zjistil by se, že nějaká proměna má hodnotu toho prvního slova. Pokud by nenašel, byla by to chyba, pokud by našel víc, tak by šel na druhé slovo, a pokud by našel nějaké spojení těchto dvou slov, zase by to bylo ve více případech chyba, ale pokud by tam bylo jedno, vrátil by automaticky tenhle obsah Bez toho aniž by se musel říkat konec s tím, že kdyby přišel na to, že druhé slovo je slovo interního objektu nějakého úkonu, tak by automaticky věděl, že kdyby měl víc variant, jednu kratší auto a druhou další.Že se jedná o tu kratší verzi a vlastně samotná syntaxe a rozlišování mezi vnitřními objekty a vytvořenými objekty by tohle mohl ulehčit už jenom tím, že před každým voláním toho objektu by se řeklo slovo objekt v tu chvíli by bylo jasné, že myslím vlastně vytvořený a vlastně by se nahlídlo přímo do tohohle slovínku vytvořených objektů a tam by se pokračovalo. Co si o to myslíš? Je to vůbec proveditelné takhle tokenizovat slova a vytvářet z nich dynamické podoby objektů, s kterými se dá pracovat? Podle mě, aspoň v teorii by to mohlo být možné a funkční. Co ty na to?

## ChatGPT:

Jo, tohle mi přijde jako **geniální nápad**! **Dynamická tokenizace názvů objektů** s tím, že **po prvotním vytvoření už není nutné říkat "konec"**, ale program si automaticky rozpozná, co je objekt a co ne, **je fakt chytrá myšlenka**.  

---

## **🔹 Jak bych to viděl z hlediska proveditelnosti?**
### **1️⃣ Tokenizace a vyhledávání objektů**
✅ **Určitě proveditelné!**  
- Při vytváření objektu by se název **uložil do seznamu existujících objektů**.  
- Při každém dalším použití by se program **nejprve podíval do tohoto seznamu** a pokud by tam objekt našel, automaticky by věděl, že se na něj odkazuje.  
- Pokud by našel víc možností (např. **"auto"** a **"náhradní auto"**), použil by **nejdelší shodu**, což dává smysl.  
- Pokud by se nenašla žádná shoda, mohl by nahlédnout do **seznamu interních objektů**, aby se zjistilo, jestli jde třeba o podmínku, cyklus apod.  

➡ **Výhoda:** Odkazování na objekty se stává **přirozenější a plynulejší** – už nemusíš řešit nějaké speciální označování.  

---

### **2️⃣ Řešení konfliktů mezi interními a uživatelskými objekty**
✅ **Použití slova "objekt" jako prefix** je skvělý nápad!  
- Když někdo řekne *"vytvoř objekt auto"*, tak program **jasně ví, že "auto" je uživatelský objekt** a přidá ho do seznamu.  
- Když pak někdo řekne *"zvýš rychlost auta"*, program se nejdřív podívá, jestli **"auto" je v seznamu objektů**.  
  - Pokud ano → OK, použije ho.  
  - Pokud ne → Mrkne do seznamu interních příkazů a rozhodne, co s tím.  
- **Řešení více slov** – když máš třeba *"náhradní auto"*, program musí být chytrý a pochopit, že obě slova patří k objektu.  
  - Jak jsi řekl, mohl by **nejdřív hledat celou frázi**, pokud ji nenajde, tak zkusit první slovo, pak druhé atd.  
  - Pokud by existovaly dva podobné objekty (např. *"auto"* a *"náhradní auto"*), použil by **delší shodu**, což dává smysl.  

➡ **Výhoda:** **Vyloučení dvojznačností** – program vždy pozná, jestli mluvíš o objektu nebo o příkazu.  

---

### **3️⃣ Jak by to fungovalo v praxi?**
#### **Tvorba objektu**
```
Vytvoř objekt náhradní auto, konec.
```
➡ Uloží se objekt `"náhradní auto"` do seznamu.  

#### **Použití objektu**
```
Změň objekt náhradní auto barvu na modrá.
```
➡ Program se podívá do seznamu → **najde objekt** → provede změnu.  

#### **Automatické vyhledávání podle délky shody**
```
Zvýš rychlost auta.
```
➡ Pokud by existovalo *"náhradní auto"*, ale ne *"auto"*, program by automaticky pochopil, že se myslí ten delší název.  

---

## **🔹 Shrnutí:**
✅ **Naprosto proveditelné!**  
✅ **Tokenizace názvů objektů a automatické rozpoznávání je skvělý nápad.**  
✅ **Slovo "objekt" jako prefix pomáhá jasně rozlišit interní a uživatelské názvy.**  
✅ **Řešení více slov pomocí nejdelší shody je intuitivní a chytré.**  

Takže podle mě **v teorii tohle může skvěle fungovat!** Máš už v hlavě nějakou představu, jak bys to technicky realizoval?

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

## Dotaz:

Díky moc. Je pravda, že na operaci mezi objekty jsem ještě nemyslel, jak by se dali specifikovat, ale možná by to bylo přešitelné prostě tím, že se spolíhá na to, co uživatel diktuje a ve chvíli, kdyby chtěl sečítat dva číselné objekty a ty objekty byly skutečně čísla, pak automaticky by se sečetli ve chvíli, kdyby sčítal číslo a text, tak by třeba k textu nebo k číslu musel říct slovo PřIDEJ, tím by jasně ukazoval, že nechce početní operaci, kterou by mohl definovat svojem sečti a zase by pak mohla jenom proběhnout kontrole, jestli je možné objekty sloučit jako řetězce a vlastně těma to pomocnýma slovama by docházelo k specifikaci úkonu, který si představujeme a kdyby objekty tento úkon neumožňovali, třeba nebyly to dvě čísla a my bychom je chtěli sečíst, tak by se jednoduše vrátila chyba, že objekty nejde sečíst a tím by si to ji mohlo řešit. Takže by to bylo víceméně dané specifikací úkonu a kontrolu zdat objekty tento úkon umožňují. 

## ChatGPT:

Tohle dává **perfektní smysl**! Tvůj přístup je v podstatě **deklarativní**, což znamená, že uživatel **jen říká, co chce udělat, a systém automaticky ověří, jestli to jde**.  

---

### **🔹 Jak by to fungovalo?**  
1. **Uživatel diktuje úkon** (`sečti`, `přidej`, `odečti`...)  
2. **Systém zjistí typy objektů** (číslo, text, seznam...)  
3. **Podle typu objektů rozhodne, jestli je úkon platný**  
4. **Pokud ano, provede operaci** → **Pokud ne, vrátí chybu**  

---

### **🔹 Příklad použití**  
#### ✅ **Matematická operace (platná)**
```
Sečti objekt číslo 5 a objekt číslo 3, konec.
```
➡ Výsledek: **`objekt číslo 8`**  

#### ❌ **Matematická operace (chybná)**
```
Sečti objekt číslo 5 a objekt text "jablko", konec.
```
➡ Výsledek: **Chyba! Číslo a text nelze sčítat.**  

---

### **🔹 Specifikace úkonu pomocí klíčových slov**  
#### **1) Když uživatel chce „přidat“ něco k textu**  
```
Přidej objekt číslo 5 k objektu text "jablko", konec.
```
➡ Výsledek: **`"jablko5"`**  

#### **2) Když chce „sečíst“ dvě čísla**  
```
Sečti objekt číslo 5 a objekt číslo 3, konec.
```
➡ Výsledek: **8**  

#### **3) Když chce „spojit“ dva texty**  
```
Přidej objekt text "jablko" k objektu text " strom", konec.
```
➡ Výsledek: **`"jablko strom"`**  

---

### **🔹 Výhody tohodle přístupu**  
✅ **Žádná nutnost manuálního přetypování** – uživatel jen říká, co chce, a program sám zjistí, jestli je to možné.  
✅ **Dynamická kontrola chyb** – už při diktování se zjistí, jestli operace dává smysl.  
✅ **Jednoduchá syntaxe** – stačí pár klíčových slov (`sečti`, `přidej`, `odečti`...)  

---

### **🔹 Jak by mohl fungovat vykonávací mechanismus?**
1. **Přečte se příkaz** – zjistí se úkon a objekty  
2. **Ověří se kompatibilita objektů** – pokud nejsou kompatibilní, vrátí chybu  
3. **Pokud jsou kompatibilní, vytvoří se nový objekt** s výsledkem operace  

Tohle by se dalo implementovat dost efektivně – například jednoduchý **parser**, který by podle klíčových slov rozpoznal, co má dělat, a pak jen kontroloval typy objektů v tabulce.

---

## **🔹 Shrnutí**  
✅ **Jasné a přirozené zadávání operací**  
✅ **Dynamická kontrola chyb podle typů objektů**  
✅ **Použití klíčových slov pro jednoznačné určení úkonu**  
✅ **Možnost rozšíření na další operace (např. násobení, dělení, porovnávání)**  

Myslím, že **tenhle přístup je extrémně intuitivní a zároveň efektivní**. Stačilo by jen vytvořit **seznam podporovaných úkonů** a definovat, **jaké kombinace objektů jsou povolené**. Máš už představu, **jak by se daly specifikovat složitější operace**? Třeba `sečti všechny objekty v seznamu` nebo `porovnej dva objekty a zjisti, který je větší`?

## Dotaz:

Takže jsem rád, že se ti to líbí. To, co tady píšeš úplně na konci, mě utvrdňuje v tom, že tomu smysl úplně rozumíš, protože takhle mi to přijde úplně jak bych si to představoval. Takže sečti všechny objekty v seznamu. Jasně dává instrukce sečit všechny objekty v seznamu a porovnej objekt ten a objekt ten a zjistí, který je větší, dává taky smysl. Pro dnešek už končím, já už jsem po vychádce doma, teď si musím zameditovat, ale super, díky moc, tohle je rozhodně parádní a nakonec bych ti poprosil, jestli bys mi to všechno, co jsme si tady spolu takhle připravili, bys mi mohl schrnout do nějakého jednoho celku, nemusí tam být všechno, ale ty základní věci, které jsme se tady dotkli, schnout do nějaké sumarizace, tak abych, až se na to podívám, dokázal se rychle chytit, kde jsme byli a mohl pokračovat dál. Každopádně ještě jenom moc díky a těším se na příště :-) 

## ChatGPT:

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

## Dotaz:

Tak už jsem zpátky a tentokrát u počítače :-)
Meditace byla prospěšná a tady je pár závěrů na které jsem během ní přišel :-)

1) Jako první by se měla vytvořit základní definice pro objekt, z které by vycházale všechny další objekty, ať už interní a nebo externí.
2) Základní definice pro objekt bude prázdný seznam.
3) První pole bude vždy vyhrazené pro objekt "name", který bude mít 2 pole: Jedno bude pro jméno objektu (takže "name") a druhé bude pro řetězec reprezentující jméno objektu ke kterému patří.
4) Vytvoření prázdného objektu bude probíhat výrazem:
Create object with name first object end name.
To se pak ve zkráceném zápisu půjde zapsat jako: 
"first object" = None
Což v pythonovském kodu by mohlo znamenat:
"object" = [["name", "first object"],]
5) Přizazení hodnoty by se dělalo přes objekt value a mohlo by se zapsat dodatečně:
Ad to object first object value 5.
nebo 
Ad value 5 to object first object.
což by se zase dalo přepsat jako
"object".append(["value", 5])
a struktura objektu by již vypadala:
"object" = [["name", "first object"], ["value", 5]]
6) Také by se hodnota dala přidělit rovnou při vytváření objektu:
Create object with name first object end name, and ad value 5.
Nebo
Create object with name first object end name, and with value 5.
Případně mě teď ještě napadlo, že namísto end name by stačilo jen znovu uvést slovo name a to by znamenalo ukončení zadávání jména, takže příkaz by zněl:
Create object with name first object name, and with value 5.
I když jak na to koukám, tak takto je to trochu matoucí, takže end name je asi lepší zachovat.
Takže tímto bychom vytvořili objekt který obsahuje dva objekty. Jeden pro jméno a druhý pro hodnotu.
7) Objektově bych pak rozličoval mezi hodnotou a textem, takže pro zadání textu by se použil objekt text:
Create object with name first object name end name, and with text ahoj všem end text.
Což by zase reprezentovalo:
"object" = [["name", "first object"], ["texts", "ahoj všem"]]
8) Podobně by se tedy vytvořili všechny další objekty jako třeba parametrs
Create object with name first object name end name, and with parametr color set to red, and parametr second color set to blue, end parametrs.
Což by zase reprezentovalo:
"object" = [["name", "first object"], ["parametrs", ["color", "red"], ["second color", "blue"]]]
Což by se tedy dalo zapsat:
"object" = [
    ["name", "first object"], 
    ["parametrs", 
        ["color", "red"], 
        ["second color", "blue"]
    ]
]
9) To už je zase jenom myšlenka navíc, že objekt name by se mohl staraat i o zprávu jmen objektů, takže by vyhledánání objektu probýhalo přes něj.
Takže kdybych v kodu použil:
Ad to object first object value 5.
Pak by se prohlída tokenizace všech name objektů což by mohl být zase seznam seznamů, kde ke každému tokenu jména by se přiřadil daný objekt a byl tak přístupný.
S tím že value by tedy reprezentovala číselnou hodnotu a dala by se tedy zapsat buď jako:
["value", 5]
Nebo jako desetiné číslo:
["value", 5, [decimal point, -2]]
Což by byl výraz pro 0.05

S tím zde je tedy vše v nejzákladnější formě, ale každý objekt by mohl mít neomezené množství polí, a jen by tak narůstala jeho složiost, která by byla ale přímo úměrná jeho účelu.
Jinými slovy základní operace jako vytvoření objektu odkazujícího na nějakou proměnnou nebo číselnou hodnotu by byli na nejnižší a tím pádem na nejrychlejší úrovni. A třeba taková definice třídy, která by měla několik položek v objektu parametry a pak několik položek v objektu funkce, by samozdžejměně měla složitější struktur - více do sebe zapuštěných seznamů, ale zase vše by bylo snadno přístupné, protože všechny parametry by byli v seznamu objektu parametry a všechny funkce by byli v seznamu objektu funkce. Což by asi taky mohlo i usnadnit jejich volání, kor, kdyby zde byl nějaký podobný tokenový mechanizmus i pro tyto objekty. A nebo je možné že by stačil jeden tokenový mechanizmus na jména objektů a hledat v nich. I když takto by vznikla množina všech jmen kde by se některé z různých objektů mohli i zdvojovat, takže toto by chělo více domyslet, ale nějak takto by to mohlo fungovat, že by tokenizace byla třeba taky objektová a tak by v seznamu za jménem tokenu moho být uveden nadřazený objekt, či nějaký jiný mechanizmus.

Co ty na to, můžeš mi tyto nápady nějak rozvést a zhodnotit a případně napsat zda tě napadá jak to ještě vylepšit a hlavně jestli je to takto i schůdné?

## ChatGPT:

Tohle je super myšlenkový rámec! Máš velmi dobře definovaný základní objektový systém, který umožňuje jednoduché a systematické rozšiřování. Pojďme si to trochu rozebrat, rozvést a podívat se na možné vylepšení.  

---

### **Shrnutí a analýza tvého návrhu**  

1. **Základní objektová struktura**  
   - Objekt je reprezentován jako seznam seznamů.  
   - První položka vždy obsahuje `["name", jméno_objektu]`.  
   - Další položky pak obsahují další atributy jako `["value", hodnota]`, `["text", text]`, `["parameters", ["color", "red"], ["second_color", "blue"]]`, atd.  

2. **Přístup k objektům podle jména**  
   - Jména objektů jsou spravována pomocí speciálního objektu (možná nějaký registr všech objektů).  
   - Vyhledávání probíhá přes tokenizaci jmen.  
   - Uvažuješ o přidání hierarchie (možnost propojit jméno objektu s nadřazeným objektem).  

3. **Zadávání hodnot**  
   - Možnost přiřadit hodnotu (`value`), text (`text`), nebo parametry (`parameters`).  
   - Hodnoty mohou být buď celá čísla, nebo desetinné (`["value", 5, [decimal point, -2]] → 0.05`).  
   - Přidání hodnoty může být dodatečné nebo součástí příkazu pro vytvoření objektu.  

4. **Přístup k atributům**  
   - Všechny parametry budou v sekci `parameters`, všechny funkce v sekci `functions`.  
   - Tento přístup usnadňuje organizaci a přístup k jednotlivým částem objektu.  

---

### **Co se mi na tom líbí**  
✅ **Modularita** – můžeš snadno přidávat další atributy a rozšiřovat objekty.  
✅ **Flexibilita** – systém umožňuje pracovat jak s hodnotami, tak i s textem nebo složitějšími strukturami.  
✅ **Tokenizace jmen** – umožňuje efektivní vyhledávání objektů podle názvu.  
✅ **Hierarchie a organizace** – oddělené sekce pro parametry a funkce dávají smysl.  

---

### **Návrhy na vylepšení**  

#### 1️⃣ **Zrychlení vyhledávání objektů**  
- Pokud budeš mít hodně objektů, vyhledávání přes seznam může být pomalé.  
- Možná by bylo lepší místo seznamu seznamů použít slovník `{jméno_objektu: objekt}`.  
  ```python
  objects = {
      "first object": {
          "name": "first object",
          "value": 5,
          "parameters": {
              "color": "red",
              "second color": "blue"
          }
      }
  }
  ```
- Tokenizace by pak mohla pracovat jako index pro rychlejší přístup.  

#### 2️⃣ **Struktura pro decimal point**  
- Místo `["value", 5, [decimal point, -2]]` by mohlo být jednodušší  
  ```python
  ["value", Decimal("0.05")]
  ```
- Použití `Decimal` (z `decimal` knihovny) zajistí přesnost a umožní snadnější operace.  

#### 3️⃣ **Zjednodušení syntaxe**  
- `Create object with name first object end name.` je trochu verbose. Možná by šlo použít:
  ```
  Create object: first object.
  ```
- `Ad value 5 to object first object.` → `Set first object.value = 5.`  

#### 4️⃣ **Rozšíření na objektově orientovaný přístup**  
Místo seznamu seznamů by bylo čistší použít třídu:  
```python
class Obj:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def set_value(self, key, value):
        self.attributes[key] = value
```
Použití:  
```python
obj = Obj("first object")
obj.set_value("value", 5)
obj.set_value("parameters", {"color": "red", "second color": "blue"})
```
Tohle by zpřehlednilo kód a umožnilo snadnější rozšiřování.  

---

### **Shrnutí návrhů**  
🔹 Použít slovník místo seznamu seznamů → rychlejší vyhledávání.  
🔹 Použít `Decimal` pro čísla místo vlastní reprezentace.  
🔹 Zjednodušit syntaxi příkazů.  
🔹 Možná zvážit objektově orientovaný přístup pro lepší organizaci.  

Co myslíš? Líbí se ti některý z těchto návrhů? 😊

## Dotaz:

Rozumím jak to myslíš a máš pravdu, jen jsme si nerozuměli v tom, že když jsem ycházel z toho, že objekt by byl seznam seznamů, že jsem tím myslel spíše odkaz na to, že všechny objekty by měli stejnou strukturu. Jedná se přeci jenom o nový přístup k tvorně jazyka a tak použití pythonvských tříd jako mezikroku je určitě dobrý nápad , nicméně kdyby se takto měla definovat každá hodnota tak v jednom kodu mám těch tříd tolik, že bych to ani nespočítal :-)

A každá třída sebou nese značnou zátěž, která pro reprezentaci jednoduchých proměnných není vůbec třeba. Veškeré procesy by byli deklarativní, takže by záleželo na tom zda objekt má value a nebo text, ale zase na druhou třídu by každý objekt měl mít minimum informací, aby byl lehký a nepřinášel overhed.

A i co se týká formulace, tak je mi jasné, že p té přestávce už asi nemáš v aktivní paměti to, že jsme se balili o tom, že jako první krok je potřeba vymyslet slovní příkazy, protože slovní zadávání kodu musí být jednoznačnné. A až teprve když bude tato logika začneme zápisi skracovat pro psanou fomru.

Co se mi ale líbí je možnost slovníku, kdy by každá objekt mohl být slovník s klíčem jako názvem a hodnotou, která by právě mohla být seznamem pro další objekty.
Takže bych ušetřil za objekt "name" protože jeho funkci by plnili klíče slovníků, takže vlastně každá objekt by mohl být slovníkem s klíčem jak jménem objektu a hodnotu v podobě seznamu pro další objekty, ať už je jím value, text, nebo třeba parametrs.

Co ty na to?

## ChatGPT:

Jo, teď už tomu rozumím líp! 😊 Takže hlavní cíl je:  
1) **Mít jednotnou strukturu pro objekty**  
2) **Udržet objekty co nejlehčí** (bez zbytečné režie tříd)  
3) **Definovat logiku přes přirozené slovní příkazy**  

A jo, slovníková struktura místo seznamu dává velký smysl!  

---

### 🔹 **Slovník jako základní objekt**
Pokud by každý objekt byl slovník, tak by vypadal třeba takto:  

```python
{
    "first object": {  
        "value": 5,  
        "text": "ahoj všem",  
        "parameters": {  
            "color": "red",  
            "second color": "blue"  
        }  
    }
}
```
Takže:
- **Jméno objektu je klíč slovníku** (tím pádem už nemusíš mít `["name", "first object"]` uvnitř)
- **Obsah objektu je zase slovník** (může obsahovat hodnotu, text, parametry, nebo další vnořené objekty)

Tohle má super výhody:
✅ **Přímý přístup k objektům přes klíče**  
✅ **Žádná zbytečná hierarchie** (dříve bylo `["name", "first object"]`, což byl seznam v seznamu)  
✅ **Lepší čitelnost i správa**  

---

### 🔹 **Přepisování slovních příkazů**
Tvůj původní příkaz:
```
Create object with name first object end name, and with value 5.
```
se dá přepsat do:
```python
objects["first object"] = {"value": 5}
```

A když přidáme další hodnoty:
```
Ad to object first object value 5.
Ad to object first object text ahoj všem end text.
Ad to object first object parametr color set to red.
```
bude:
```python
objects["first object"]["value"] = 5
objects["first object"]["text"] = "ahoj všem"
objects["first object"].setdefault("parameters", {})["color"] = "red"
```

Tím se vyhneš potřebě nějaké třídy a stále to zůstane maximálně flexibilní.

---

### 🔹 **Jak to ještě zjednodušit?**
- **Doplnit speciální datové typy pro čísla**  
    - Místo `["value", 5, [decimal point, -2]]` bych možná použil normální čísla (`5e-2` pro `0.05`)
    - Nebo zavést interní zápis jako `{"value": (5, -2)}`  
- **Zjednodušit tokenizaci**  
    - Hledání v objektech už půjde přímo přes `objects["jmeno"]`
    - Pokud potřebuješ fuzzy hledání, můžeš si udělat index slovníku

---

Tohle už je hodně lehká struktura a přitom dost silná. Jak se ti to líbí? 😊

## Dotaz:

Jo dává to smysl :-) Fandil jsem seznamům, ale sje pravda že slovník je ideální volba.
A jen tedy k číslům zápis s tuple (5, -2) byl odpočátku mojí volbou, jednak se tím člověk vyhne knihovně decimal, která sice počítá dobře a možná se bez ní neobejdu, ale na druhou stranu tento zápis se dvěma čísli (hodnota, pozice desetiné čárky) už mám taky ozkoušen, že dokáže velmi rychle počítat, takže bych mu chtěl dát přednost a decimal použít jen tam kde to bez něj nejde :-)

ALe super, tohle zatím stačí, a na další se vrhneme zase příště. 

teď už je pozdě a čeká mě večeře, takže pro dnešek dobrý. Moc děkuji za další posun a tedy zase zítra :-) :-) :-)

## ChatGPT:

Jasně, tuple `(hodnota, exponent)` je fajn volba, když chceš mít efektivní práci s čísly bez nutnosti tahat `decimal`. A když bude někdy potřeba extra přesnost, může se decimal použít jen tam, kde to fakt jinak nejde. Takže za mě super rozhodnutí! 😊  

Jsem rád, že jsme to zase posunuli o kus dál. Užij si večeři a odpočiň si, ať je zítra zase síla na další pokrok! 🎯  

Budu se těšit, měj fajn večer! 🍽️😎
