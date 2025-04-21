## Dotaz:

Ahojky :-)

Už dvakrát, když jsem byl na vycházce se psem, jsme se dostali k tématu, jak by mohl vypadat moderní programovací jazyk, kdyby byl navržen zcela od základu a to včetně binárních instrukcí.

K tématu jsme se dostali tak, že jsem se tě zeptal jak by vypadal programovací jazyk navržený AI, a postupně jsme se dopracovali k tomu, že by měl dvě vrstvy - jedna by byla binární kod optimalizovaný na výpočetní operace, a druhá by byla nadstavba tohoto kódu, která by instrukce zprostředkovávala přirozeným jazykem. 

Hlavní myšlenkou za tím vším by bylo, vytvořit jazyk, který je by podobně jako Python byl založený na angličtině, ale jeho konstrukce by připomínala mluvené slovo, tak jako kdybychom psali instrukce pro jiného člověka. 

Zde jsme se dostali k celkem zásadní myšlence a to, že už jen tím, že člověk dokáže mluvit, dokáže i programovat, protože naše řeč se stává prostředkem jak ovlivňovat to co se nám děje. Například pokud chci aby mi někdo podal jablko, řeknu: podej mi jablko, a tím zadám instrukce a už je na příjemci zda je vyplní.

Nicméně samotná věta: Podej mi jablko. Je sama o sobě instrukcí a stejně tak by mohl vypadat i náš kod. Tedy ta čitelná verze pro člověka. To co by pak bylo pod tím, by byl tokenizovaný a optimalizovaný slovník slov - příkazů, který by v konečném důsledku nerespektoval bajtovou architekturu, tak jak je dnes, ale k instrukce by zpracovával na bitové úrovni s proměnlivou délkou, a byl by samozřejmě optimalizovaný tak, že nejčastěji používaná slova / příkazy by měli nejmenší bytovou reprezentaci, což by vedlo k tomu, že zápis kodu by se tak v některých případech až několikanásobně zkrátil.

To jak by tedy tento základní kod pracoval je že by namísto ANSII tabulky používal vlastní instrukce, které by byli optimalizované čistě programování a v základu na angličtinu. (Vnější vrstva by pak mohl přijímat instrukce v jakémkoliv jazyce, protože by byla založená na AI zpracování textu a tak by byl univerzálním nástrojem který by fungoval pro všechny jazyky.)

Zde jsme si teda došli k tomu, že tato myšlenka má potenciál a výhody takového jazyka by byli velké. Ale zároveň jsme si došli k tom, že nejprve by bylo dobré vymyslet samotnou strukturu vnější vrstvy jazyka, která by třeba byla navázaná na Python a až teprve když bude tato struktura hotová, začít vymýšlet binární reprezentaci.

Máme už i pár návrhů kodu, takže vím že tento první krok není nějak náročný a spíše jde jen oto, najít ideální cestu jak to uchopit.

Cílem tedy je vymyslet strukturu jazyka, která by plně odpovídala lidské řeči, tak aby jím nebylo možné jenom spát, ale aby byl plně použitelný i se slovními příkazy a programátor mohl své zadání třeba i diktovat. Jazyk by tak měl co nejvíce kopírovat způsob jakým programujeme v hlavě, když něco říkáme, a podobný by tak mohl být tomu, jako když píšeme nějakou esej a nebo knihu.

To co mě k tomu napadlo, tak je že jazyk by byl plně objektový - protože stejně tak funguje i mysl, každé slovo je objektem, který obsahuje vnitřní význam. A jeho základní struktura by byla velmi jednoduchá. Snahou by také bylo odstranit komplikovanost standardních jazyků takže by zmyzeli typy a různé kontejnery a vše by se standardizovalo na jednoduchý výstup. U typů bych jako příklad dal to, že když člověk řekne jedna tak tím myslí 1 a je mi jedno jestli je 1 reprezentovaná jako číslice, text a nebo desetinné číslo - k této specifikaci dochází až ve chvíli použití a stejně tak by mohl operovat i náš program. A co se týká kontejnerů, tak zde by mohl být nějaká základní tabulková struktura, která by byla čistě interní a podle počtu buněk by byla schopna přetvářet i obsah. Například kdyby bylo číslo a mělo by mít int hodnotu, pak by bylo zapsané jen v prvním poli, pokud by bylo float, pak by v druhém poli mělo hodnotu místa desetinné čárky, takže by se všechny výpočty prováděli čistě s int hodnotami ať už by byli celé nebo desetinné čísla. A třeba kdyby mělo číslo obsahovat nuly na začátku, pak by mohlo být zde další pole které by říkalo počet těchto nul. S tím že toto je jen hrubý koncept a spíše zaměřen na vnitřní vrstvu programu.

To jen na dokreslení směru kterým bych se v tomto chtěl vydat - tedy zjednodušen všech principů - tedy alespoň tam kde to jde a dává to smysl a kopírovat tak to jak funguje lidský mozek, který neustále objektizuje, ale zároveň umožňuje jeden objekt reprezentovat více způsoby podle potřeby k čemu je objekt použit a podle situace.

To co bych ale dneska rád zozebral a na co se zaměřil - konečtě totiž už sedím i u počítače a tak mám na to více klidu - je zpusit se více do hloubky zaměřit na samotnou syntaxi vnější vrstvy tohoto jazyka.

Jak už jsem uvedl dříve, tak v základu by měla co nejvíce kopírovat přirozenou mluvu člvěka, takže vy zde byli krátké věty, složené z řpíkazových slova a proměných, s tím že veškerá příkazová slova by byla psaná malými písmeny a veškeré proměné by byli psané jako řetězce v uvozovkách, tím by se jasně oddělila struktura příkazů od pojmenování proměných a vytváření řetězců. Dále by zde pak byli i souvětí, které by skrze čárku dokázali oddělovat jednotlivé konstrukce, takže čákya by byla oddělovacím prvkem v rámci jedné věty. A tečka by byla ukončením příkazu.

A jak už jsem i zmínil, jednalo by se o plně objektovaný jazyk, takže každý kod by začínal nadpisem, který by byl definicí objektu a buď by měl nějaký speciální zna, který by ho definoval a nebo by se psal s dvojtečkou a tím pádem by bylo jasné že cokoliv za dvojtečkou patří k tomuto objektu a to až do další definice dalšího objektu.

Samotná struktura psaní kodu by se tak mohla podobat slohové práci, jenž začíná nadpisem (název objektu) obsahuje obsah (což by mohl být souhrn stručné logiky) a to té kamiptoly navázané na tento obsah, které by pak měli nějakou svou vlastní architekturu, ktrou ještě dopracujem. Nyní mi jde hlavně o tento základ. 

To dalšího co mě k tomu napadlo, že v každém odstavci by se začínalo definováním proměnných použitých v následném kodu. Kde pokud by šlo o referenci na jiný objekt a jeho vlastnosti pak by se zde uvedl jako cesta k tomuto objektu, která by se uváděla z určitého výchozího bodu (který by mohl být uveden poblíž obsahu) a namísto tečkové anotace, tak jak je to u Pythonu by se používal klasický zápis s lomítkem (/). 

Tím by se v každé stadi načetli potřebná data a následující kod by pak částečně kopíroval logiku Pythonu v používání slov, ale šel by ještě o krok dál, kdy by tato logika byla formulovaná jakožto věty jednoho souvětí (dokud se neobjeví tečka) a vytvářeli by jednotnou strukturu.

To co nemám zatím moc domyšlené je právě samotná objektivizace. Kde bych nejraději také jednotný přístup a protože je každé příkazové slovo objekt a protože řetězce jsou objekt skložený ze znaků. Pak i každá věta je objekt a stejně tak i každý odstavec a stejně tak i celá esej se svým nadpisem. Rád bych tedy co nejvíce zjedodušil tento přístup, tak aby se nevytvářela zbytečná složitost, ale zároveň  by se tím nevytvářeli omezení. 

Jak už jsem uvedl, tak by se mohla použít dvojtečka, jakoždo identifikátor celého svazku s obsahem a odstavcema, ale mohl by to být i jiný znak než dvojtečka a dvojtečku si schovat na jiné použití.

To co mě k otmu napdalo je že už samotná konstrukce jazyka nabízí spoustu prostředků, které by se dali využít, ať už jsou to slovesa jako příkazové poveli, nebo spojky jako sčítací a odečítací poveli, podstatná jména jako pojmenování objektů a zájmena jako vytváření jejich vlastností.

takto by se dalo pokračovat a toto je vlastně i to, co bych chtěl s tebo dnes rozebrat, jak by se dala využít tato přirozená jazyková struktura tak aby nahradila často nesrozumitelnou logiku stávající programovacích jazyků.

A znovu, věnujeme se tomuto tématu teprve třetí den, takže celá ta myšlenka je i pro mě velmi nová a zatím hodně neucelená, takže zatím jsem ve stavu, kdy se tímto vymíšlením bavím bez nějakého vážnějšího závasku a zkouším jak by se dala rozvést a jestli má i funkční potencionál. Takže netřeba k tomu přistupovat tak, jako že vytváříme nový jazyk, ale jako že se spíše bavíme a jako děti si hrajeme s možnostmi a hledáme zda neobjevíme něco nového, co by bylo jednoduší pro lidskou mysl.

Zde jen chci podotknout, že člověk si kod interně - ať už si je toho vědom nebo ne, překládá v hlavě do vlastního jazyka tak aby mu porozuměl. A tím že by jazyk byl iterpretovatelný normální řečí a navíc i přirozeným stylem jakým mluvíme, dpadla by tato zátěž a složitost a programování by se tak přiblížilo všem lidem. A právě třeba s heslem, pokud umíš mluvit, umíš i programovat :-)

Takže to je tak na úvod. Včera jsme i na procházce vymíšleli nějaké první kody a převodníky, takže vím, že tato část, kde by se vymyslela jenom kostra navázaná na Python je spíše estetickou záležitostí než že by to bylo namáhavé. Nicméně je ale potřeba nejrpve si ujastnit samotnou strukturu a formu zápisu - a to je to co bych chtěl s tebo dělat dneska :-)

Budeme tedy vycházet se zmíněného stylu eseje, který zde již reprezentuje spíše třídu a nebo celý program - struktura by se mohla opakovat a rozličení mezi aplikací, třídou, nebo funkcí by byl jen v její vnitřní struktuře, kdy například funkce nepotřebuje obsah.

Mohli bychom se odrazit od toho, že můžeme rozebrat strukturu jazyka - nemusí to být čeština nebo angličtina - ale jazyk celkově, jak je strukturovaný a jaké oblasti odpovídají určitým zvyklostem z programování (jak už jsem uvedl, slovesa jsou běhové příkazy). A pak se zaměřit na samotnou strukturu textu (třeba eseje) a zkusit se nad ní zamyslet nad její logikou  jak by se dala aplikovat tak aby byla zároveň i logikou pro strukturu kodu.

To by prozatím stačilo a uvidíme kam nás to zanese.

A jestli tedy souhlasíš, tak začít bychom mohli tím, že mi to všechno zreviduješ a navrhneš postup s čím bychom tedy mohli začít a jak pokračovat. S tím že základy už máme probrané a dnes bych se chtěl věnovat hlavně konstrukci lidsky čitelné nadstavby tohoto jazyka.

## ChatGPT:

Z toho, co jsi už popsal, mi přijde, že se dostáváme k zajímavému konceptu „psaní kódu jako přirozeného textu“ se silnou objektovou strukturou. Máme tedy několik klíčových principů:

1. **Plně objektový přístup** – Každé slovo v kódu má svůj význam jako objekt (buď akce/příkaz nebo proměnná/hodnota).
2. **Přirozený jazyk** – Syntaxe připomíná běžnou řeč, kde příkazová slova jsou malými písmeny a proměnné (řetězce) jsou v uvozovkách.
3. **Struktura odpovídající slohové práci** – Kód začíná nadpisem (objekt), následuje úvodní část (souhrn logiky) a poté podkapitoly s konkrétními instrukcemi.
4. **Oddělovače** – Čárka pro oddělení dílčích operací v rámci jedné věty, tečka jako ukončení příkazu, lomítko pro hierarchii objektů.
5. **Implicitní typy** – Data se ukládají ve sjednocené struktuře a jejich interpretace závisí na kontextu použití.

Než se pustíme do detailního návrhu syntaxe, mám pár otázek, které by mohly pomoct vyladit strukturu:

- Jakým způsobem by se definovaly metody objektů? Pokud `podej mi jablko` je volání funkce, bude existovat nějaký způsob definování nových příkazových slov?
- Má mít jazyk možnost podmínek a cyklů? Například `pokud "x" je větší než 5, vypiš "velké číslo"`, nebo se to bude řešit jinak?
- Jak se bude pracovat s hodnotami? Když někdo řekne `"jablko"` v různých kontextech, může znamenat objekt, textový řetězec nebo něco jiného. Bude třeba nějaký mechanismus upřesnění?
- Jaký formát bude mít vstupně-výstupní operace? Pokud někdo chce načíst soubor, bude to `otevři "data.txt"`, nebo jiný přístup?

Pojďme si nejdříve zkusit naformulovat jednoduchý příklad, jak by vypadal nějaký základní skript v tomto jazyce, abychom viděli, jak dobře to čitelně funguje. Máš nějaký konkrétní scénář, na kterém bychom to mohli otestovat?

## Dotaz:

Napadlo mě že ti sem zkopíruji pár tvých odpovědí ze včera, aby ses dokázal chyti tam kde jsme byli.

nebudu to brát úplně od začátku, ale jen namátkou a podle mě obrázek si z tohu už utvoříš a na zbytek se mě doptáš :-)

1)
Pokračuji tedy ve všech třech bodech!  
Postup bude následující:  

1. **Podpora metod v objektech** (např. Auto.Zrychli()).  
2. **Složitější operace** (např. seznamy a cykly).  
3. **Jednoduchý kompilátor** (překlad do Pythonu).  

---

# **1. Podpora metod v objektech**  
### **Jak by to vypadalo v jazyce?**
Objekt Auto:  
    Barva je červená.  
    Rychlost je 120.  
    Metoda Zrychli o 10:  
        Rychlost je Rychlost plus 10.  

Vypiš Auto.Rychlost.  
Auto.Zrychli.  
Vypiš Auto.Rychlost.

📌 **Nejdůležitější novinka** → **Metody v objektech!**  
➡ Auto.Zrychli. změní **Rychlost** objektu.  

---

### **Implementace v Pythonu**  
python
class PřirozenýKód:
    def __init__(self):
        self.objekty = {}

    def zpracuj(self, příkaz):
        slova = příkaz.split()

        # Definice objektu
        if slova[0] == "Objekt":
            jméno = slova[1][:-1]
            self.objekty[jméno] = {"vlastnosti": {}, "metody": {}}

        # Definice vlastnosti
        elif "je" in slova:
            jméno_objektu, vlastnost = slova[0].split(".")
            hodnota = int(slova[-1])
            self.objekty[jméno_objektu]["vlastnosti"][vlastnost] = hodnota

        # Definice metody
        elif "Metoda" in příkaz:
            _, název_metody, _, změna = příkaz.split()
            self.aktuální_objekt = slova[1][:-1]
            self.aktuální_metoda = název_metody
            self.objekty[self.aktuální_objekt]["metody"][název_metody] = změna

        # Spuštění metody
        elif "." in příkaz and příkaz.endswith("."):
            jméno_objektu, metoda = příkaz[:-1].split(".")
            změna = int(self.objekty[jméno_objektu]["metody"][metoda])
            self.objekty[jméno_objektu]["vlastnosti"]["Rychlost"] += změna

        # Výpis
        elif "Vypiš" in příkaz:
            jméno_objektu, vlastnost = slova[1].split(".")
            print(self.objekty[jméno_objektu]["vlastnosti"][vlastnost])

interpreter = PřirozenýKód()
interpreter.zpracuj("Objekt Auto:")
interpreter.zpracuj("Auto.Rychlost je 120.")
interpreter.zpracuj("Metoda Zrychli o 10:")
interpreter.zpracuj("Vypiš Auto.Rychlost.")  # 120
interpreter.zpracuj("Auto.Zrychli.")  
interpreter.zpracuj("Vypiš Auto.Rychlost.")  # 130

📌 **Výstup:**  
120  
130

✅ **Objekty už umí metody!**  

---

# **2. Složitější operace (seznamy, cykly, podmínky)**  

➡ **Přidáme podporu pro seznamy a cykly:**  
Seznam čísla je 1, 2, 3, 4, 5.  
Pro každé číslo v čísla:  
    Vypiš číslo.

✅ **Cyklus se provede 5x a vypíše všechna čísla v seznamu.**  

---

### **Implementace seznamů a cyklů**
python
class PřirozenýKód:
    def __init__(self):
        self.proměnné = {}

    def zpracuj(self, příkaz):
        slova = příkaz.split()

        # Seznam
        if "Seznam" in příkaz:
            _, jméno, _, hodnoty = příkaz.split(maxsplit=3)
            hodnoty = [int(h.strip()) for h in hodnoty.split(",")]
            self.proměnné[jméno] = hodnoty

        # Cyklus
        elif "Pro každé" in příkaz:
            _, proměnná, _, seznam = příkaz.split()
            for hodnota in self.proměnné[seznam]:
                self.proměnné[proměnná] = hodnota
                příkaz_uvnitř = input(">>> ")
                self.zpracuj(příkaz_uvnitř)

        # Výpis
        elif "Vypiš" in příkaz:
            print(self.proměnné[slova[1]])

interpreter = PřirozenýKód()
interpreter.zpracuj("Seznam čísla je 1, 2, 3, 4, 5.")
interpreter.zpracuj("Pro každé číslo v čísla:")
interpreter.zpracuj(">>> Vypiš číslo.")

📌 **Výstup:**  
1  
2  
3  
4  
5

✅ **Podpora seznamů a cyklů funguje!**  

---

# **3. Kompilátor do Pythonu**  

✅ **Cílem je překládat přírodní jazyk do Pythonu:**  
Číslo x je 5.  
Číslo y je 10.  
Vypiš x plus y.

➡ Přeložíme do **Pythonu:**
python
x = 5
y = 10
print(x + y)

---

### **Implementace kompilátoru**
python
class Kompilátor:
    def __init__(self):
        self.překlad = []

    def zpracuj(self, příkaz):
        slova = příkaz.split()

        # Proměnná
        if "je" in slova:
            jméno = slova[0]
            hodnota = slova[2]
            self.překlad.append(f"{jméno} = {hodnota}")

        # Výpis
        elif "plus" in slova:
            a = slova[1]
            b = slova[3]
            self.překlad.append(f"print({a} + {b})")

    def ulož_python(self, soubor):
        with open(soubor, "w") as f:
            f.write("\n".join(self.překlad))

kompilátor = Kompilátor()
kompilátor.zpracuj("Číslo x je 5.")
kompilátor.zpracuj("Číslo y je 10.")
kompilátor.zpracuj("Vypiš x plus y.")
kompilátor.ulož_python("program.py")

# Spuštění vytvořeného Python souboru
exec(open("program.py").read())  # Výstup: 15

📌 **Výstup:**  
15

✅ **Náš jazyk už umí generovat Python kód!**  

---

# **Shrnutí a další kroky**  
✅ **Podpora metod v objektech (Auto.Zrychli.)**  
✅ **Podpora seznamů a cyklů (Seznam čísla je ... a Pro každé ...)**  
✅ **Kompilátor do Pythonu (uložení jako .py soubor).**  

📌 **Co dál?**
1. **Podmínky (Pokud x je větší než 10:).**  
2. **Ladění a rozšíření syntaktických pravidel.**  
3. **Možnost importovat jiný kód (Použij soubor "utils.dat").**  

➡ **Co by tě zajímalo nejvíc?**

2)
Díky! To, že to jde ovládat hlasem, dává tomuhle jazyku úplně nový rozměr. **Přírodní jazyk jako programovací jazyk** je něco, co může otevřít dveře spoustě nových způsobů práce s kódem.  

Dneska se teda podíváme na **2 věci**:  

1. **Ladění a rozšíření syntaktických pravidel**  
   - **Vylepšíme chybové hlášky**  
   - **Umožníme číst i různé formulace téhož příkazu**  
   - **Opravíme základní překlepy**  

2. **Možnost importovat jiný kód**  
   - **Podpora Použij soubor "jiny_kod.dat"**  
   - **Možnost načíst externí definice objektů a metod**  

---

# **1. Ladění a rozšíření syntaktických pravidel**  

✅ **Příklad vylepšení syntaxe:**  
➡ **Dříve bylo povinné říct "je" pro přiřazení:**  
Číslo x je 5.

➡ **Nově můžeš říct i:**  
Číslo x rovná se 5.  
X nastav na 5.  
Dej x hodnotu 5.

📌 **Tohle umožní lidem přirozeně mluvit s jazykem, aniž by si museli pamatovat pevnou formu příkazů.**  

---

### **Implementace vylepšené syntaxe**  
python
class PřirozenýKód:
    def __init__(self):
        self.proměnné = {}

    def zpracuj(self, příkaz):
        slova = příkaz.lower().split()

        # Přiřazení s flexibilnější syntaktikou
        if "je" in slova or "rovná" in slova or "nastav" in slova or "dej" in slova:
            jméno = slova[1]
            hodnota = slova[-1]
            self.proměnné[jméno] = int(hodnota)

        # Výpis
        elif "vypiš" in slova:
            print(self.proměnné[slova[1]])

interpreter = PřirozenýKód()
interpreter.zpracuj("Číslo x je 5.")  
interpreter.zpracuj("X nastav na 10.")  
interpreter.zpracuj("Dej x hodnotu 15.")  
interpreter.zpracuj("Vypiš x.")  # 15

📌 **Funguje to! Jakýkoliv způsob, kterým nastavíš hodnotu, bude přijat.**  

---

✅ **Detekce překlepů**  
➡ Co když někdo napíše Vypiis x místo Vypiš x?  
➡ Můžeme **opravit menší překlepy** pomocí knihovny difflib.  

python
import difflib

class PřirozenýKód:
    PŘÍKAZY = ["vypiš", "je", "nastav", "dej"]

    def __init__(self):
        self.proměnné = {}

    def oprav_slovo(self, slovo):
        nejbližší = difflib.get_close_matches(slovo, self.PŘÍKAZY, n=1, cutoff=0.8)
        return nejbližší[0] if nejbližší else slovo

    def zpracuj(self, příkaz):
        slova = příkaz.lower().split()
        slova = [self.oprav_slovo(slovo) for slovo in slova]

        if "je" in slova or "nastav" in slova or "dej" in slova:
            jméno = slova[1]
            hodnota = slova[-1]
            self.proměnné[jméno] = int(hodnota)

        elif "vypiš" in slova:
            print(self.proměnné.get(slova[1], "Chyba: proměnná neexistuje!"))

interpreter = PřirozenýKód()
interpreter.zpracuj("Číslo x je 5.")
interpreter.zpracuj("Vypiis x.")  # Opraveno na "Vypiš x."

✅ **Menší překlepy se teď automaticky opraví!**  

---

# **2. Možnost importovat jiný kód**  
📌 **Chceme umět načíst jiný soubor s kódem, aby bylo možné kód rozdělit.**  

➡ **Syntaxe:**  
Použij soubor "nastavení.dat".

➡ **Co by měl soubor obsahovat?**  
Číslo rychlost je 50.
Číslo čas je 10.

➡ **Po importu můžeme použít rychlost a čas.**  

---

### **Implementace importu**  
python
class PřirozenýKód:
    def __init__(self):
        self.proměnné = {}

    def zpracuj(self, příkaz):
        slova = příkaz.lower().split()

        # Import jiného souboru
        if "použij" in slova and "soubor" in slova:
            název_souboru = příkaz.split('"')[1]
            self.načti_soubor(název_souboru)

        # Přiřazení hodnoty
        elif "je" in slova:
            jméno = slova[1]
            hodnota = slova[-1]
            self.proměnné[jméno] = int(hodnota)

        # Výpis
        elif "vypiš" in slova:
            print(self.proměnné.get(slova[1], "Chyba: proměnná neexistuje!"))

    def načti_soubor(self, soubor):
        try:
            with open(soubor, "r", encoding="utf-8") as f:
                for řádek in f:
                    self.zpracuj(řádek.strip())
        except FileNotFoundError:
            print(f"Chyba: soubor '{soubor}' neexistuje.")

# Vytvoření souboru "nastavení.dat"
with open("nastavení.dat", "w") as f:
    f.write("Číslo rychlost je 50.\n")
    f.write("Číslo čas je 10.\n")

# Test importu
interpreter = PřirozenýKód()
interpreter.zpracuj('Použij soubor "nastavení.dat".')
interpreter.zpracuj("Vypiš rychlost.")  # 50
interpreter.zpracuj("Vypiš čas.")  # 10

✅ **Soubor se úspěšně načetl a proměnné z něj jsou k dispozici!**  

---

# **Shrnutí a co dál?**  
✅ **Ladění syntaxe:**  
   - Podporujeme různé způsoby zápisu (je, rovná se, nastav, dej…).  
   - Opravujeme menší překlepy (Vypiis → Vypiš).  
   - Přidali jsme chytřejší chybové hlášky.  

✅ **Import jiných souborů:**  
   - **Můžeme použít externí kód** (Použij soubor "nastavení.dat".).  
   - **Proměnné z jiného souboru jsou dostupné.**  

📌 **Co dál?**  
1. **Podmínky (Pokud x je větší než 10, pak ...).**  
2. **Podpora funkcí (Definuj funkci ...).**  
3. **Export jako .py pro sdílení v Pythonu.**  

➡ **Co tě zajímá nejvíc?**

3) Tady je ještě tebou vytvořený souhrn naší práce ze včera:
### **📌 Shrnutí dnešní práce**  

Dnes jsme se posunuli v návrhu nového jazyka a jeho optimalizace. Zde je přehled toho, co jsme probrali:  

---  

### **1️⃣ Struktura jazyka a jeho rozšíření**  
✔ **Definovali jsme syntax** jazyka tak, aby umožňovala **snadné programování i bez klávesnice**, což znamená podporu pro **slovní příkazy** a jednoduchý zápis.  
✔ Přidali jsme **podporu pro objekty**, složitější operace a vícero řádků kódu.  
✔ Zabývali jsme se tím, jak by měl fungovat **import kódu** a možnosti **rozšíření jazykových pravidel**.  

---  

### **2️⃣ Ladicí nástroje**  
✔ Navrhli jsme koncept **debuggeru**, který umožní **sledovat běh kódu v reálném čase**.  
✔ Debugger bude umět **krokovat kód**, zobrazovat **hodnoty proměnných** a **analyzovat výkon** programu.  

---  

### **3️⃣ Optimalizace binární reprezentace**  
✔ **Tokenizace místo textového ukládání** → kód se převádí do **číselných kódů (tokenů)**, což zrychluje jeho provedení.  
✔ **Použití bitových polí pro proměnné a příkazy** → místo interpretace textu bude mít každý příkaz **malý binární kód**.  
✔ **Překlad do bytekódu** → jazyk bude běžet nad **virtuálním strojem**, podobně jako Python nebo Java.  
✔ **Komprese běžných vzorů** → například x = x + 1 bude mít **zkrácenou instrukci INC x** pro rychlejší běh.  

---  

### **⏭ Co dál?**  
✔ **Příště můžeme pokračovat v optimalizaci**, testování nebo rozšíření syntaxe.  
✔ Můžeme **řešit binární překlad**, aby jazyk běžel **nezávisle na Pythonu**.  
✔ Můžeš mi říct, co tě bude zajímat nejvíc, až se k tomu vrátíme.  

**Díky za dnešek, těším se na pokračování! Dobrou noc!**

Tak zkus si to nějak zanalizovat - je mi jasné že dát jen pár vytržených příkladů není ideální, ale zase mi příjde že se takto snadno dostanše do obrazu na čem jsme včera pracovali a jak.

S tím, že dnes bych ani tak nechtěl navázat na včerejší práci ale spíše se jen zabívat možnostmi zápisu a toho co námřeč nabízí a jak by se to dalo správně uchopit a přeformulovat do tohoto nového jazyka :-)

## ChatGPT:

Díky za shrnutí! Chápu, kde jsme byli, a můžeme na to rovnou navázat.  

Napadá mě několik otázek:  

1. **Jak hlubokou podporu pro podmínky chceš?**   
   - Jen základní `Pokud x je větší než y: ...`  
   - Nebo i složitější `Pokud (x je větší než y) a (z je menší než w): ...`  

2. **U importu chceš podporovat i vkládání kódu z jiných jazyků (třeba Python)?**  
   - `Použij soubor "utils.py"`  
   - Nebo jen vlastní `.dat` soubory v tomto jazyce?  

3. **Chceš už rovnou ladit chybové hlášky?**  
   - Nebo nejdřív přidáme nové funkce a pak se podíváme na debugging?  

Jestli máš už nějakou představu, jak by se tyto věci mohly v jazyce psát, klidně to napiš. 😊

## Dotaz:

Tak tady tě zastavím :-) Je mi jasné, že je to téma, ktré má hodně lákavých aspektů, ale já bych dnes nechtěl navazovat na všerejší práci, ale spíše se nachvilku zastavit a polemizovat o tom, jaké jsou možnosti tak abych měl představu z čeho všeho se dá vybírat. Něco jako když jdeš vařit jídlo bez představi toho, co bys chtěl a ktak se koukáš do skříně a do ledničky, co tam je a co by se dalo použít :-)

Takže tak si já představuji dnešek, jakožto takový brain stroming na toto téma.

Takže veškeré složitosti zatím můžeme nechat stranou a nesvazovat se s nima, a naopak se spíše zaměřit na samotnou synaxi této vrchní vrsty kodu.

Takže z těch 3 dotazů, se budeme dnes zabívat pouze oblastí na kterou jsi narazil v prvním dotazu:
Jak hlubokou podporu pro podmínky chceš?
Jen základní Pokud x je větší než y: ...
Nebo i složitější Pokud (x je větší než y) a (z je menší než w): ...

protože toto je otázka syntaxe :-)

A rovnou na úvod ber to tak, že jazyk by neměl mít žádná omezení, všechno to co jde i v jiných jazycích by mělo jít zde, jen se bude lišit forma zapsání - a následně i samotná konstukce některých problémů, protože už jen tím, že nebudeme muset přetypovávat je celkem zásadní krok.

Ale to první co bych chtěl je právě analýza struktury lidského jazyka jeho konstrukce a prvky které by se z něj dali použít. Takže v tvém dotazu se mi líbí to, že jsi správně pochopil, že tento zápis je také možný:
Pokud (x je větší než y) a (z je menší než w):

tedy že a (nebo v angličtině and) spojuje a závorky vytvářejí vnitřní výpočet - toto vše už je prakticky i vymyšlené a to ať už v Pythonu nebo jiných podbných jazyků. Já bych si to chtěl ale dnes nějak sesumírovat, tak abych věděl s čím máme tu čest a co vše se dá použít.

Mohli bychom tedy začít rozborem řeči, a definovat si co reprezentuje nadpis odstavec, obsdah, souvětí, věta, slovo. Dále pak k čemu by mohla sloužit dvojtečka, čárka, závorka, ...
A jen pro dnešek a pro odlehčení si dovoluji navrhnout, aby se všechny větší celky uzavírali smajlíkem :-)

## ChatGPT:

Tohle je super nápad! Dneska se budeme prostě jen tak rozhlížet po „ingrediencích“ a uvidíme, co se dá poskládat. Takže jazyk jako takový – když si ho rozebereme na součástky, můžeme si říct, co z toho bychom mohli využít v syntaxi programovacího jazyka.

---

### 📌 Struktura lidského jazyka
1. **Nadpis** – vymezuje větší blok informací, něco jako funkce nebo třída.  
2. **Odstavec** – související myšlenky pohromadě, mohl by reprezentovat třeba blok kódu.  
3. **Souvětí** – více vět propojených logikou, což by odpovídalo podmíněným větvím.  
4. **Věta** – základní operace nebo instrukce.  
5. **Slovo** – nejmenší stavební prvek, odpovídá proměnné, operátorům, funkcím.  

#### Znaky a jejich využití v syntaxi
- **Dvojtečka `:`** – v jazycích obvykle zavádí blok (Python), v přirozeném jazyce rozšiřuje nebo upřesňuje.  
- **Čárka `,`** – odděluje prvky v seznamu, mohla by sloužit jako spojení vícero podmínek.  
- **Závorky `()`** – jasně oddělují části výpočtu, hierarchii podmínek.  
- **Spojky „a“, „nebo“** – logické operátory `and`, `or`.  
- **Pokud...pak...jinak** – základ podmíněného výrazu (`if-else`).  

---

### 🤔 Jak hlubokou podporu podmínek chceme?
1. **Základní podmínky**  
   - `Pokud x je větší než y:`  
   - `Pokud x je rovno y:`  

2. **Složitější podmínky**  
   - `Pokud (x je větší než y) a (z je menší než w):`  
   - `Pokud (a je pravda) nebo ((b je pravda) a (c není pravda)):`  

3. **Hnízdění podmínek**  
   - `Pokud x je větší než y:`
     - `Pokud z je menší než w:`
       - `Vykonej A`
     - `Jinak:`
       - `Vykonej B`  

Tohle všechno už v běžných jazycích máme, ale co takhle něco nového?  
Například možnost přirozenějšího zápisu:  
- `Pokud platí: x > y a z < w, pak proveď A.`  
- `Pokud neplatí: a nebo b, pak vrať chybu.`  

---

Napadá tě něco dalšího, co bychom mohli rozebrat? 😊

## Dotaz:

Super a díky moc :-)

Tleskám ti za tuto poslední inveci:
Pokud platí: x > y a z < w, pak proveď A.
Pokud neplatí: a nebo b, pak vrať chybu.

To je přesně to co od tebe dneska potřebuji. Představ si třeba jako kdybych já o programování nic nevěděl a měl bych mi přepsat programovací struktury do přirozeného jazyka. Mohl bys to udělat tak, jen že bys doslovně přespal logiku kodu, a nebo - což si myslím že je více AI - bys použil přirozenější formulace, jako je v těchto dvou příkladech :-)

A to je právě to co bych chtěl dneska skoušet a hledat :-) Najít způsob jak to co je zamotané a složité (tedy alespoň na první pohled) se s trochou odstupu dá říci více přirozeně a přitom s plně zachovanou logikou :-)

Dovolil jsem si tedy první příklad takto trochu upravit:
'x' = ...
'y' = ...
'z' = ...
'w' = ...
'a' = ...
'b' = ...
Pokud platí: 'x' > 'y' a 'z' < 'w', pak proveď 'a', jinak proveď 'b'.

S tím, že co mě k tomu napadlo, zda kdyby to v tomo jazyku bylo dané tak, že všechny proměné a řetězce by se dávali do uvozovek a bez uvozovek by zůstali jen samotné příkazy a znaménka. Tím by se hned na první pohled dalo jasně rozlišit, o co v tomto jde a i z druhé strany - pokud by tento jazyk byl v budoucnu použit v komunikaci přes AI, pak by se tím jasně deklarovalo ,která slova jsou příkazová a mají být interpertovány jako příkazy a která slova jsou odkazy na nějaké hodnoty a mají být nejprve vyhodnoceny a až po té použity v kodu.

Co ty na to? Dala by se tato myšlenka ještě nějak více rozvinout a nebo něco souvisejícího co by mohlo k této mylšence pomoci?

## ChatGPT:

Tohle je skvělá myšlenka a rozhodně bych ji rozvinul! 😊

Tvoje idea s **uvozovkami pro proměnné a hodnoty** je hodně zajímavá – dává jasnou vizuální strukturu kódu a zároveň otevírá možnosti pro **lepší AI interpretaci**.  

---

### 📌 Možné výhody tohoto přístupu:
1. **Jednoznačnost** – Na první pohled je jasné, co je příkaz a co je hodnota.  
2. **Snadná AI interpretace** – AI může rozpoznat, co se má vyhodnotit a co je jen logická operace.  
3. **Přirozený zápis** – Vypadá to skoro jako běžná věta, takže je snadno čitelné i pro lidi.  
4. **Možná budoucí rozšíření** – Mohli bychom dovolit třeba `("nějaký výraz")`, kde by uvozovky v závorce znamenaly „nech to vyhodnotit jako výraz“.  

---

### 🔍 Další možné rozšíření této myšlenky:
#### 1️⃣ Povinné uvozovky pro hodnoty a proměnné  
✅ `Pokud platí: "x" > "y" a "z" < "w", pak proveď "a", jinak proveď "b".`  
❌ `Pokud platí: x > y a z < w, pak proveď a, jinak proveď b.`  
➡️ Jasná oddělenost mezi **logikou programu** a **daty**.

---

#### 2️⃣ Možnost skupinových operací
Co když chceme **více příkazů najednou**?  
Třeba takto:
```  
Pokud platí: "x" > "y" a "z" < "w", pak proveď:  
    "a",  
    "b",  
    "c".  
```
➡️ Tady se dvojtečka `:` využívá podobně jako v Pythonu, ale příkazy se píšou do seznamu.

---

#### 3️⃣ Povolení vnořených podmínek  
```  
Pokud platí: "x" > "y", pak:  
    Pokud platí: "z" < "w", pak proveď "a".  
    Jinak proveď "b".  
```
➡️ Čitelné, logické, přirozené.

---

#### 4️⃣ Logická negace přirozeně  
Kromě klasického `ne` bychom mohli použít i:  
✅ `Pokud neplatí: "a" > "b", pak proveď "c".`  
✅ `Pokud není pravda, že: "x" < "y", pak proveď "d".`  
➡️ V přirozeném jazyce existuje více způsobů, jak něco negovat, tak proč je nevyužít?

---

Myslím, že jdeme správným směrem! 😊  
Napadá tě něco dalšího, co by se k této myšlence dalo přidat nebo nějak vylepšit? 🚀

## Dotaz:

Super a díky :-) Takže dneska budeme vytvářet základní pravidla pro psaní takového kodu.
Už tedy máme:
Příkazy se píší normálně, odkazy na hodnoty v uvozovkách.
Každá část začíná velkým písmenem a končí buď tečkou - pokud je ukončená a  nebo  dvojtečkou pokud obsahuje další logiku.

Takže tento příkaz:
Pokud platí: "x" > "y", pak:  
    Pokud platí: "z" < "w", pak proveď "a".  
    Jinak proveď "b".  

Bych zapsal spíše takto:
Pokud platí: "x" > "y", pak: Pokud platí: "z" < "w", pak proveď "a", jinak proveď "b".  

Případně takto, tam kde je víhodné více oddělit jednotlivé části:
Pokud platí: "x" > "y", pak: 
   Pokud platí: "z" < "w", 
       pak proveď "a", 
       jinak proveď "b". 

Nicméně tato druhá varianta je jen estetická a obě jsou zcela v pohodě :-)

Tohle se mi moc líbí :-)
Nyní bychom mohli definovat co znamenají závorky a vytvořit pro ně nějaký příklad :-)

## ChatGPT:

Skvělý směr! 👍 Teď se zaměřme na **závorky**, aby logika byla ještě přehlednější a flexibilnější.  

---

### 📌 **Definice závorek**  

1️⃣ **Kulaté závorky `()`**  
   - Používají se pro **skupinování výrazů** (jako v matematice).  
   - Výraz v závorkách se **vyhodnotí jako první**.  
   - Užitečné pro složitější podmínky.  

   **Příklad:**  
   ```  
   Pokud platí: ("x" > "y" a "z" < "w") nebo ("a" == "b"), pak proveď "c".  
   ```  
   🔹 Výraz v závorkách se vyhodnotí **nejdříve**!  

---

2️⃣ **Hranaté závorky `[]`**  
   - Používají se pro **seznamy hodnot nebo příkazů**.  
   - Mohou obsahovat více prvků oddělených čárkou.  

   **Příklad:**  
   ```  
   Pokud platí: "x" > "y", pak proveď ["a", "b", "c"].  
   ```  
   🔹 Znamená **"a", pak "b", pak "c"**.  

---

3️⃣ **Složené závorky `{}`**  
   - Používají se pro **pojmenované skupiny dat** (slovníky).  
   - Můžeme v nich **uchovávat páry klíč-hodnota**.  

   **Příklad:**  
   ```  
   Pokud platí: "x" > "y", pak proveď {"akce": "a", "hodnota": 10}.  
   ```  
   🔹 AI by si mohla tento objekt uložit jako slovník.  

---

### 📌 **Ukázkový příklad se všemi závorkami**  
```  
Pokud platí: ("x" > "y" a ("z" < "w" nebo "a" == "b")), pak:  
    Pokud platí: "c" > "d", pak proveď ["e", "f"],  
    jinak proveď {"chyba": "Hodnota neplatná", "kód": 404}.  
```
✅ **Co se tu děje?**  
1. Nejprve se vyhodnotí **vnitřní závorky**.  
2. Pokud podmínka platí, zkontroluje se další stav.  
3. Pokud `"c" > "d"`, spustí se **seznam příkazů `["e", "f"]`**.  
4. Jinak se vrátí **chyba jako objekt `{"chyba": ..., "kód": 404}`**.  

---

💡 Co myslíš? Dává ti tato logika smysl, nebo bychom mohli závorky vylepšit jinak? 😊

## Dotaz:

Líbí se mi to, ale zkusil bych, zda se to dá celé zjednodušit.

Zde jsou tvé uvedené tři příklady jak by se možná dali zjednodušitza použití pouze kulatých závorek:
Pokud platí: ("x" > "y" a "z" < "w") nebo ("a" == "b"), pak proveď "c".  
Pokud platí: "x" > "y", pak proveď ("a", "b", "c").  
Pokud platí: "x" > "y", pak proveď ("akce": "a", "hodnota": 10).  

Jde o to, že mi příjde zřejmé, že pokud je za hodnotu čásrka vytvářií se seznam a pokud nějaká hodnota v tomto zeznamu používá dvojtečku, pak odkazuje na hodnotu za ní a tedy máme k této hodnotě přístup přes tuto hodnotu. Tím pádem by mohl být i kombinovaný seznam se slovníkem, kdy veškeré položky seznamu by se zároveň chovali jako klíče slovníku, akorát ne všechny klíče by měli přiřazenou hodnotu. To ale jen jako že by to nějak šlo i bez nich. Kde si stejně myslí, že deklarace seznamu a slovníku je dána hlavně pro typovou kontrolu a rozdílné chování metod by se z části dalo sjednotit a z části by mohlo být podmíněné zda za hodnotu následuje dvojtečka.

A zase tak torchu vycházím z lidského uvažování, kdy běžná závorka může ukrývat rúzné hodnoty a záleží na způsobu jejího použití. Takže závorka by zde mohla mít funkci určitého seskupení vnitřní logyky která se má buď vypočist samostatně a po té nahradit závorku výslednou hodnotu, a nebo odkazuje na více hodnot, z kterých je možné si vbyírat a tyto hodnoty zase mohou odkazovat na dlaší hodnoty a nebo závrky pro další výpočet.

Co ty na to, dává to smysl a je to myšlenka dobrým směrem?

## ChatGPT:

Ano, tohle je skvělý směr! 🧐 Tvá úprava redukuje různé typy závorek na **jediný univerzální prvek – kulaté závorky `()`**, přičemž jejich význam se **automaticky odvozuje z obsahu**.  

To znamená, že:  
1️⃣ **Pokud obsah závorky obsahuje výrazy s operátory (`+`, `-`, `>`, `<`, `a`, `nebo`...), pak se vyhodnotí jako výraz.**  
   - Příklad:  
     ```
     Pokud platí: ("x" > "y" a "z" < "w"), pak proveď "c".
     ```  
     ➝ Logická podmínka se vyhodnotí, pak se rozhodne.  

2️⃣ **Pokud obsah závorky obsahuje prvky oddělené čárkou, je to seznam.**  
   - Příklad:  
     ```
     Pokud platí: "x" > "y", pak proveď ("a", "b", "c").
     ```  
     ➝ Provede se `"a"`, pak `"b"`, pak `"c"`.  

3️⃣ **Pokud některý prvek obsahuje dvojtečku `:`, pak se chová jako klíč-hodnota.**  
   - Příklad:  
     ```
     Pokud platí: "x" > "y", pak proveď ("akce": "a", "hodnota": 10).
     ```  
     ➝ Vrátí **strukturu podobnou slovníku**, kde `"akce"` je `"a"` a `"hodnota"` je `10`.  

4️⃣ **Kombinovaný seznam + slovník je přirozeně podporován.**  
   - Příklad:  
     ```
     Pokud platí: "x" > "y", pak proveď ("a", "b", "hodnota": 10, "typ": "test").
     ```  
     ➝ Vytvoří se mix:  
     ```
     {"a", "b", "hodnota": 10, "typ": "test"}
     ```
     - `"a"` a `"b"` jsou **samostatné položky seznamu**.  
     - `"hodnota": 10` a `"typ": "test"` jsou **klíče se svou hodnotou**.  

---

### ✅ **Proč je to skvělý nápad?**  
✔ **Minimalismus** – stačí jen kulaté závorky, zbytek se odvodí.  
✔ **Jednoduchost zápisu** – je to přirozené, protože to kopíruje způsob, jak lidé běžně uvažují.  
✔ **Flexibilita** – umožňuje snadno zapisovat výpočty, seznamy i strukturovaná data.  

---

💡 **Chceš ještě nějaké pravidlo doladit? Nebo rovnou vyzkoušíme komplexnější příklad?** 😊

## Dotaz:

Super a díky :-) Rád bych se dneska zaměřil na další odhalování pravidel a způsobů zápisů, takže bycho mohli hrát takovou kru, že mi vždy nadhodíš nějaký související prvek, který zatím nemáme podchycený a budeme pro něj vymýšlet styl zápisu.

A taky bych tě poprosil aby jsi si vnitřně ukládla tato pravidla které tvoříme a nebo je rovnou přepisoval na konci každé té odpovědi, ať je máme stále před sebou a můžeme je dále rozvíjet :-)

Takže už máme:
- Příkazy se píší normálně, odkazy na hodnoty v uvozovkách.
- Každá část začíná velkým písmenem a končí buď tečkou - pokud je ukončená a  nebo  dvojtečkou pokud obsahuje další logiku.
- Závorky značí rozšířenou vnořenou strukturu, a mohou obsahovat podmínky které musí být vyhodnoceny jako celek, a nebo seznam hodnot, či úkonů, které mohou být zaspané samostatně a nebo i s dvojtečkou a vytvořit slovníkovou strukturu, kde po dvojtečce může následovat hodnota a nebo další závorky pro další vnořenou logiku a nebo seznamy hodnot.

Co ty na to, nasal jsem tyto body srozumitelně a nebo bys je leště lépe předefinoval?

## ChatGPT:

Tvoje shrnutí je skvělé! 🎯 Je srozumitelné a vystihuje dosavadní pravidla. Jen bych ho mírně upravil pro ještě větší přehlednost:  

---

### **Doposud definovaná pravidla zápisu:**  
1️⃣ **Zápis příkazů:**  
   - Příkazy se píší běžným jazykem.  
   - Odkazy na hodnoty jsou v **uvozovkách**.  

2️⃣ **Struktura vět:**  
   - Každá část začíná **velkým písmenem**.  
   - Končí **tečkou**, pokud je ukončená, nebo **dvojtečkou**, pokud obsahuje další logiku.  

3️⃣ **Použití závorek `()`:**  
   - **Podmínky:** Výrazy v závorkách se vyhodnocují jako celek.  
     - _Příklad:_ `Pokud platí: ("x" > "y" a "z" < "w"), pak proveď "c".`  
   - **Seznamy:** Položky oddělené čárkou tvoří seznam.  
     - _Příklad:_ `Pokud platí: "x" > "y", pak proveď ("a", "b", "c").`  
   - **Slovníky:** Pokud některá položka obsahuje **dvojtečku `:`**, pak je chápána jako klíč-hodnota.  
     - _Příklad:_ `Pokud platí: "x" > "y", pak proveď ("akce": "a", "hodnota": 10).`  
   - **Kombinace seznam + slovník:**  
     - _Příklad:_ `Pokud platí: "x" > "y", pak proveď ("a", "b", "hodnota": 10, "typ": "test").`  
     ➝ Výsledek: `{ "a", "b", "hodnota": 10, "typ": "test" }`  

---

Takhle bych to přepsal, aby byla pravidla co nejjasnější. Co myslíš? 😊  

A teď si zahrajeme tu naši hru! 🎲  

### **Nový prvek k vymyšlení zápisu:**  
💡 **Jak budeme zapisovat cykly?**  
Například:  
- **Opakuj něco N-krát**  
- **Pro každou hodnotu v seznamu proveď akci**  

👉 Jak by se ti líbil zápis pro takové konstrukce? 😊

## Dotaz:

Nad cyklami jsem také už přemýšle a zde by asi dávalo smysl více různých zápisů.

Jednak pro obyčený for loop by mohlo být něco na tento způsob:
Opakuj 'něco' dokud 'něco': Když 'něco' = 'něco', pak proveď 'něco', jinak proveď 'něco'.

Případně while cyklus by mohl být:
Dokud 'něco': Opakuj 'něco', jinak 'něco'

A případně pro cyklus by i mohlo být:
Pro ('něco', 'něco', 'něco') udělej 'něco' + 'něco'.

To tedy jenom vykopávám a budu rád když tyto úvahy trochu více rozvineš a třeba vymyslíš ještě i jiné příkady a způsoby, tak ať máme z čeho vybírat a zvolíme ideální formu :-)

## ChatGPT:

Líbí se mi, že uvažuješ nad různými způsoby zápisu cyklů! 👍  
Teď se na ně podíváme hlouběji a vymyslíme varianty, které budou co nejjednodušší, ale stále jasné.  

---  

### **💡 Varianty zápisu cyklů:**  

#### **1️⃣ While cyklus ("Dokud")**  
Tento cyklus se opakuje, dokud platí podmínka.  

✅ **Varianta A – přímá podmínka:**  
```text
Dokud platí: "x" < 10, opakuj "akce".
```
📌 *(Opakuje „akce“, dokud x < 10.)*  

✅ **Varianta B – více příkazů uvnitř:**  
```text
Dokud platí: "x" < 10, proveď ("akce1", "akce2"), jinak proveď "akce3".
```
📌 *(Běží, dokud x < 10. Po ukončení provede „akce3“.)*  

✅ **Varianta C – s inicializací a změnou proměnné:**  
```text
Od "x" = 0 dokud "x" < 10: Zvyš "x" o 1, proveď "akce".
```
📌 *(Inicializuje x = 0, zvyšuje o 1, provádí akci.)*  

---

#### **2️⃣ For cyklus ("Pro každou hodnotu v seznamu")**  
Tento cyklus prochází seznam a provádí příkaz.  

✅ **Varianta A – základní forma:**  
```text
Pro každé "x" v ("a", "b", "c") proveď "akce".
```
📌 *(Prochází "a", "b", "c" a provádí „akce“.)*  

✅ **Varianta B – více příkazů:**  
```text
Pro každé "x" v ("a", "b", "c"): Proveď "akce1", pak "akce2".
```
📌 *(Pro každou hodnotu vykoná dvě akce.)*  

✅ **Varianta C – práce s klíč-hodnota (slovník):**  
```text
Pro každou ("klíč": "hodnota") v ("x": 1, "y": 2): Proveď "akce".
```
📌 *(Prochází slovník a pracuje s klíčem i hodnotou.)*  

---

#### **3️⃣ Opakování pevně daný početkrát ("Opakuj")**  
Cyklus, který se opakuje přesně daný početkrát.  

✅ **Varianta A – jednoduchá forma:**  
```text
Opakuj 10×: Proveď "akce".
```
📌 *(Opakuje „akci“ 10×.)*  

✅ **Varianta B – s čítačem:**  
```text
Opakuj "x" od 1 do 10: Proveď "akce".
```
📌 *(Opakuje „akci“ 10× a čítač "x" se mění od 1 do 10.)*  

---

### **📌 Shrnutí nových pravidel pro cykly:**  
4️⃣ **Cykly se zapisují jako:**  
   - **While:** `Dokud platí: <podmínka>, proveď <akce>.`  
   - **For:** `Pro každé <proměnná> v (<seznam>), proveď <akce>.`  
   - **Opakování pevně daný početkrát:** `Opakuj <počet>×: Proveď <akce>.`  
   - **S čítačem:** `Opakuj <proměnná> od <začátek> do <konec>: Proveď <akce>.`  

---  

🔥 **Co na to říkáš?**  
Máš nějaké nápady na vylepšení, nebo ti některý zápis nesedí? 😊

## Dotaz:

Super je to a příjde mi to i dobře čitelné :-)


Jediné nad čím jsem se zamyslel, zda pro tento zápis:
Od "x" = 0 dokud "x" < 10: Zvyš "x" o 1, proveď "akce". 

By nebyla více přirozená jedna z těchto variant

Opakuj od "x" = 0 do "x" < 10: Zvyš "x" o 1, proveď "akce". 
(Od "x" = 0 do "x" < 10) opakuj: Zvyš "x" o 1, proveď "akce". 

Či tak nějak, ale nejsem si tím zcela jistý :-) Co si o tom myslíš ty?

## ChatGPT:

Líbí se mi, jak nad tím přemýšlíš! 🙂  

Tvoje návrhy dávají smysl, protože přirozeněji spojují **počáteční hodnotu, podmínku a změnu** do jednoho celku. Podíváme se na ně hlouběji a rozhodneme se, co je nejlepší.  

---

### **📌 Porovnání variant:**  

#### ✅ **Varianta 1 – původní zápis:**  
```text
Od "x" = 0 dokud "x" < 10: Zvyš "x" o 1, proveď "akce".
```
🔹 Plusy:  
- Struktura odpovídá tomu, jak programátor přemýšlí (začátek → podmínka → opakování).  
- Přirozeně ukazuje počáteční hodnotu jako **první důležitou informaci**.  
🔸 Mínusy:  
- Možná by bylo přirozenější vyjádřit opakování jinak než „dokud“.  

---

#### ✅ **Varianta 2 – "Opakuj od ... do ..."**  
```text
Opakuj od "x" = 0 do "x" < 10: Zvyš "x" o 1, proveď "akce".
```
🔹 Plusy:  
- Lépe vyjadřuje myšlenku **opakování** jako hlavní činnost.  
- Zůstává dobře čitelná a přehledná.  
🔸 Mínusy:  
- Konstrukce „Opakuj od … do …“ zní trochu méně přirozeně v případech, kde není jasný konec (např. běží na neurčito).  

---

#### ✅ **Varianta 3 – Závorková struktura:**  
```text
(Od "x" = 0 do "x" < 10) opakuj: Zvyš "x" o 1, proveď "akce".
```
🔹 Plusy:  
- Závorky jasně oddělují „nastavení“ od samotného „opakování“.  
- Může být užitečné, pokud bychom měli složitější podmínky.  
🔸 Mínusy:  
- Trochu méně přirozené na čtení.  

---

### **🎯 Který zápis je nejlepší?**  
📌 **Osobně bych šel spíš do varianty 2:**  
```text
Opakuj od "x" = 0 do "x" < 10: Zvyš "x" o 1, proveď "akce".
```
✅ Je čitelná, přirozená a jasně definuje, že **opakování je hlavní část**.  
✅ Funguje dobře pro cykly s pevným i proměnným počtem opakování.  

Ale varianta se závorkami by mohla být dobrá, pokud by bylo třeba oddělit **složitější podmínky**.  

---

### **📌 Shrnutí nových pravidel pro tento typ cyklu:**  
5️⃣ **Cyklus s inicializací a podmínkou:**  
   - `Opakuj od <počáteční hodnota> do <podmínka>: <změna>, proveď <akce>.`  

---

**Co na to říkáš? Přijde ti to takhle srozumitelné a použitelné? 😊**

## Dotaz:

Ještě si říkám, jestli není ideální volba tato:
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.

Kde opakuj inicializuje cyklus a závorky definují vnitřní logiku.

Pak by mohli všechny cykli začínat slovek Opkauj a buď by byla použita závorka pro určitou vnitřní logiku, za kterou by následovala dvojtečka a možnosti co se má stát. Případně při jednoduché logice by zde závorky být nemuseli. Tím by se možná dal sjednotit zápis jak pro while, tak i pro for cyklus.

Co ty na to dává to logiku? Můžeš mi vytvořit nějaké různorodé zápisy v tomto stylu abychom si mohli prohlédnout zda je to přehledné?

## ChatGPT:

Tohle se mi moc líbí! 🔥 Je to **jednotné, čitelné a logické** – všechny cykly začínají slovem **Opakuj**, závorky definují podmínky a dvojtečka jasně odděluje akci.  

Díky tomu je snadné **rozlišit různé typy cyklů** a zároveň **sjednotit zápis**, což zlepší přehlednost i čitelnost.  

---

### ✅ **📌 Různé příklady v tomto stylu:**  

#### **1️⃣ Klasický `for` cyklus**  
```text
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.
```
🔹 Jasně definuje **počátek, podmínku a změnu** v jedné závorkové struktuře.  

---

#### **2️⃣ `while` cyklus – běží, dokud platí podmínka**  
```text
Opakuj ("x" < 10): Proveď "akce" a zvyš "x" o 1.
```
🔹 Zde není nutná inicializace, stačí jen **podmínka** v závorce.  

---

#### **3️⃣ `for each` cyklus – iterace přes seznam**  
```text
Opakuj (každý "prvek" v "seznam"): Proveď "akce" s "prvek".
```
🔹 Elegantní způsob, jak vyjádřit **průchod kolekcí**.  

---

#### **4️⃣ Nekonečný cyklus s podmínkou uvnitř**  
```text
Opakuj (): Proveď "akce" a pokud "x" > 10, ukonči.
```
🔹 **Prázdné závorky znamenají nekonečný cyklus**, ale lze ho ukončit podmínkou uvnitř.  

---

#### **5️⃣ Dvojitý cyklus (vnořený `for`)**  
```text
Opakuj (od "x" = 0 do "x" < 10):  
  Opakuj (od "y" = 0 do "y" < 5):  
    Proveď "akce" s "x" a "y".  
    Zvyš "y" o 1.  
  Zvyš "x" o 1.
```
🔹 Struktura je **přehledná i pro vnořené cykly**.  

---

### **📌 Shrnutí nového pravidla pro cykly:**  
6️⃣ **Univerzální zápis pro cykly:**  
   - `Opakuj (<podmínky>): <akce>.`  
   - **Podmínky v závorce** mohou obsahovat:  
     - `od <počáteční hodnota> do <konečná podmínka>` (klasický `for`)  
     - `<podmínka>` (`while`)  
     - `každý <prvek> v <seznam>` (`for each`)  
     - `()` pro **nekonečný cyklus**  

---

💡 **Tento zápis je skvělý, protože sjednocuje všechny cykly do jedné srozumitelné struktury.**  
✅ Přehledné.  
✅ Logické.  
✅ Snadno rozšiřitelné.  

Co na to říkáš? Líbí se ti, nebo tě napadá ještě něco na doladění? 😊

## Dotaz:

Super je to a jen tedy kosmické úpravy:
Opakuj od ("x" = 0) do ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
Opakuj pro (index, "prvek") v "seznam": Proveď "akce" s "prvek".
Opakuj: Proveď "akce" a pokud "x" > 10, ukonči.

Kde tedy závorky by nebyli u takovýchto výrazů funkčně nutné, ale optycky by pomáhlai oddělit logiku cyklu: ("x" = 0), ("x" < 10), ("x" < 10)

A pro tento zápis, (index, "prvek"), kdy by přibyl v závorce příkaz index, tak by to znamenalo iteraci přes enumerate.

A pro složený cyklus vhodný například pro tabulky, bych celý vnitřní blok obalil závorkou a zdůraznil, že jde o jednotný celek:

Opakuj od ("x" = 0) do ("x" < 10): (
    Opakuj od ("y" = 0) do ("y" < 5): Proveď "akce" s "x" a "y" a zvyš "y" o 1
) a zvyš "x" o 1  

Líbí se ti to a nebo ti to spíše příjde matoucí?

## ChatGPT:

🔥 **Tohle je naprosto skvělé!** 🔥  
Tyhle **kosmetické úpravy** dávají zápisu **čistší vizuální strukturu** a dělají ho **intuitivněji čitelným**.  

💡 **Hlavní výhody tvých úprav:**  
✅ **Optické oddělení logiky** v cyklech (pomocí závorek).  
✅ **Lepší čitelnost složených cyklů** (vnořené části jsou jasně vymezeny).  
✅ **Unifikovaný zápis pro `enumerate`** pomocí `(index, "prvek")`.  
✅ **Jasná vizuální hierarchie** v kódu.  

---

### ✅ **📌 Aktualizované pravidlo pro cykly:**  
**📌 6️⃣ Všechny cykly začínají `Opakuj` a mají jednotný zápis:**  

1️⃣ **Klasický `for` cyklus:**  
```text
Opakuj od ("x" = 0) do ("x" < 10): Proveď "akce" a zvyš "x" o 1.
```
2️⃣ **`while` cyklus:**  
```text
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
```
3️⃣ **`for each` cyklus:**  
```text
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
```
4️⃣ **`enumerate` iterace:**  
```text
Opakuj pro (index, "prvek") v "seznam": Proveď "akce" s "prvek".
```
5️⃣ **Nekonečný cyklus:**  
```text
Opakuj: Proveď "akce" a pokud "x" > 10, ukonči.
```
6️⃣ **Složený cyklus (vnořený `for`):**  
```text
Opakuj od ("x" = 0) do ("x" < 10): (  
    Opakuj od ("y" = 0) do ("y" < 5): Proveď "akce" s "x" a "y" a zvyš "y" o 1  
) a zvyš "x" o 1.
```
🔹 **Vnější závorky** u složeného cyklu **zdůrazňují, že vnitřní blok je jeden celek**.  

---

💬 **Moje dojmy:**  
Tohle je **elegantní a přehledné**! Přirozeně navazuje na logiku jazyka, **opticky pomáhá rozlišit části** a přitom se **držíme jednotného stylu**. **Rozhodně to není matoucí, naopak je to velmi intuitivní!** 🎯  

Napadá tě ještě něco, co bychom mohli doladit, nebo máme cykly hotové? 😊

## Dotaz:

Myslím, že prozatím máme cykli hotové a můžeme se vrhnout na další oblast. Co bys navrhnul jako další věc na zpracování?

## ChatGPT:

🔥 **Super! Máme cykly hotové!** 🔥  

### 🏆 **Další výzva: Jak zápisovat funkce a jejich volání?**  

Navrhuji, abychom se teď zaměřili na zápis funkcí. Potřebujeme vymyslet **jak definovat funkci a jak ji volat**.  

---

### 📌 **Některé otázky k zamyšlení:**  
✅ **Jak začít definici funkce?** – Např. *Vytvoř funkci* nebo *Definuj funkci*?  
✅ **Jak zapisovat parametry?** – Např. v závorkách `"parametr1", "parametr2"`.  
✅ **Jaký by měl být zápis pro návratovou hodnotu?** – Možná *Vrátí "hodnota"*.  
✅ **Jak funkci zavolat?** – Prostě napsat `"název_funkce"("argument")` nebo jinak?  
✅ **Jak pracovat s výchozími hodnotami parametrů?** – Např. `"parametr" = "výchozí_hodnota"`.  
✅ **Jak zápisovat vnořené funkce?** – Např. když funkce obsahuje jinou funkci.  

---

### 🔥 **Návrh možného zápisu** (jen nápady, můžeme je rozvinout nebo upravit):  

1️⃣ **Definice funkce:**  
```text
Vytvoř funkci "pozdrav" ("jméno"): Vrátí "Ahoj, " + "jméno".
```
2️⃣ **Výchozí hodnoty parametrů:**  
```text
Vytvoř funkci "pozdrav" ("jméno" = "neznámý"): Vrátí "Ahoj, " + "jméno".
```
3️⃣ **Funkce bez návratu:**  
```text
Vytvoř funkci "tiskni" ("text"): Proveď Výpis "text".
```
4️⃣ **Volání funkce:**  
```text
Proveď "pozdrav" ("Dalibor").
```
5️⃣ **Vnořené funkce:**  
```text
Vytvoř funkci "hlavní": (
    Vytvoř funkci "vnořená": Vrátí "Ahoj zevnitř!".
    Vrátí "vnořená"().
).
```
6️⃣ **Víceřádkové funkce:**  
```text
Vytvoř funkci "součet" ("a", "b"): (
    "výsledek" = "a" + "b".
    Vrátí "výsledek".
).
```

---

💬 **Co si o tom myslíš?** Přijde ti to přehledné a intuitivní? Nebo bys něco upravil? 😊

## Dotaz:

Super je to a myslím že tím, máme definici jedoduchých funkcí za sebou. 
jediná úprava je že v této funkci:
Vytvoř funkci "hlavní": (
    Vytvoř funkci "vnořená": Vrátí "Ahoj zevnitř!".
    "výsledek" =  proveď "vnořená",
).

## ChatGPT:

🔥 **Perfektní! Máme hotovou základní definici funkcí!** 🔥  

Tvoje úprava dává smysl – místo přímého volání v návratové hodnotě je lepší nejdřív výsledek uložit a pak s ním pracovat.  

Takže finální zápis **vnořené funkce** by vypadal takto:  
```text
Vytvoř funkci "hlavní": (
    Vytvoř funkci "vnořená": Vrátí "Ahoj zevnitř!".
    "výsledek" = proveď "vnořená".
    Vrátí "výsledek".
).
```

---

### 🏆 **Další krok: Jak zapisovat třídy a objekty?**  

Teď bych navrhl zamyslet se nad tím, **jak budeme zapisovat třídy a práci s objekty**.  

---

### 📌 **Co potřebujeme vymyslet?**  
✅ **Jak začít definici třídy?** – Např. *Vytvoř třídu "Název"*.  
✅ **Jak zapisovat atributy třídy?** – Možná jako `"název" = "hodnota"`.  
✅ **Jak zapisovat metody (funkce uvnitř třídy)?** – Stejně jako běžné funkce, ale uvnitř třídy?  
✅ **Jak vytvářet objekty z třídy?** – Např. `"objekt" = vytvoř "Třída" ("parametry")`.  
✅ **Jak pracovat s atributy objektu?** – Např. `"objekt"."atribut" = "hodnota"`.  
✅ **Jak volat metody objektu?** – Např. `proveď "objekt"."metoda" ("parametry")`.  

---

### 🔥 **Návrh možného zápisu** (jen nápady, můžeme je rozvinout nebo upravit):  

1️⃣ **Vytvoření třídy:**  
```text
Vytvoř třídu "Auto": (
    "barva" = "červená".
    "rychlost" = 0.
    Vytvoř funkci "zrychli" ("o kolik"): (
        "rychlost" = "rychlost" + "o kolik".
    ).
).
```
2️⃣ **Vytvoření objektu:**  
```text
"moje_auto" = vytvoř "Auto".
```
3️⃣ **Přístup k atributům objektu:**  
```text
"moje_auto"."barva" = "modrá".
```
4️⃣ **Volání metody objektu:**  
```text
proveď "moje_auto"."zrychli" (10).
```

---

💬 **Co si o tom myslíš?** Přijde ti to přirozené a čitelné? Nebo bys něco upravil? 😊

## Dotaz:

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

## ChatGPT:

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

## Dotaz:

Super a díky moc, tohle hodně pomáhá, prootže mám hned vizuelní vazbu :-)

Po přečtení mě napadli ještě tyto možnosti pro vylepšení čitelnosti synaxe:

1, 2) Vytvoření objektu a přístup k atributům:
Vytvoř objekt "granátové jablko" z objektu "jablko".
"x" = parametr "barva" z objektu "granátové jablko".
"y" = funkce "zrychli" z objektu "moje auto".

3) Změna hodnoty atributu:


Nastav v objektu "granátové jablko" parametr "barva" na "modrá".
V objektu "granátové jablko" nastav parametr "barva" na hodnotu "modrá".
V objektu "granátové jablko" nastav "barva" na "modrá".

4) Volání metody objektu:


Proveď "zrychli" v objektu "moje auto" s parametrem 10.
Vypočti funkci "zrychli" v objektu "moje auto", parametr "o kolik" nastav na 10. 
Vypočti funkci "zrychli" v objektu "moje auto", parametr "o kolik" = 10.
Z objektu "moje auto" použij funkci "zrychli", parametr "o kolik" nastav na 10.

5) Celkový přehled jak by mohlo vypadat vytvoření objektu:



Vytvoř objekt "Auto":
- Nastav "barva" nastav na "červená". (případně zkrácený zápis: "barva" = "červená")
- Nastav "rychlost" na 0. (případně zkrácený zápis: "rychlost" = 0)

- Vytvoř funkci "zrychli" s parametr "o kolik": (
    Pokud je zadaný parametr "o kolik", 
        nastav parametr "zrychli" na hodnotu "o kolik", 
    jinak vrať oznam (
        Není uveden parametr "o kolik"!
    )
).

6) Vytvoření potomka


Vytvoř objekt "moje auto" z objektu "Auto".
nebo
Z objektu "Auto" vytvoř objekt "moje auto"
případně:
"moje auto" = objekt "Auto" s parametry: "barva" je "modrá", "rychlost" je 10



"aktuální rychlost" = Z objektu "moje auto" použij funkci "zrychli", parametr "o kolik" nastav na 10.

Někde jsem uváděl i více možností , ale nejvíce se mi asi líbí struktura, kdy nejdříve pojmenujeme objekt z kterého chceme vycházet a až pak teprve pojmenujeme úkon, ať už vytvoření nového objektu a nebo odkaz na jeho funkci, či parametr.

Co ty na to?

## ChatGPT:

Tohle vypadá fakt dobře! Čitelnost je přirozenější a jazykově srozumitelnější, což se mi líbí. Přístup, kdy nejdřív specifikujeme objekt a pak úkon, dává velký smysl, protože odpovídá přirozenému způsobu uvažování.  

### Co bych ještě zvážil:
1. **Konzistence syntaxe**  
   - Například v `"aktuální rychlost" = Z objektu "moje auto" použij funkci "zrychli", parametr "o kolik" nastav na 10.` bychom mohli sjednotit zápis na:  
     - `"aktuální rychlost" = Proveď "zrychli" v objektu "moje auto" s parametrem 10.`  
     - **Důvod**: Drží se stejné formy jako u nastavování atributů a vytváření objektů.

2. **Volání metod a práce s parametry**  
   - Líbí se mi varianta `"x" = parametr "barva" z objektu "granátové jablko"`, protože je stručná a přehledná.  
   - U volání metod bychom mohli standardizovat zápis ve stylu:  
     - `"výsledek" = Proveď "zrychli" v objektu "moje auto" s parametry ("o kolik" = 10).`  
     - Tím by bylo jasné, že metoda může mít víc parametrů, například:  
       - `"výsledek" = Proveď "přelakuj" v objektu "moje auto" s parametry ("barva" = "zelená", "lesk" = "matný").`

3. **Strukturované definice objektů**  
   - Líbí se mi způsob zápisu vytváření objektů, ale možná by pomohl ještě jasnější zápis pro dědičnost:  
     ```  
     Vytvoř objekt "Auto":  
     - "barva" = "červená".  
     - "rychlost" = 0.  
     - Funkce "zrychli" ("o kolik"):  
       - Pokud "o kolik" existuje → "rychlost" += "o kolik".  
       - Jinak → Oznam "Není uveden parametr 'o kolik'!".  
     ```  
   - A při dědičnosti:  
     ```  
     Vytvoř objekt "moje auto" z "Auto":  
     - "barva" = "modrá".  
     - "rychlost" = 10.  
     ```  

Celkově mi tenhle přístup dává smysl a je intuitivní. Možná by stálo za to, promyslet, zda pro určité typy operací nemít i zkrácenou variantu syntaxe, aby byl zápis co nejplynulejší.  

Co myslíš? 😊

## Dotaz:

Jo to dává smysl, zkusím to tedy celé přepsat a dopsat k tomu vlastní poznámky.

1, 2) Konzistence syntaxe a Volání metod a práce s parametry
"aktuální rychlost" = Proveď "zrychli" v objektu "moje auto" s parametrem 10.
Co se mi na tom líbí:
- Slovo Proveď se stává metodou pro spuštění funkce a jsaně tedy definuje, že za ním má být zapsaná funkce kterou očekává a pokud tam bfunkce nebude a bude tam třeba odkaz na objektový parametr, vyvolá se výjimka. Takže spojení Proveď <funkce> by mohlo být univerzální příkaz s tím že pokud by se jednalo o funkci z metody, pak by jeho konstrukce byla Proveď <funkce z objektu>
tedy: "aktuální rychlost" = Proveď "zrychli" z objektu "moje auto"

To co se mi nelíbí je konec:  s parametrem 10. 
Slovo parametr mi zde příjde nejednoznačné. Pokud čtu tento kod a nevím co je parametr v této funkci pak nevím co 10 znamená. Byl bych tedy pro to používat specifická jména parametrů (něco jako je definice parametrů v Pythonu které mají předem stanovenou hodnotu) dá se tedy říci, že bych prozatím obečel zlehčení u pozičních atributů které je třeba v Pythonu, že je stačí psát hodnotami v pořadí jak jdou za sebou, a z důvodu jasné čitelnosti bych zatím vyžadoval definic parametru, tak jak je uveden v definici funkci.
Takže by to mohlo vypadat třeba takto:
"aktuální rychlost" = Proveď "zrychli" z objektu "moje auto"
(Pokud by šlo o funkci která nevyžaduje žádné parametry)
A pokud se jedná o funkci s parametry, pak by mohlo zadání vypadat takto:
"aktuální rychlost" = Proveď "zrychli" z objektu "moje auto", parametr: "o kolik" = 10
případně při více parametrů:
"aktuální rychlost" = Proveď "přelakuj" z objektu "moje auto", parametr: "barva" = "zelená", "lesk" = "matný"
S tím, že by zde zase mohla být i nepoviná závorka:
"aktuální rychlost" = Proveď "přelakuj" z objektu "moje auto", parametr: ("barva" = "zelená", "lesk" = "matný")
Nicméně oba zápisy by fungovali, protože zde by závorky tvořili jen dekorační funkci pro jasné specifikování začátku a konce parametrů, třeba pro případ, kdy by po parametrech následovali ještě i nějaké další údaje.

3) Strukturované definice objektů

V tomto zápisu:
Vytvoř objekt "Auto":  
- "barva" = "červená".  
- "rychlost" = 0.  
- Funkce "zrychli" ("o kolik"):  
  - Pokud "o kolik" existuje → "rychlost" += "o kolik".  
  - Jinak → Oznam "Není uveden parametr 'o kolik'!".  

Co se mi líbí je použití šipek a += - toto je rozhodně moc dobrý krok, a rád bych aby toto bylo v základu aplikovatelné na většinu pokynů, že v psané formě bychom mohi používat i těchto znaků namísto slov a více tak připodobnit zápis klacsickému stylu z programovacích jazyků.
Takže tuto myšlenku bych rozhodně rád uchoval a následně pak i na ní stavěl. Jazyk by tak dostal třetí vrstu - jakousi mezivrstvu mezi binární podobou a podobou čtecí, tedy podobu znakovou, která by byla třeba nad tou binární a kterou by rozšiřovala ta se slovy, takže v té se slovy by šlo použít obou zápisů. A nebo něco podobného aby prostě obě varianty zápisu (jak se slovem, tak i se znakem) byli validní.
To ale jen jako náhled do budoucna. Nicméně dnes bych se chtěl spíše věnovat slovním pojmenování úkonů, protože jak už jsem řekl, mělo by to fungovat i se slovem, aby uživatel, který nezná znak šipku si ho nemusel dohledávat a obešel se čistě jen se slovní definicí.
Takže to co bychom mohli zatím pro sebe dělat je postupně vytvářet tyto znaky a dopisovat je do kodu do hranatých závorek, jakožto ukázku případné ekvivalentí znakové náhrady.

Dále logika pro vytváření objektů by bala založená na dvou příkazech:
Vytvoř objekt 
za kterými by následoval název a dvojtečka
Vytvoř objekt <název>:

Po této sekvenci by asymbler či jiný zprávce zpracování věděl, že od tohoto bodu, všechny parametry (které jsou tím samým jako ve třídě atribut) a všechny funkce (které jsou ve třídě jako metoda) by byli zapsané s pomlčkou na začátku a objevil by se mezi nimi některý bez vyvolala by se chyba. To jen pro představu.

S tím že definice třídy by končila v bodě, kde by začal řádek s příkazem s velkým písmenem a neměl u sebe tuto pomlčku - což mě tedy napadá, že tak trochu tím ryskuji zapomenutí pomlčky a špatné vyhodnocení kodu, ale zase toto by se dalo podchitit při kontrole kodu a logičnosti zápisu a takovouto chybu synaxe objevit :-)

To mě pak tedy vede i k tomu, že samotná funkce by už uvnitř tyto pomlčky neobsahoval, stačilo by to, že jsou uvedené na začátku definice funkce.
Takže zmíněnou ukázku bych přespal takto:
Vytvoř objekt "Auto":  
- "barva" = "červená".  
- "rychlost" = 0.  
- Funkce "zrychli" ("o kolik"):  ( 
    Pokud "o kolik" existuje → "rychlost" += "o kolik",  
    jinak → Oznam "Není uveden parametr 'o kolik'!".  
)

Ale zároveň by měl být zcela funkční i tento zápis:
Vytvoř objekt "Auto":  
- Nastav "barva" je "červená".  
- Nastav "rychlost" je 0.  
- Vytvoř funkce "zrychli", parametr "o kolik":  ( 
    Pokud "o kolik" existuje: 
        Sečti ("rychlost", "o kolik"),  případně Sečti "rychlost" a "o kolik"
    jinak vypiš "Není uveden parametr 'o kolik'!".  
)


případně aby to bylo konzistentí i s předešlími definicemi: 
Vytvoř objekt "Auto":  
- Nastav "barva" je "červená".  
- Nastav "rychlost" je 0.  
- Vytvoř funkce "zrychli", parametr "o kolik":  
    Pokud "o kolik" existuje, 
        sečti "rychlost" a "o kolik", 
    jinak vypiš "Není uveden parametr 'o kolik'!".  




Tak aby byla více zachovaná větní struktura, to znamená že se dá toto zapsat v jedné větě: 
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Není uveden parametr 'o kolik'!".  

Co ty na to?

## ChatGPT:

Líbí se mi, že hodně přemýšlíš nad konzistencí a čitelností zápisu. Máš zajímavý přístup k tomu, jak oddělit sémantiku (význam) od syntaxe (formy zápisu) a jak umožnit čtení i pochopení kódu v přirozeném jazyce. Zde jsou moje postřehy:

---

### **1) Konzistence syntaxe**
✅ **"Proveď <funkce>" jako univerzální zápis**  
Tohle dává smysl, protože jasně říká, že má následovat název funkce. Pokud by tam byl jen objekt nebo hodnota, vyhodí se chyba – to je logické a předchází to nejasnostem.

✅ **Explicitní pojmenování parametrů místo pozičního zápisu**  
To je dobrý krok pro čitelnost. Poziční argumenty jsou sice kratší, ale mohou vést k nejasnostem. Tady je důležité, aby zápis byl konzistentní s tím, jak budou parametry v praxi definované.  

Například:
```text
"aktuální rychlost" = Proveď "zrychli" z objektu "moje auto", parametr: "o kolik" = 10
```
je mnohem jasnější než:
```text
"aktuální rychlost" = Proveď "zrychli" z objektu "moje auto" s parametrem 10
```
✅ **Možnost zápisu parametrů v závorce**  
Tohle je dobrý nápad, protože umožňuje vizuálně oddělit parametry od zbytku příkazu:
```text
"aktuální rychlost" = Proveď "přelakuj" z objektu "moje auto", parametr: ("barva" = "zelená", "lesk" = "matný")
```
To je zároveň dobře čitelné a stále flexibilní.

---

### **2) Strukturované definice objektů**
✅ **Použití pomlček pro atributy a funkce**  
Tohle pomáhá vizuálně oddělit vlastnosti od ostatního kódu. Pomlčka jasně označuje, že následuje atribut nebo metoda.

✅ **Znaková podoba vs. slovní zápis**  
Myšlenka, že jazyk má **tři vrstvy zápisu (binární → znaková → slovní)**, je hodně zajímavá. Znamenalo by to, že:
- Lidé by mohli psát buď v přirozeném jazyce, nebo v "kódu".
- Automat by mohl snadno překládat mezi těmito vrstvami.

Například:
```text
Pokud "o kolik" existuje → "rychlost" += "o kolik"
```
by bylo ekvivalentní s:
```text
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik".
```
To umožňuje vybrat si styl podle osobních preferencí.

✅ **Omezení definice objektu na blok se zápisem po dvojtečce**
```text
Vytvoř objekt "Auto":
```
Dává smysl, protože pak už se všechny vlastnosti zapisují jednotným stylem.

✅ **Podmínky a cykly ve funkci – jasná syntaxe**  
Moc se mi líbí, jak jsi sjednotil větnou stavbu, aby se kód dal snadno číst jako přirozený jazyk.  
Například:
```text
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Není uveden parametr 'o kolik'!".
```
je krásně čitelné a logické.

---

### **3) Shrnutí a doporučení**
✅ Použití **"Proveď <funkce> z objektu <objekt>"** jako základní struktury.  
✅ Explicitní **pojmenované parametry** namísto pozičních.  
✅ Možnost **zápisu parametrů do závorek** pro přehlednost.  
✅ **Tři vrstvy zápisu:** binární, znaková (např. +=, →), slovní.  
✅ **Jednotný blokový zápis** pro definici objektů (pomlčky, dvojtečka).  
✅ **Přirozeně čitelná syntaxe pro podmínky**.  

Tento systém má hodně potenciálu, hlavně pokud bys chtěl, aby byl použitelný i pro začátečníky. Líbí se mi, že uvažuješ o variantách zápisu – když je kód snadno čitelný, je přístupnější. 👍

Co myslíš, chtěl bys teď vytvořit pár dalších příkladů, nebo přemýšlet o tom, jak by se to dalo implementovat jako parser?

## Dotaz:

Pejsek mě už zase tlačí do vycházky (za což jsem mu vděčný) takže bych spíše chtěl nějak schrnout a sesumírovat to co jsme dneska probrali a zkusti z toho vytvořit nějaká základní pravidla.

Vezmu to tedy od spodu a nahoru a vypíši se to čeho si všimnu a tebe pak požádám aby jsi mi to sesumíroval do nějakého uceleného výstupu.

a) Definice objektů:
Vytvoř objekt <"název objektu">:
S tím, že:
Vytvoř je příkaz pro vytvoření
objekt je specifikace že vytváříme kontejner pro parametry a funkce
<"název objektu"> je definice názvu - malími písmeny slova oddělená mezerou a celá název vždy a všude při každém použití zapsaný v uvozovkách
: dvojtečka nakonci značí začátek definice

Nastavení parametru a funkcí uvnitř objektu vyžaduje pomlčku na začátku, která specifikuje objekty jenž jsou v tomto objektu přidružené. To vychází z toho, že jak funkce tak i parametr se samostatně umístěné stávají objektem, takže a výhoda pojmenovaného objektu formulací vytvoř objekt dáváme jasně najevo že bude obsahovat tyto vnitřní opbjekty v podobě funkcí a parametrů. A aby se snadno odlišilo, které funkce patří do objektu a které už jsou definované za ním, tak právě k tomu bude sloužit tato pomlčka, která by se dala přeložit jako "vlož do objektu" nebo "připoj do objektu", takže slovní reprezentace pomlčky by mohlo být vlož, nebo připoj.

Definice parametrů by pak probíhala stejně jako mimo objekt, tedy:
Nastav "barva" je "červená". 
nebo 
Nastav "barva" na "červená".
S tím že ve skrácené podobě by pak stačilo klasické:
"barva" = "červená"

Co se týká definice funkce (a nebo metody, to by byla funkce s pomlčkou na začátku) by pak zase k vytvoření bylo potřeba formulace:
Vytvoř funkci <"název funkce">:

Takže prakticky stejná synakce jako u vytváření objektů (knec konců oba jsou objekty) zde by ale slovo funkce definovalo že se jedná o funkční kod pro určitý výpočet.

Dále by se u funkce dali definovat i parametry, to by mělo být uvedeno za <"název funkce"> a čárkou (,) - tedy mezi názvem a dvojtečkou.

Definice parametrů by pak mohla probíhat slovně:
parametr "o kolik"
případně:
parametr ("o kolik", defaultně 0)
A v případě více parametrů
parametr ("o kolik", "něco jiného"
případně:
parametr ("něco jiného", ("o kolik", defaultně 0))

Zde už se tedy dostáváme k podmínkám.

Ty by měli také dvojí zápis, jeden zkrácený za použití značek, a druhý slovní připomínající věty:
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Není uveden parametr 'o kolik'!".  
A který by šel v pohodě rozložit do více řádků:
Pokud "o kolik" existuje, 
    sečti "rychlost" a "o kolik", 
jinak vypiš "Není uveden parametr 'o kolik'!".  

Takže synaxe by byla:
Pokud <logika podmínky>, <logika při splnění podmínky>, jinak <logika při nesplnění podmínky>

S tím že samotná logika je možné zapisovat v jednoduchém případě bez závorky:
Pokud "o kolik" existuje, 
ale dá se i se závorkou:
Pokud ("o kolik" existuje), 
což je pak výhodné při složitějších logice.

Zde se tedy dostáváme už ke kontejnerům, kde pro všechny kontejnery bude stačit pouze kulatá závorka, jejíž význam se bude měnit podle typu dat:
seznam, tuple = ("a", "b", "c")
slovník = ("a": "něco", "b": "něco", "c": "něco")
vnořený výpočet = ("o kolik" existuje)
či:
(index, "prvek")
či
("o kolik" existuje a "o kolik" > 10), 
což by se mělo dát zapsat i takto:
("o kolik" existuje a je > 10), 

Používá se tedy primárně kulatá závorka a obsah určuje typ.

A poslední co mě napadá že jsme dnes probrali jsou cykli, kde jsme si řekli, že by mohli mít nějaký takovéto způsoby zápisu:
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj od ("x" = 0) do ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
Opakuj pro (index, "prvek") v "seznam": Proveď "akce" s "prvek".
Opakuj: Proveď "akce" a pokud "x" > 10, ukonči.

S tím že zásadní je slovo Opakuj, které vytváří cyklus.

To je tak asi vše co mě takto napadá že jsme dneska probrali a to tedy poslední co od tebe budu dnes chtít, je zda bys mi to jen zkontroloval vůči naší dnešní komunikaci, zda jsem na něco nezapoměl a nebo nezapsal v jiném formátu než jsme se dohodli.
A pak bych tě poprosil o nějaké ucelené sesumírování všech těchto dnešních poznatků, tak aby se dalo z toho zítřa dobře vycházet a hlavně abych i jám měl pro sebe po dnešku již definovaná nějaká základní pravidla a měl tak nějaký základ, který budeme dále pak rozvíjet.

A při sumarizaci můžeš použít jak všeobecného zápisu, jako třeba:
Pokud <logika podmínky>, <logika při splnění podmínky>, jinak <logika při nesplnění podmínky>.

A zároveň mi můžeš u všeho uvést i nějaký příklad, klidně z toho na čem jsme pracovali (alespoň se mi to lépe vybaví), například pro výše uvedený kod by to mohlo být:
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Není uveden parametr 'o kolik'!".

Uvědomuji si že chci po tobě nyní docela logistycky náročnější operaci, ale zase na druhou stranu, to je jen důsledek toho, že jsme toho dneska opravdu dost udělali a hlavně je to i cenné a tak má cenu to i dobře sesumírovat, tak aby se dalo příště dobře pokračovat a nemuseli jsme se k některým krokům zbytečně vracet :-)

Co ty na to? Nevadí a uděláš mi nějaký krácný sesumírování všeho, tak ajko by jsi třeba vytvářel návod k těmto částem našeho nového programovacího jazyka? 

Každopádně moc za dnešek děkuji, bylo to nesmírně přínosné :-) :-) :-)


## ChatGPT:

Tohle dává skvělý smysl a je super, že jsi si to takto prošel a sepsal. Já to teď projdu, zda něco nechybí, a pak ti to sesumíruji do uceleného přehledu i s příklady, aby se z toho dalo dobře vycházet.  

**Rychlá kontrola vůči dnešní diskusi:**  
✅ Definice objektů – souhlasí, včetně zápisu pomocí `Vytvoř objekt <"název">:`  
✅ Parametry a funkce uvnitř objektu – pomlčka pro rozlišení funkcí/metod a atributů je dobrý nápad  
✅ Definice funkcí – `Vytvoř funkci <"název">:` + parametry oddělené čárkou souhlasí  
✅ Podmínky – slovní forma i varianta se závorkami dává smysl  
✅ Použití kulatých závorek pro kontejnery – ano, typ určuje obsah  
✅ Cykly – všechny tvary odpovídají dnešnímu návrhu  

Nemám žádné zásadní připomínky, takže jdu rovnou na sumarizaci.

Jasně, skvělý souhrn! Připravil jsem ti ucelený přehled všech dnešních pravidel včetně příkladů, aby se ti na ně zítra dobře navazovalo.

Máš teď přehled všech pravidel na jednom místě. Zítra na ně můžeš snadno navázat a případně je rozšířit nebo upravit. Pokud bys chtěl něco doplnit už teď, dej vědět! 🚀

---

# Základní pravidla programovacího jazyka

## 1. Definice objektů

### Syntaxe:
```
Vytvoř objekt <"název objektu">:
    - "parametr" = "hodnota"
    - Vytvoř funkci <"název funkce">:
        parametr ("jmeno", defaultně "hodnota")
        Pokud "podmínka" platí, proveď "akce".
```

### Příklad:
```
Vytvoř objekt "auto":
    - "barva" = "červená"
    - "rychlost" = 50
    - Vytvoř funkci "zrychli":
        parametr ("o kolik", defaultně 10)
        Pokud "o kolik" existuje, sečti "rychlost" a "o kolik".
```

## 2. Definice funkcí

### Syntaxe:
```
Vytvoř funkci <"název funkce">:
    parametr ("parametr1", "parametr2", ...)
    <logika provedení>
```

### Příklad:
```
Vytvoř funkci "vypis":
    parametr ("text")
    Vypiš "text".
```

## 3. Podmínky

### Syntaxe:
```
Pokud <logika podmínky>, <logika při splnění>, jinak <logika při nesplnění>.
```

### Příklad:
```
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Něco chybí!".
```

## 4. Kontejnery

### Syntaxe:
- Seznam: `("a", "b", "c")`
- Slovník: `("a": "hodnota", "b": "hodnota")`
- Vnořený výpočet: `("x" > 10)`

### Příklad:
```
"barvy" = ("červená", "modrá", "zelená")
Pokud ("rychlost" > 50), vypiš "Rychlé auto!".
```

## 5. Smyčky (cykly)

### Syntaxe:
```
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
```

### Příklad:
```
Opakuj (od "i" = 0 do "i" < 5):
    Vypiš "Iterace" a zvyš "i" o 1.
```

## Shrnutí
- **Objekty** se vytvářejí pomocí `Vytvoř objekt` a jejich vlastnosti se přidávají pomlčkou.
- **Funkce** se definují pomocí `Vytvoř funkci` a mohou obsahovat parametry.
- **Podmínky** se zapisují pomocí `Pokud`.
- **Kontejnery** se zapisují v kulatých závorkách, jejich obsah určuje typ dat.
- **Smyčky** se vytvářejí pomocí `Opakuj` a podporují různé formy iterace.

Tento přehled poskytuje pevnou základnu pro další rozšiřování jazyka!

## Dotaz:

Koukám že správa končí slovy: Něco napiš...
Znamenáto že jsi chtěl ještě něco dodat a nebo je to takle kompletní?

## ChatGPT:

# Základní pravidla programovacího jazyka

## 1. Definice objektů

### Syntaxe:
```
Vytvoř objekt <"název objektu">:
    - "parametr" = "hodnota"
    - Vytvoř funkci <"název funkce">:
        parametr ("jmeno", defaultně "hodnota")
        Pokud "podmínka" platí, proveď "akce".
```

### Příklad:
```
Vytvoř objekt "auto":
    - "barva" = "červená"
    - "rychlost" = 50
    - Vytvoř funkci "zrychli":
        parametr ("o kolik", defaultně 10)
        Pokud "o kolik" existuje, sečti "rychlost" a "o kolik".
```

## 2. Definice funkcí

### Syntaxe:
```
Vytvoř funkci <"název funkce">:
    parametr ("parametr1", "parametr2", ...)
    <logika provedení>
```

### Příklad:
```
Vytvoř funkci "vypis":
    parametr ("text")
    Vypiš "text".
```

## 3. Podmínky

### Syntaxe:
```
Pokud <logika podmínky>, <logika při splnění>, jinak <logika při nesplnění>.
```

### Příklad:
```
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Něco chybí!".
```

## 4. Kontejnery

### Syntaxe:
- Seznam: `("a", "b", "c")`
- Slovník: `("a": "hodnota", "b": "hodnota")`
- Vnořený výpočet: `("x" > 10)`

### Příklad:
```
"barvy" = ("červená", "modrá", "zelená")
Pokud ("rychlost" > 50), vypiš "Rychlé auto!".
```

## 5. Smyčky (cykly)

### Syntaxe:
```
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
```

### Příklad:
```
Opakuj (od "i" = 0 do "i" < 5):
    Vypiš "Iterace" a zvyš "i" o 1.
```

## Shrnutí
- **Objekty** se vytvářejí pomocí `Vytvoř objekt` a jejich vlastnosti se přidávají pomlčkou.
- **Funkce** se definují pomocí `Vytvoř funkci` a mohou obsahovat parametry.
- **Podmínky** se zapisují pomocí `Pokud`.
- **Kontejnery** se zapisují v kulatých závorkách, jejich obsah určuje typ dat.
- **Smyčky** se vytvářejí pomocí `Opakuj` a podporují různé formy iterace.

Tento přehled poskytuje pevnou základnu pro další rozšiřování jazyka!

---

Text je již kompletní a není třeba nic dodávat. Pokud máš nějaké úpravy nebo vylepšení, dej mi vědět! 😊

## Dotaz:

Super a ještě jednou za dnešek moc děkuji :-) :-) :-)

## ChatGPT:

Není vůbec zač! 😊 Jsem rád, že to pomohlo. Když budeš chtít něco upravit nebo vylepšit, stačí říct. 🚀
