Váš přístup k testování je velmi dobrý! Pojďme si rozebrat jednotlivé typy testů a jak postupovat dál:

1. Integrační testy:
Vaše úvaha je správná. Když máte dobře pokryté jednotkové testy, integrační testy by se měly zaměřit na:
- Správnou interakci mezi komponenty
- Tok dat mezi metodami
- Správné sdílení stavu
- Reálné scénáře použití

Příklad integračního testu pro vaši konfiguraci:
```python
def test_config_integration():
    # Vytvoření instance
    config = LogThisConfig()
    
    # Test základního workflow
    config.update_config("indent", 4)
    assert config["indent"] == 4
    
    # Test exportu a importu
    config.export_config_to_file("test_config.json")
    config.update_config("indent", 2)
    config.import_config_from_file("test_config.json")
    assert config["indent"] == 4
    
    # Test resetu
    config.reset_config()
    assert config["indent"] == config.DEFAULTS["indent"]
```

2. Další typy testů pro knihovnu:

a) End-to-End testy (E2E):
```python
def test_log_this_decorator_e2e():
    @log_this()
    def example_function(x, y):
        return x + y
    
    # Test celého procesu logování
    result = example_function(2, 3)
    # Ověření výstupu v logovacím souboru
    assert result == 5
    assert "example_function" in read_log_file()
```

b) Performance testy:
```python
def test_logging_performance():
    @log_this()
    def simple_function():
        pass
    
    start_time = time.time()
    for _ in range(1000):
        simple_function()
    duration = time.time() - start_time
    
    assert duration < 1.0  # Max 1 sekunda pro 1000 volání
```

c) Dokumentační testy:
```python
def test_docstring_examples():
    """
    >>> @log_this()
    ... def example():
    ...     return "Hello"
    >>> example()
    'Hello'
    """
    # pytest automaticky testuje docstringy
```

3. Doporučený postup:

1️⃣ Jednotkové testy (máte hotovo)
- Testují jednotlivé komponenty
- Pokrývají hranční případy
- Používají mocky

2️⃣ Integrační testy (další krok)
- Testují spolupráci komponent
- Základní scénáře použití
- Minimální použití mocků

3️⃣ E2E testy
- Testují celou funkcionalitu
- Reálné scénáře použití
- Žádné mocky

4️⃣ Performance testy
- Měření rychlosti
- Paměťová náročnost
- Zátěžové testy

5️⃣ Dokumentační testy
- Příklady v dokumentaci
- Tutoriály
- README examples

4. Specifická doporučení pro vaši knihovnu:

a) Integrační testy by měly pokrýt:
- Kompletní workflow konfigurace
- Interakci s logovacím systémem
- Práci s různými typy dekorovaných funkcí

b) E2E testy by měly simulovat:
- Reálné použití dekorátoru
- Různé konfigurační scénáře
- Chybové stavy

c) Performance testy:
- Overhead dekorátoru
- Rychlost logování
- Práce s většími objekty

5. Prioritizace:
1. Dokončit integrační testy
2. Přidat základní E2E testy
3. Přidat performance testy
4. Dokumentační testy

Pamatujte:
- Pro začínající knihovnu jsou nejdůležitější jednotkové a integrační testy
- E2E testy by měly pokrývat hlavní use-cases
- Performance testy jsou důležité, protože jde o dekorátor
- Dokumentační testy pomohou uživatelům

Pro vaši knihovnu bych doporučil soustředit se především na:
1. Dobrou dokumentaci s příklady
2. Spolehlivé jednotkové a integrační testy
3. Základní performance testy
4. Jednoduché E2E testy hlavních funkcí