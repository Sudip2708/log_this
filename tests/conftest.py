"""
conftest.py

Je standardní název, který pytest používá pro sdílené konfigurace, fixturny a další nastavení.

Tento soubor:
- Je automaticky načten pytestem: Pokud je umístěn v kořenovém adresáři projektu nebo ve složkách s testy.
- Má hierarchický rozsah: Pokud máte více souborů conftest.py v různých adresářích, platí nastavení pouze pro testy ve stejné složce a jejích podadresářích.
- Nepotřebuje explicitní importy: Fixturny definované v conftest.py jsou automaticky dostupné ve všech testech v jeho dosahu.
- Pytest tento soubor rozpozná díky jeho pevnému názvu, takže změnit jej na jiný název (např. my_conftest.py) by znamenalo, že pytest nebude soubor automaticky detekovat.

Proč to dělat tímto způsobem:
Znovupoužitelnost:
- Fixturny (capture_logs, mock_function, complex_object) poskytují opakovaně využitelný základ pro více testovacích scénářů.
- Nemusíte psát podobný kód ve více testech.

Izolace:
- Zachytávání logů (capture_logs) a práce s mock funkcemi (mock_function) zajistí, že testy jsou nezávislé na externích faktorech (např. na skutečných datech nebo funkcích).

Lepší správa testů:
- Centralizace konfigurací a společných zdrojů v conftest.py usnadňuje údržbu testů a sdílení fixturní logiky.

Efektivita:
- Minimalizuje duplicitu kódu.
- Umožňuje rychle přidávat nebo měnit chování fixturní logiky na jednom místě.

---

**Doporučený postup při vytváření testů:**

1. **Začněte základními jednotkovými testy:**
   - Testujte jednotlivé funkce a třídy.
   - Příklad: Testujte dekorátor `@log_this` s jednoduchými funkcemi.

2. **Postupujte k testování jednotlivých režimů logování:**
   - Testujte, zda různé režimy `mode` fungují správně (např. `_log_simple`, `_log_detailed`).
   - Příklad: Zkontrolujte, zda se správně logují parametry a návratové hodnoty.

3. **Zaměřte se na validaci konfigurace:**
   - Testujte funkce v adresáři `config/data/mixins_data`, např. validaci konfigurace a její načítání.

4. **Testujte serializaci a další pomocné funkce:**
   - Například testujte `_safe_serialize` pro správné zpracování složitých objektů.

5. **Provádějte integrační testy:**
   - Simulujte reálné scénáře využití knihovny, např. jak funguje logování v kombinaci s různými režimy a objekty.

6. **Otestujte hraniční případy a chyby:**
   - Testujte neplatné vstupy a chování knihovny při výjimečných situacích.

7. **Dokončete testování s testy výkonu:**
   - Změřte čas zpracování logování a zjistěte, zda knihovna neovlivňuje výkon aplikace.

---

**Seznam testovacích cílů pro vaši knihovnu:**

1. **Základní testy:**
   - Funkčnost dekorátoru `@log_this`.
   - Správné nastavení loggeru.

2. **Testování módů logování:**
   - `@log_this(mode="simple")`
   - `@log_this(mode="detailed")`
   - A další režimy.

3. **Konfigurace:**
   - Načítání a validace konfigurace.

4. **Pomocné funkce:**
   - Serializace objektů.
   - Práce s docstringy.

5. **Integrační testy:**
   - Využití knihovny v komplexních scénářích.

6. **Výkonnostní testy:**
   - Ověření rychlosti logování.

"""
import logging
from tests._fixtures import (
    capture_logs,  # Fixture pro zachycení log výstupů.
    mock_function,   # Fixture pro vytvoření jednoduché mock funkce pro testování logování.
    complex_object,   # Fixture pro vytvoření komplexního objektu pro testování serializace.
)

def pytest_configure(config):
    """Konfigurace pytest pro lepší výstup a chování.

    Nastavuje custom markery a úroveň logování.

    Args:
        config (_pytest.config.Config): Konfigurace pytest
    """
    config.addinivalue_line(
        "markers",
        "log_mode: marker pro testování různých módů logování"
    )
    logging.basicConfig(level=logging.DEBUG)


