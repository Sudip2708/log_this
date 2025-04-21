# Třídy a metody z nativní ABC knihovny
from abc import ABC, ABCMeta, abstractmethod

# Přidané metody pro snadnější použití
from .abc_singleton_meta import AbcSingletonMeta
from .abc_method import abc_method
from .abc_property import abc_property

# Bonusové metody
from .bonus import (
    AbcAbstractBuilder,
    abc_type_validator,
    abc_log,
    abc_doc_generator
)

__all__ = [

    # Třídy a metody z nativní ABC knihovny
    'ABC',
    'ABCMeta',
    'abstractmethod',

    # Přidané metody pro snadnější použití
    'AbcSingletonMeta',
    'abc_method',
    'abc_property',

    # Bonusové metody
    'AbcAbstractBuilder',
    'abc_log',
    'abc_type_validator',
    'abc_doc_generator',
]

# Dokumentace:
"""
# Vlastnosti knihovny:
• Řeší nejčastější potřeby práce s ABC
• Udržuje nízkou komplexitu

# Základní metody
Metoda abc_property() a abc_method():
• Výrazně zkracují zápis
• Zachovávají funkcionalitu původního zápisu
• Zachovávají typovou kontrolu
• Jsou čitelné a intuitivní

Singleton meta třída:
• Thread-safe implementace
• Možnost smazání instance pro testování
• Zachování kompatibility s ABC

# Rozšíření v této verzi:
abc_method():
• Podpora pro definici návratového typu
• Zachování typových anotací

abc_property():
• Lepší error handling
• Možnost specifikace typu property

# Noně přidáno
AbcAbstractBuilder:
• Generický abstraktní builder jako bonus
• Rozšiřuje možnosti práce s abstraktními třídami
- Poskytuje generický rámec pro postupnou, řízenou konstrukci objektů
- Umožňuje krokovat proces vytváření komplexních objektů
- Odděluje konstrukční logiku od reprezentace objektu
Výhody:
- Flexibilita: Umožňuje postupnou, podmíněnou tvorbu objektů
- Čitelnost: Kód je srozumitelnější a lépe strukturovaný
- Oddělení zodpovědností: Konstrukční logika je oddělena od samotného objektu
- Znovupoužitelnost: Lze snadno rozšiřovat a modifikovat
- Podpora imutability: Umožňuje vytvářet nezměnitelné objekty
Případy použití:
- Komplexní objekty s mnoha volitelnými parametry
- Konfigurace objektů s proměnlivou strukturou
- Tvorba konfiguračních nástrojů
- Testování a mockování objektů

abc_log (Logging Decorator):
• Umožňuje sledovat volání abstraktních metod
• Konfigurovatelné úrovně logování
• Pomáhá při ladění a identifikaci chybějících implementací
- Dekorátor pro přidání logování abstraktním metodám.
Výhody:
- Automatické logování volání abstraktních metod
- Konfigurovatelná úroveň logování
- Sledování průběhu volání metod před jejich implementací
Příklady použití:
- Ladění: Sledování volání ještě neimplementovaných metod
- Audit: Záznam pokusů o volání abstraktních metod
- Diagnostika: Identifikace míst, kde chybí implementace
    
abc_type_validator (Type Validation):
• Provádí pokročilou typovou kontrolu v runtime
• Podpora složitých typů (generics, union, optional)
• Zvyšuje bezpečnost a spolehlivost kódu
- Dekorátor pro rozšířenou typovou kontrolu abstraktních metod.
Výhody:
- Statická typová kontrola před voláním metody
- Detailní validace vstupních parametrů
- Podpora složitých typů (generics, union, optional)
Použití:
- Zvýšení bezpečnosti typů v runtime
- Včasná detekce nesprávných typů
- Podpora komplexnějších typových kontrol

abc_doc_generator (Documentation Generator):
• Automaticky generuje konzistentní dokumentaci
• Extrahuje informace přímo z typových anotací
• Usnadňuje tvorbu dokumentace pro abstraktní metody
- Dekorátor pro automatické generování dokumentace abstraktních metod.
Výhody:
- Automatické generování konzistentní dokumentace
- Extrakce informací přímo z typových anotací
- Jednotný formát dokumentace pro abstraktní metody
Použití:
- Udržování konzistentní dokumentace
- Automatické generování podkladů pro API dokumentaci
- Usnadnění tvorby dokumentace

# Poznámky:
- Pro použití dokumentačního generátoru je doporučena instalace docformatter
- Jednotlivé utility lze kombinovat
- Implementace jsou navrženy s ohledem na flexibilitu a rozšířitelnost


# Potřeba dokončit:
• Vytvořit setup.py pro snadnou instalaci
• Přidat kompletní testy
• Připravit dokumentaci
• Publikovat na PyPI
"""