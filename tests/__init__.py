"""
## Spouštění testů pomocí pytest a jeho možnosti

**Základní příkaz pro spuštění všech testů v aktuálním adresáři je:**

```bash
pytest
```

**Další užitečné příkazy a možnosti:**

  * **Spuštění konkrétního testu nebo skupiny testů:**
      * **Podle názvu:** `pytest test_module.py::test_function`
      * **Podle značky:** `pytest -m slow` (pokud jsou testy označeny značkami)
  * **Změna úrovně verbóznosti:**
      * `-v`: Více informací o průběhu testů
      * `-q`: Méně informací, pouze shrnutí
  * **Vybrání testů podle exprese:**
      * `pytest -k "test_function or another_test"`
  * **Zastavení po prvním selhání:**
      * `-x`
  * **Paralelní spuštění testů:**
      * `-n auto`: Automatické určení počtu pracovníků
  * **Generování HTML reportu:**
      * `--html=report.html`
  * **Přeskočení určitých testů:**
      * `-m "not slow"`
  * **Použití vlastních pluginů:**
      * `--pyargs pytest_my_plugin`
  * **Nastavení pracovní složky:**
      * `-c pytest.ini`

**Příklady použití:**

  * **Spuštění všech testů v adresáři `tests`:**
    ```bash
    pytest tests
    ```
  * **Spuštění pouze pomalých testů:**
    ```bash
    pytest -m slow
    ```
  * **Spuštění testu `test_login` v souboru `test_auth.py` a generování HTML reportu:**
    ```bash
    pytest test_auth.py::test_login --html=report.html
    ```
  * **Paralelní spuštění všech testů s maximálně 4 pracovníky:**
    ```bash
    pytest -n 4
    ```

**Konfigurační soubor `pytest.ini`**

V tomto souboru lze nastavit globální konfiguraci pro pytest. Mezi běžné možnosti patří:

  * **Adresáře, ve kterých se hledají testy**
  * **Výchozí značky**
  * **Pluginy**
  * **Možnosti příkazové řádky**

**Další užitečné možnosti a pluginy**

Pytest nabízí mnoho dalších možností a pluginů, které mohou usnadnit a rozšířit vaše testování. Některé z nich jsou:

  * **xdist:** Rozšíření pro distribuované testování
  * **cov-py:** Měření pokrytí kódu testy
  * **pytest-mock:** Mocking a patching
  * **pytest-bdd:** Behavior-driven development

**Více informací**

Podrobnější informace a další možnosti naleznete v oficiální dokumentaci pytest: [https://docs.pytest.org/en/latest/](https://www.google.com/url?sa=E&source=gmail&q=https://docs.pytest.org/en/latest/)

**Tipy pro efektivní testování s pytest**

  * **Píšete testy průběžně:** Nečekejte, až budete mít celý kód hotový.
  * **Testy by měly být jednoduché a čitelné.**
  * **Každý test by měl testovat pouze jednu věc.**
  * **Využívejte fixtures pro sdílení dat mezi testy.**
  * **Automatizujte spouštění testů.**

**Potřebujete další pomoc?**

Pokud máte konkrétní otázku nebo problém související s pytest, neváhejte se zeptat. Ráda vám pomůžu s dalšími detaily a příklady.

**Chcete se dozvědět více o nějakém konkrétním tématu souvisejícím s pytest?** Například:

  * Jak napsat efektivní testy?
  * Jak využít fixtures?
  * Jak měřit pokrytí kódu testy?
  * Jak používat pytest s jinými nástroji?

Stačí mi říct a já se pokusím vám poskytnout co nejvíce relevantních informací.

---


1. Spusťte pytest s verbose módem pro více detailů:
```bash
pytest -v -W always
```

2. Případně:
```bash
pytest -v --disable-warnings
```

3. Pokud chcete vidět přesný obsah varování, použijte:
```bash
pytest -v -W error
```


"""
