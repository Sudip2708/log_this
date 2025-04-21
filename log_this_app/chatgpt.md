## Dotaz:

Ahojky :-)

Včera jsme vymysleli tuto jednoduchou metodu ,která by za pomoci dekorátoru dokázala nahradit zápis větve try / excetpt:

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def exception_catch(*exceptions):
    """Dekorátor pro zachytávání specifikovaných výjimek a logování chyb."""

    # Kontrola platnosti výjimek
    for _exc in exceptions:
        if not issubclass(_exc, BaseException):
            raise TypeError(f"{_exc} není platná výjimka")

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_message = f"Chyba při vykonávání {func.__name__}: {e}"

                # Pokud máme specifikované výjimky, kontrolujeme je
                if exceptions:
                    for exc in exceptions:
                        if isinstance(e, exc):
                            logging.error(error_message, exc_info=True)
                            raise

                # Pokud žádná výjimka nesedí, nebo nejsou specifikovány, logujeme vše
                logging.error(error_message, exc_info=True)
                raise

        return wrapper

    return decorator

Pak jsme na ní dále pracovali a ve finále jsme měli samostatnou třídu, která přebrala logiku této funkce (a pojmenovala ji jako metodu catch) a dále vcelku nabobtnala a přibrala další metody, kde některé z nich jsou jistě výborné, jako třeba metoda vertify, která umožňuje snadné ověření vstupu a nebo metoda handle která umožňuje definici způsobu vyřízení výjimky, když chceme do způsobu zasáhnout a nebo ho změnit.

Krom toho ale nabrala spoustu dalšíchmetod, které všechny tak nějak dávají smysl, ale protože jsem teď tím trochu zahlcený a potřeboval bych si srovna v hlavě co to skutečně máme, poprosil bych tě, aby jsi mi pro tyto metody dané třídy:
    verify: Universální metoda pro ověřování podmínek.
    safe_verify: Bezpečná interní metoda pro ověřování vstupů.

    catch: Dekorátor pro zachytávání a zpracování výjimek.
    handle: Registrace vlastního handleru pro specifickou výjimku.

    set_log_level: Nastavení úrovně logování pro specifickou výjimku nebo globálně.
    set_message: Nastavení vlastní chybové zprávy pro specifickou výjimku.
    set_log_format: Nastavení formátu logování pro specifickou výjimku.

    set_default_handler: Nastavení globálního fallback handleru pro nezachycené výjimky.
    register_global_handler: Registrace globálního handleru pro specifické typy výjimek.
    create_exception_group: Vytvoření skupiny příbuzných výjimek.
    set_retry_strategy: Nastavení strategie opakování pro specifické výjimky.

Vytvořil nějaký stručný referát o tom, jak moc je která z těch metod užitečná a zkusit popsat třeba pro každou nějakou jeden nebo dva vzorové příklad kdy by se teto metoda mohla hodit.

Jde mi o to, abych si udělal představu o tom co máme a dokázal se v tom lépe zorientovat :-)

Takže jestli bys mi je mohl seřadit i podle důležitosti, od těch nejzásadnější až po ty nejméně důležité.

A tady k nim máš ještě pár bližších informací, kde se i píší případy použití, nicméně já bych nyní chtěl něco ve stylu:
Tato metoda je velmi užitečná zvláště v situacích...
Tato metoda není zásadní, ale může se hodit v situacích...


A tady tedy tahák z kterého můžeš čerpat:

1. verify(podmínka, zpráva=None, exception_type=VerifyError):

Popis:
Univerzální metoda pro ověřování podmínek.
Slouží k zjednodušení ověřování vstupních hodnot a podmínek v kódu.
Pokud podmínka není splněna, vyvolá výjimku.
Použití:
verify(isinstance(value, str), "Hodnota musí být řetězec")
verify(value > 0, "Hodnota musí být kladná")
verify(condition, exception_type=CustomError)
Kdy se hodí:
Pro ověření typu proměnné.
Pro ověření platnosti hodnoty.
Pro ověření složitějších podmínek.
Pro zjednodušení a zpřehlednění kódu, kde se často vyskytují kontroly a vyvolávání výjimek.


2. safe_verify(podmínka, zpráva=None, exception_type=SafeVerifyError):

Popis:
Bezpečná interní metoda pro ověřování vstupů v rámci třídy ExceptionHandler.
Podobná metodě verify(), ale s dodatečnými bezpečnostními mechanismy, aby se předešlo rekurzivním chybám.
Použití:
Používá se interně v metodách třídy ExceptionHandler pro ověření vstupních parametrů.
Kdy se hodí:
Pro ověřování vstupů v rámci metod, které samy pracují s výjimkami, aby se zabránilo nekonečnému cyklu.


3. catch(exceptions, log_level=None, message=None):

Popis:
Dekorátor pro zachytávání a zpracování výjimek.
Umožňuje elegantní a centralizované zpracování výjimek u funkcí a metod.
Konfigurovatelné logování a chování při výjimce.
Použití:
@exception_catch(ValueError, TypeError)
@exception_catch(log_level=logging.WARNING)
@exception_catch(message="Kritická chyba v procesu")
Kdy se hodí:
Pro zjednodušení kódu a odstranění redundantních try-except bloků.
Pro jednotné zpracování výjimek v rámci aplikace.
Pro flexibilní logování a reakci na různé typy výjimek.


4. handle(exception_type, handler, reraise=True):

Popis:
Metoda pro registraci vlastního handleru (funkce) pro specifickou výjimku.
Umožňuje definovat, co se má stát, když je daná výjimka zachycena.
Použití:
exception_handler.handle(KeyError, handler=lambda e: print(f"Zachycen KeyError: {e}"), reraise=False)
Kdy se hodí:
Pro specifické zpracování určitých typů výjimek.
Pro oddělení logiky zpracování výjimek od hlavní logiky kódu.
Pro flexibilní reakci na výjimky (např. logování, zobrazení uživateli, opakování akce).


5. set_log_level(log_level, exception_type=None):

Popis:
Metoda pro nastavení úrovně logování pro specifickou výjimku nebo globálně.
Umožňuje detailní kontrolu nad tím, jaké informace o výjimkách se budou logovat.
Použití:
handler.set_log_level(logging.WARNING, ValueError)
handler.set_log_level(logging.ERROR)
Kdy se hodí:
Pro nastavení různé úrovně logování pro různé typy výjimek (např. pro kritické chyby logovat podrobněji).
Pro dočasné zvýšení úrovně logování pro ladění.


6. set_message(message, exception_type=None):

Popis:
Metoda pro nastavení vlastní chybové zprávy pro specifickou výjimku nebo globálně.
Umožňuje přizpůsobit chybové hlášky, které se logují nebo zobrazují uživateli.
Použití:
handler.set_message("Kritická chyba validace", ValueError)
handler.set_message("Obecná chyba")
Kdy se hodí:
Pro srozumitelnější a uživatelsky přívětivější chybové hlášky.
Pro specifikaci kontextu chyby v logu.


7. set_log_format(log_format, exception_type=None):

Popis:
Metoda pro nastavení formátu logování pro specifickou výjimku nebo globálně.
Umožňuje přizpůsobit vzhled a obsah logovacích zpráv.
Použití:
handler.set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError)
handler.set_log_format("%(levelname)s: %(message)s")
Kdy se hodí:
Pro přizpůsobení logovacích zpráv formátu, který vyhovuje potřebám projektu nebo logovacího systému.
Pro přidání specifických informací do logů (např. čas, úroveň, název souboru).


8. set_default_handler(handler):

Popis:
Metoda pro nastavení globálního fallback handleru pro nezachycené výjimky.
Umožňuje definovat, co se má stát, pokud žádný specifický handler nezachytí danou výjimku.
Použití:
handler.set_default_handler(lambda e: print(f"Nezachycená výjimka: {e}"))
Kdy se hodí:
Pro zajištění jednotného zpracování všech výjimek, i těch neočekávaných.
Pro logování nebo hlášení chyb, které by jinak nebyly zpracovány.


9. register_global_handler(handler, *exception_types):

Popis:
Metoda pro registraci globálního handleru pro specifické typy výjimek.
Umožňuje centralizované zpracování chyb pro určité typy výjimek v rámci celé aplikace.
Použití:
handler.register_global_handler(lambda e: print(f"Zachycena globální výjimka: {e}"), ValueError, TypeError)
Kdy se hodí:
Pro jednotné zpracování chyb určitého typu v celé aplikaci (např. logování všech chyb databáze).
Pro implementaci globálních politik zpracování chyb.


10. create_exception_group(group_name, *exception_types):

Popis:
Metoda pro vytvoření skupiny příbuzných výjimek.
Umožňuje seskupit výjimky, které mají podobný význam nebo se s nimi zachází podobně.
Použití:
handler.create_exception_group("data_errors", ValueError, TypeError, KeyError)
Kdy se hodí:
Pro usnadnění kategorizace a zpracování výjimek.
Pro definování společných pravidel pro skupiny výjimek.


11. set_retry_strategy(exception_type, max_attempts, delay, backoff=2):

Popis:
Metoda pro nastavení strategie opakování pro specifické výjimky.
Umožňuje automatické opakování akce, která vyvolala výjimku.
Použití:
handler.set_retry_strategy(ValueError, max_attempts=3, delay=0.5)
Kdy se hodí:
Pro automatické opakování operací, které mohou dočasně selhat (např. síťové operace, přístup k databázi).
Pro zvýšení odolnosti aplikace proti chybám.

## ChatGPT:

Tady máš strukturovaný přehled užitečnosti jednotlivých metod spolu s jejich příklady použití. Seřadil jsem je od nejzásadnějších po ty méně důležité:

## Nejzásadnější metody

### 1. `catch(exceptions, log_level=None, message=None)`
**Velmi užitečná** – Dekorátor, který elegantně nahrazuje `try/except` bloky.
#### Příklady použití:
```python
@exception_handler.catch(ValueError, TypeError)
def process_data(data):
    return int(data) * 2
```
- Použitelné pro konsolidované a čisté zpracování výjimek.
- Umožňuje centrální konfiguraci zpracování chyb.

---

### 2. `handle(exception_type, handler, reraise=True)`
**Velmi užitečná** – Poskytuje flexibilitu ve způsobu zacházení s výjimkami.
#### Příklady použití:
```python
handler.handle(KeyError, lambda e: print(f"Klíč nebyl nalezen: {e}"), reraise=False)
```
- Vhodné pro oddělení logiky výjimek od hlavního kódu.
- Usnadňuje správu chyb v rozsáhlých projektech.

---

### 3. `verify(podmínka, zpráva=None, exception_type=VerifyError)`
**Užitečná** – Zjednodušuje ověřování podmínek, nahrazuje opakující se `if` kontroly.
#### Příklady použití:
```python
verify(isinstance(value, str), "Hodnota musí být řetězec")
verify(value > 0, "Hodnota musí být kladná")
```
- Přehlednější a stručnější než ruční `if/raise` bloky.
- Užitečné pro validaci vstupů i v komplexních aplikacích.

---

### 4. `set_default_handler(handler)`
**Velmi užitečná** – Umožňuje globální zachycení nečekaných chyb.
#### Příklady použití:
```python
handler.set_default_handler(lambda e: print(f"Nezachycená výjimka: {e}"))
```
- Vhodné pro frameworky a aplikace, kde chceme centrálně spravovat chyby.
- Zajišťuje, že žádná výjimka neprojde bez povšimnutí.

---

## Středně důležité metody

### 5. `safe_verify(podmínka, zpráva=None, exception_type=SafeVerifyError)`
**Užitečná v určitých situacích** – Bezpečnější varianta `verify()`, která brání rekurzivním chybám.
#### Příklad:
```python
safe_verify(isinstance(param, int), "Očekává se celé číslo")
```
- Užitečné v metodách pracujících s výjimkami.
- Zabraňuje nekonečným cyklům při nesprávném zacházení s výjimkami.

---

### 6. `set_log_level(log_level, exception_type=None)`
**Užitečná** – Umožňuje kontrolu úrovně logování chyb.
#### Příklad:
```python
handler.set_log_level(logging.WARNING, ValueError)
```
- Hodí se pro odlišné nastavení kritických a méně závažných chyb.
- Může pomoci při ladění aplikace.

---

### 7. `set_message(message, exception_type=None)`
**Užitečná** – Umožňuje přizpůsobit chybová hlášení.
#### Příklad:
```python
handler.set_message("Neplatná hodnota", ValueError)
```
- Zlepšuje srozumitelnost chybových zpráv.
- Pomáhá při ladění a práci s uživatelskými chybami.

---

## Méně zásadní metody

### 8. `set_log_format(log_format, exception_type=None)`
**Užitečná v určitých situacích** – Umožňuje přizpůsobení formátu logů.
#### Příklad:
```python
handler.set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError)
```
- Hodí se, pokud má aplikace specifické požadavky na logování.
- Nezbytné pouze pro komplexní logging systémy.

---

### 9. `register_global_handler(exception_type, handler)`
**Středně užitečná** – Umožňuje globální registraci handlerů.
#### Příklad:
```python
handler.register_global_handler(IOError, lambda e: print(f"Soubor nenalezen: {e}"))
```
- Praktické pro aplikace s jednotnou správou výjimek.
- Může být nahrazeno jinými metodami, jako je `handle()`.

---

### 10. `create_exception_group(name, *exceptions)`
**Málo používaná, ale někdy užitečná** – Slouží k seskupení výjimek pod společný název.
#### Příklad:
```python
handler.create_exception_group("FileErrors", FileNotFoundError, IOError)
```
- Použitelné v aplikacích s rozsáhlým chybovým systémem.
- V běžných případech není nezbytné.

---

### 11. `set_retry_strategy(exception_type, strategy_func)`
**Užitečná v některých scénářích** – Umožňuje definovat strategie opakování operací.
#### Příklad:
```python
def retry_logic():
    print("Opakování operace...")
handler.set_retry_strategy(ConnectionError, retry_logic)
```
- Užitečné pro síťové aplikace a automatizaci.
- V běžném kódu nemusí být potřeba.

---

## Shrnutí

- **Nejdůležitější metody**: `catch()`, `handle()`, `verify()`, `set_default_handler()`
- **Středně důležité metody**: `safe_verify()`, `set_log_level()`, `set_message()`
- **Méně důležité metody**: `set_log_format()`, `register_global_handler()`, `create_exception_group()`, `set_retry_strategy()`

Hlavní otázka při rozhodování o metodách: Jak často je budete používat a v jakém kontextu? Nejzásadnější metody jsou klíčové pro elegantní správu chyb, zatímco ostatní jsou užitečné jen ve specifických situacích.


Připravil jsem přehled užitečnosti jednotlivých metod spolu s jejich příklady použití. Můžeš se na něj podívat a upravit podle svých potřeb. Dej vědět, jestli chceš něco doplnit nebo přeuspořádat! 🚀

## Dotaz:

Super a díky moc, to hodně pomohlo :-)

Právě že funkcionalit je najednou hodně a z jednoduché metody se vyklubala celkem obsáhlá aplikace.

Rád bych ji ae dotáhl až do podoby knihovny, protože mi příjde že z tohoto přístupu bych nemusel těžit jenom já v budoucích kodech, ale možná by se mohl setkat se zájmem i jako samostatná knihovna pro jiné :-)

V plánu mám zítra vše vytvořit od znova abych s kod pořádně ošahal a pochopil jednotlivé změny které jsou v jednotlivých verzích postupného vývoje, tak abych jim více porozuměl do hloubky. Takže toto stručné rozebrání a zhodnocení od tebe mi pomohlo :-)

To co by bylo ještě dobré kdyby jsi mi dokázal zhodnotit, zda je lepší vytvořit tuto knihovnu čistě jen na základě:
Nejdůležitější metody: catch(), handle(), verify(), set_default_handler()

A udělat ji velmi lehkou, a nebo bys mi doporučil použít všechny vytvořené metody, s tím že nepředstavují zase tak velkou zátěž a někomu by se mohli hodit.

Která z těchto cest je lepší a kterou bych se měl vydat? 

## ChatGPT:

Tohle je skvělý směr! 🎯  

Máš pravdu, že by se z této knihovny mohlo stát něco užitečného i pro ostatní. Když se rozhoduješ mezi minimalistickou verzí (`catch()`, `handle()`, `verify()`, `set_default_handler()`) a rozšířenou verzí se všemi metodami, přemýšlej nad tímto:  

1. **Jádro knihovny** – Minimalistická verze je skvělá pro začátek, protože pokrývá základní potřeby správy výjimek. Bude lehká, snadno pochopitelná a dobře rozšířitelná v budoucnu.  
2. **Modularita** – Můžeš to udělat tak, že základní verze obsahuje jen nejdůležitější metody, ale přidáš volitelné moduly (`extra_logging`, `retry`, `global_handling`), které si uživatel může zapnout podle potřeby.  
3. **Komunita** – Pokud plánuješ knihovnu otevřít veřejnosti, nech si zpětnou vazbu od uživatelů a postupně přidávej funkce, které opravdu potřebují.  

**Moje doporučení:**  
✅ Začni s minimalistickou verzí. Jakmile bude stabilní a dobře použitelná, můžeš přidat další funkce jako volitelné rozšíření. To ti dá čas pochopit, co je opravdu potřeba, a zároveň to nebude zbytečně robustní hned od začátku.  

Co na to říkáš? 🚀

## Dotaz:

Kdybys to měl rozepsat do jednotlivých kroků, jak by jsi mě doporučil postupovat?

## ChatGPT:

Tady je strukturovaný plán, jak postupovat při vývoji a rozšíření knihovny:  

### **1. Základní implementace (MVP)**
🔹 **Cíl**: Vytvořit funkční jádro knihovny s klíčovými metodami.  
✅ **Akce**:  
- Implementuj **čtyři nejzásadnější metody**:  
  - `catch()`  
  - `handle()`  
  - `verify()`  
  - `set_default_handler()`  
- Napiš základní **testy jednotek** pro ověření funkcionality.  
- Připrav základní **dokumentaci** (krátké popisy metod + příklady použití).  

---

### **2. Refinement & Optimalizace**
🔹 **Cíl**: Vyladit a zpřehlednit základní API.  
✅ **Akce**:  
- Otestuj knihovnu na reálných scénářích.  
- Projděte si názvy metod – jsou dostatečně intuitivní?  
- Optimalizuj výkon a minimalizuj závislosti.  

---

### **3. Rozšíření funkcionality**
🔹 **Cíl**: Přidat užitečné, ale ne kritické metody.  
✅ **Akce**:  
- Implementuj **středně důležité metody**:  
  - `safe_verify()`  
  - `set_log_level()`  
  - `set_message()`  
- Přidej volitelné parametry ke stávajícím metodám pro větší flexibilitu.  
- Rozšiř testovací sadu na více případů použití.  

---

### **4. Pokročilé funkce a modularizace**
🔹 **Cíl**: Připravit rozšířené možnosti pro náročnější uživatele.  
✅ **Akce**:  
- Přidej **méně důležité metody** jako volitelné moduly:  
  - `set_log_format()`, `register_global_handler()`, `create_exception_group()`, `set_retry_strategy()`.  
- Zvaž rozdělení na **jádro + rozšiřující moduly**.  

---

### **5. Publikace a zpětná vazba**
🔹 **Cíl**: Otevřít knihovnu světu a získat zpětnou vazbu.  
✅ **Akce**:  
- Vytvoř **README** s přehledným vysvětlením a příklady.  
- Publikuj balíček na **PyPI**.  
- Sdílej knihovnu a sbírej zpětnou vazbu od uživatelů.  
- Na základě zpětné vazby uprav funkcionalitu nebo API.  

---

Co na to říkáš? 🚀

## Dotaz:

To zní dobře :-)

Mohl bys mi měl nyní z toho co víš, a za předpokladu že budu následovat všechny kroky, nějak slovy popsat smysl a využití této knihovny, tak jako bych to psal někam na web, kde bych chtěl jen o ní informovat slovně o tom, co vše nabízí a co se skrze ní dá dělat?

A jestli bys i to mohl rozdělit do těchto tří kategorií: základní implementace, rozšíření, pokročilé funkce.

## ChatGPT:

Jasně, tady je návrh popisu knihovny rozdělený do tří kategorií:

---

# 📌 **Představujeme Exception Handler – elegantní správu výjimek pro vaše Python projekty**  

Knihovna **Exception Handler** přináší snadný a přehledný způsob práce s výjimkami. Umožňuje konsolidovat správu chyb, eliminovat opakující se `try/except` bloky a poskytuje flexibilní nástroje pro logování i automatizované zpracování chyb.  

## 🔹 **Základní implementace**  
Pokud chcete **jednoduše zachytávat výjimky**, ale přitom udržet kód čistý a přehledný, stačí využít dekorátor `catch()`:  

```python
@exception_handler.catch(ValueError)
def convert(value):
    return int(value)
```

✔️ Nahrazuje `try/except` bloky  
✔️ Umožňuje definovat chování pro specifické chyby  
✔️ Funguje ihned bez složité konfigurace  

---

## 🔹 **Rozšíření možností**  
Chcete **více kontroly nad výjimkami**? Exception Handler umožňuje:  

✅ **Definovat vlastní zpracování chyb** pomocí `handle()`:  
```python
handler.handle(KeyError, lambda e: print(f"Chyba: {e}"), reraise=False)
```

✅ **Ověřovat podmínky jednodušeji** pomocí `verify()`:  
```python
verify(len(password) > 8, "Heslo musí mít alespoň 8 znaků")
```

✅ **Nastavit globální handler pro nezachycené výjimky**:  
```python
handler.set_default_handler(lambda e: print(f"Nepředpokládaná chyba: {e}"))
```

✔️ Přehlednější validace vstupů  
✔️ Možnost centrálního logování  
✔️ Flexibilní reakce na chyby  

---

## 🔹 **Pokročilé funkce pro robustní aplikace**  
Pro **komplexní projekty** nabízí knihovna pokročilé možnosti:  

🚀 **Logování s vlastním formátem** (`set_log_format()`)  
🚀 **Globální registrace handlerů** (`register_global_handler()`)  
🚀 **Seskupení výjimek pod společný název** (`create_exception_group()`)  
🚀 **Definování strategií opakování operací** (`set_retry_strategy()`)  

Tyto funkce umožňují **automatizovat správu výjimek**, udržet konzistenci napříč projektem a minimalizovat nečekané chyby v produkčním prostředí.  

---

💡 **Ať už stavíte malý skript nebo rozsáhlou aplikaci, Exception Handler vám pomůže spravovat výjimky efektivně a přehledně.**  

Co říkáš? Mám to nějak upravit, doplnit nebo zjednodušit? 😊

## Dotaz:

Super takto je to dobrý, ono je to hlavně pro mě, jen abych to viděl i takto zapsané :-) 

Dokázal bys mi zhodnotit, zda kromě těchto 11 funkcionalit je ještě něco co by bylo rozhodně dobré kdyby měla a nebo je to takto kompletní a pro účely knihovny plně dostačující?

## ChatGPT:

Celkově je sada funkcionalit velmi dobře promyšlená a pokrývá širokou škálu scénářů zpracování výjimek. Máš dobře vyvážený poměr mezi jednoduchými a pokročilými funkcemi, což knihovnu činí užitečnou jak pro běžné použití, tak pro složitější aplikace.  

### Co by mohlo ještě přidat hodnotu?
1. **Zachytávání více výjimek najednou ve `catch()`**  
   - Možnost zadat více výjimek jako tuple:
   ```python
   @exception_handler.catch((ValueError, TypeError))
   def process(data):
       return int(data) * 2
   ```
   - Možná už to umíš, ale pokud ne, tak by to mohlo zvýšit flexibilitu.

2. **Možnost ignorovat výjimky (`ignore_exceptions`)**  
   - Občas je potřeba určitou chybu ignorovat a pokračovat dál, místo jejího logování nebo reraise.
   ```python
   handler.ignore_exceptions(ValueError)
   ```
   - Užitečné pro robustní skripty, kde některé chyby nemají bránit dalším operacím.

3. **Automatický sběr traceback informací**  
   - Knihovna by mohla obsahovat volitelnou funkci pro zachytávání tracebacku a ukládání do souboru/logu.
   ```python
   handler.enable_traceback_logging("errors.log")
   ```
   - Mohlo by to být užitečné v produkčním nasazení.

4. **Podpora asynchronního zpracování chyb**  
   - Pokud používáš `asyncio`, knihovna by mohla obsahovat variantu dekorátoru `catch_async()` pro `async` funkce.
   ```python
   @exception_handler.catch_async(ValueError)
   async def async_process(data):
       return int(data) * 2
   ```

Pokud se zaměřuješ na jednoduchost a přehlednost, tak současná sada funkcí vypadá už dost kompletně. Pokud ale plánuješ knihovnu rozšiřovat pro robustnější použití, výše uvedené návrhy by mohly být zajímavé. 😊

## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



## Dotaz:



## ChatGPT:



