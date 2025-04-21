**Varianty dekorátoru `exception_catch`**

### **1) Základní dekorativní metoda**
- Dekorátor slouží k zachytávání výjimek.
- Je součástí třídy, která umožňuje globálně propojit logovací systém.
- Pokud není definováno jinak, používá se standardní logování.
- Nepodporuje pokročilé nastavení přes parametrizaci.
- Může obsahovat vnitřní `try-except` bloky pro dodatečnou logiku.

**Použití:**
```python
@exception_catch()
def some_function(some_parameters):
    try:
        some_logic()
    except TypeError as e:
        some_logic_for_this_error()
```
- Bez parametrů zachytává pouze `Exception` a loguje ji.
- S vyjmenováním výjimek zachytává pouze tyto výjimky:
```python
@exception_catch(ValueError, TypeError)
def some_function():
    some_logic()
```
- `TypeError` může být uvnitř funkce zpracován a nemusí být předán dekorátoru.

---

### **2) Pokročilejší verze s `ExceptionHandler`**
- Umožňuje pokročilou konfiguraci logování.
- Definuje hladinu logování, formát zprávy a přidává kontextové informace.
- Používá se přes instanci třídy `ExceptionHandler`.

**Použití:**
```python
handler = ExceptionHandler()

handler \
    .set_log_level(logging.WARNING, ValueError) \
    .set_message("Kritická chyba validace", ValueError) \
    .set_log_format("CUSTOM: %(message)s", ValueError) \
    .add_context("app_version", "1.0.0")

@handler.catch(ValueError, TypeError)
def example_function(x, y):
    return x / y
```
- Definuje se instance handleru a nastaví se logování.
- Dekorátor `@handler.catch` zachytává určité výjimky.

---

### **3) Dekorátor s vlastním `exception_handler.handle`**
- Kombinuje jednoduchost první varianty s větší flexibilitou.
- Každá výjimka může mít vlastní `handler`, který určí chování.
- Možno zvolit, zda se výjimka znovu vyvolá (`reraise=True`).

**Použití:**
```python
@exception_catch(KeyError)
def example_function():
    exception_handler.handle(
        KeyError,
        handler=lambda e: print(f"Zachycen KeyError: {e}"),
        reraise=False
    )
    return {}['neexistující_klíč']
```
- Zachytí `KeyError` a provede definovaný `handler`.
- Pokud `reraise=True`, výjimka je po zpracování znovu vyvolána.

---

**Shrnutí rozdílů:**
1) **Jednoduchý dekorátor** – Pouze propojení na logování a možnost vnitřního try-except.
2) **Konfigurovatelný `ExceptionHandler`** – Pokročilé logování a nastavení chování.
3) **Dekorátor s `handle` funkcí** – Flexibilní zachytávání a zpracování výjimek.

Další postup:
- Určit, která varianta bude implementována jako první.
- Definovat rozhraní a implementační kroky pro vybranou variantu.

