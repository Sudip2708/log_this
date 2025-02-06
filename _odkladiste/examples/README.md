# Log This Decorator Library

## Úvod

Knihovna `log_this` poskytuje flexibilní nástroj pro logování funkcí s různými úrovněmi podrobnosti.

## Instalace

```bash
pip install log-this
```

## Základní použití

### Jednoduché logování

```python
from log_this import log_this

@log_this(1)  # Úroveň logování
def moje_funkce(x, y):
    return x + y
```

## Úrovně logování

Knihovna podporuje následující úrovně logování:

- `0` nebo `False`: Bez logování
- `1`: Základní informace (název funkce, vstupní parametry)
- `2`: Stručný výpis (přidává výstupní hodnotu)
- `3`: Rozšířený výpis (doba běhu, využití paměti)
- `4`: Kompletní výpis (analýza prostředků, docstring)

## Příklady

### Vnořené funkce

```python
@log_this(2)
def hlavni_funkce():
    @log_this(1)
    def vedlejsi_funkce():
        pass
```

## Demo

Pro ukázky použití navštivte složku `examples/` v repozitáři.

## Licence

[Vaše licence]

## Přispívání

Příspěvky jsou vítány! Prosím, řiďte se guidelines v CONTRIBUTING.md.