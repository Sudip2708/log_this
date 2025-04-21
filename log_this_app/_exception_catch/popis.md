Používám soubor "text_na_zpracování.txt" pro extrahování podstatných informací o metodách.

**1. verify(podmínka, zpráva=None, exception_type=VerifyError):**

*   **Popis:**
    *   Univerzální metoda pro ověřování podmínek.
    *   Slouží k zjednodušení ověřování vstupních hodnot a podmínek v kódu.
    *   Pokud podmínka není splněna, vyvolá výjimku.
*   **Použití:**
    *   `verify(isinstance(value, str), "Hodnota musí být řetězec")`
    *   `verify(value > 0, "Hodnota musí být kladná")`
    *   `verify(condition, exception_type=CustomError)`
*   **Kdy se hodí:**
    *   Pro ověření typu proměnné.
    *   Pro ověření platnosti hodnoty.
    *   Pro ověření složitějších podmínek.
    *   Pro zjednodušení a zpřehlednění kódu, kde se často vyskytují kontroly a vyvolávání výjimek.

**2. safe_verify(podmínka, zpráva=None, exception_type=SafeVerifyError):**

*   **Popis:**
    *   Bezpečná interní metoda pro ověřování vstupů v rámci třídy `ExceptionHandler`.
    *   Podobná metodě `verify()`, ale s dodatečnými bezpečnostními mechanismy, aby se předešlo rekurzivním chybám.
*   **Použití:**
    *   Používá se interně v metodách třídy `ExceptionHandler` pro ověření vstupních parametrů.
*   **Kdy se hodí:**
    *   Pro ověřování vstupů v rámci metod, které samy pracují s výjimkami, aby se zabránilo nekonečnému cyklu.

**3. catch(*exceptions, log_level=None, message=None):**

*   **Popis:**
    *   Dekorátor pro zachytávání a zpracování výjimek.
    *   Umožňuje elegantní a centralizované zpracování výjimek u funkcí a metod.
    *   Konfigurovatelné logování a chování při výjimce.
*   **Použití:**
    *   `@exception_catch(ValueError, TypeError)`
    *   `@exception_catch(log_level=logging.WARNING)`
    *   `@exception_catch(message="Kritická chyba v procesu")`
*   **Kdy se hodí:**
    *   Pro zjednodušení kódu a odstranění redundantních `try-except` bloků.
    *   Pro jednotné zpracování výjimek v rámci aplikace.
    *   Pro flexibilní logování a reakci na různé typy výjimek.

**4. handle(exception_type, handler, reraise=True):**

*   **Popis:**
    *   Metoda pro registraci vlastního handleru (funkce) pro specifickou výjimku.
    *   Umožňuje definovat, co se má stát, když je daná výjimka zachycena.
*   **Použití:**
    *   `exception_handler.handle(KeyError, handler=lambda e: print(f"Zachycen KeyError: {e}"), reraise=False)`
*   **Kdy se hodí:**
    *   Pro specifické zpracování určitých typů výjimek.
    *   Pro oddělení logiky zpracování výjimek od hlavní logiky kódu.
    *   Pro flexibilní reakci na výjimky (např. logování, zobrazení uživateli, opakování akce).

**5. set_log_level(log_level, exception_type=None):**

*   **Popis:**
    *   Metoda pro nastavení úrovně logování pro specifickou výjimku nebo globálně.
    *   Umožňuje detailní kontrolu nad tím, jaké informace o výjimkách se budou logovat.
*   **Použití:**
    *   `handler.set_log_level(logging.WARNING, ValueError)`
    *   `handler.set_log_level(logging.ERROR)`
*   **Kdy se hodí:**
    *   Pro nastavení různé úrovně logování pro různé typy výjimek (např. pro kritické chyby logovat podrobněji).
    *   Pro dočasné zvýšení úrovně logování pro ladění.

**6. set_message(message, exception_type=None):**

*   **Popis:**
    *   Metoda pro nastavení vlastní chybové zprávy pro specifickou výjimku nebo globálně.
    *   Umožňuje přizpůsobit chybové hlášky, které se logují nebo zobrazují uživateli.
*   **Použití:**
    *   `handler.set_message("Kritická chyba validace", ValueError)`
    *   `handler.set_message("Obecná chyba")`
*   **Kdy se hodí:**
    *   Pro srozumitelnější a uživatelsky přívětivější chybové hlášky.
    *   Pro specifikaci kontextu chyby v logu.

**7. set_log_format(log_format, exception_type=None):**

*   **Popis:**
    *   Metoda pro nastavení formátu logování pro specifickou výjimku nebo globálně.
    *   Umožňuje přizpůsobit vzhled a obsah logovacích zpráv.
*   **Použití:**
    *   `handler.set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError)`
    *   `handler.set_log_format("%(levelname)s: %(message)s")`
*   **Kdy se hodí:**
    *   Pro přizpůsobení logovacích zpráv formátu, který vyhovuje potřebám projektu nebo logovacího systému.
    *   Pro přidání specifických informací do logů (např. čas, úroveň, název souboru).

**8. set_default_handler(handler):**

*   **Popis:**
    *   Metoda pro nastavení globálního fallback handleru pro nezachycené výjimky.
    *   Umožňuje definovat, co se má stát, pokud žádný specifický handler nezachytí danou výjimku.
*   **Použití:**
    *   `handler.set_default_handler(lambda e: print(f"Nezachycená výjimka: {e}"))`
*   **Kdy se hodí:**
    *   Pro zajištění jednotného zpracování všech výjimek, i těch neočekávaných.
    *   Pro logování nebo hlášení chyb, které by jinak nebyly zpracovány.

**9. register_global_handler(handler, \*exception_types):**

*   **Popis:**
    *   Metoda pro registraci globálního handleru pro specifické typy výjimek.
    *   Umožňuje centralizované zpracování chyb pro určité typy výjimek v rámci celé aplikace.
*   **Použití:**
    *   `handler.register_global_handler(lambda e: print(f"Zachycena globální výjimka: {e}"), ValueError, TypeError)`
*   **Kdy se hodí:**
    *   Pro jednotné zpracování chyb určitého typu v celé aplikaci (např. logování všech chyb databáze).
    *   Pro implementaci globálních politik zpracování chyb.

**10. create_exception_group(group_name, \*exception_types):**

*   **Popis:**
    *   Metoda pro vytvoření skupiny příbuzných výjimek.
    *   Umožňuje seskupit výjimky, které mají podobný význam nebo se s nimi zachází podobně.
*   **Použití:**
    *   `handler.create_exception_group("data_errors", ValueError, TypeError, KeyError)`
*   **Kdy se hodí:**
    *   Pro usnadnění kategorizace a zpracování výjimek.
    *   Pro definování společných pravidel pro skupiny výjimek.

**11. set_retry_strategy(exception_type, max_attempts, delay, backoff=2):**

*   **Popis:**
    *   Metoda pro nastavení strategie opakování pro specifické výjimky.
    *   Umožňuje automatické opakování akce, která vyvolala výjimku.
*   **Použití:**
    *   `handler.set_retry_strategy(ValueError, max_attempts=3, delay=0.5)`
*   **Kdy se hodí:**
    *   Pro automatické opakování operací, které mohou dočasně selhat (např. síťové operace, přístup k databázi).
    *   Pro zvýšení odolnosti aplikace proti chybám.