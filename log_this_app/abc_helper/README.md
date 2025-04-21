# ABC Helper

## Úvod

ABC Helper je lightweight knihovna zjednodušující práci s abstraktními třídami (ABC) v Pythonu. Poskytuje užitečné nástroje pro tvorbu, rozšiřování a správu abstraktních tříd a metod.

## Instalace

```bash
pip install abc-helper
```

## Hlavní funkce

- Zjednodušení práce s abstraktními metodami
- Podpora singleton vzoru pro abstraktní třídy
- Rozšířené nástroje pro logování a validaci
- Automatické generování dokumentace

## API Reference

### Základní abstraktní třídy a metody

#### `ABC`
Základní abstraktní bazální třída. Ekvivalent `abc.ABC` z knihovny `abc`.

#### `ABCMeta`
Metaclass pro tvorbu abstraktních tříd. Ekvivalent `abc.ABCMeta`.

#### `abstractmethod`
Dekorátor pro definici abstraktních metod. Ekvivalent `abc.abstractmethod`.

### Rozšířené utility

#### `AbcSingletonMeta`
Thread-safe metaclass pro implementaci singleton vzoru s podporou abstraktních tříd.

```python
from abc_helper import ABC, AbcSingletonMeta

class MySingleton(ABC, metaclass=AbcSingletonMeta):
    pass
```

### Zjednodušené definice abstraktních metod a vlastností

#### `abc_method(name: str, return_type: type = None, *params: str) -> Callable`
Zjednodušená tvorba abstraktních metod.

```python
from abc_helper import ABC, abc_method

class MyAbstractClass(ABC):
    # Namísto @abstractmethod def method(self): pass
    method = abc_method("method")
```

#### `abc_property(name: str, prop_type: type = Any) -> property`
Zjednodušená tvorba abstraktních properties.

```python
from abc_helper import ABC, abc_property

class MyAbstractClass(ABC):
    # Namísto @property @abstractmethod def prop(self): pass
    prop = abc_property("prop")
```

### Rozšířené nástroje

#### `@log_abstract_method(log_level: int = logging.DEBUG)`
Dekorátor pro přidání logování abstraktním metodám.

```python
from abc_helper import ABC, log_abstract_method

class MyClass(ABC):
    @log_abstract_method(logging.INFO)
    @abstractmethod
    def my_method(self, param: str) -> bool:
        pass
```

#### `@validate_abstract_method_types`
Dekorátor pro rozšířenou typovou kontrolu abstraktních metod.

```python
from abc_helper import ABC, validate_abstract_method_types
from typing import List, Dict

class MyValidator(ABC):
    @validate_abstract_method_types
    @abstractmethod
    def process_data(
        self, 
        data: List[int], 
        config: Dict[str, Any]
    ) -> bool:
        pass
```

#### `@generate_abstract_method_docs`
Automatické generování dokumentace pro abstraktní metody.

```python
from abc_helper import ABC, generate_abstract_method_docs

class MyDocumentedClass(ABC):
    @generate_abstract_method_docs()
    @abstractmethod
    def process_item(
        self, 
        item: str, 
        weight: float
    ) -> Dict[str, Any]:
        pass
```

## Příklad komplexního použití

```python
from abc_helper import (
    ABC, AbcSingletonMeta, abc_method, 
    abc_property, log_abstract_method
)

class AbstractDataProcessor(ABC, metaclass=AbcSingletonMeta):
    # Abstraktní property
    data = abc_property("data")
    
    # Abstraktní metoda s logováním
    @log_abstract_method()
    @abstractmethod
    def process(self, input_data: str) -> bool:
        pass
```

## Licence

MIT License

## Autor

[Vaše jméno]

## Verze

0.1.0

## Příspěvky

Příspěvky jsou vítány! Prosím, otevřete issue nebo pull request na GitHubu.


## Popis této dokumentace

Dokumentace obsahuje několik klíčových částí:

1) Úvod - popis knihovny
2) Instalace
3) Hlavní funkce
4) API Reference
   - Popis každé třídy/metody
   - Příklady použití
5) Komplexní příklad
6) Licence
7) Autor
8) Verze
9) Informace o příspěvcích

Doporučení:
- Doplňte vlastní jméno autora
- Přidejte odkaz na GitHub repozitář
- Průběžně aktualizujte verzi knihovny