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

