"""
Samostatný validátor pro Generic[T1, T2, ...] není potřeba,
protože Generic slouží pouze jako základní třída pro tvorbu generických typů
a nepoužívá se přímo jako anotace hodnot.

Příklad:
    class Stack(Generic[T]):
        ...

    Správný typ pro anotaci hodnoty je pak:
        Stack[int], nikoliv Generic[int]

Při instancování generické třídy (např. Stack[int]) se typová informace
z Generic přesune do konkrétní třídy. Validace je tedy zajištěna
validátorem dané konkrétní třídy, nikoliv Generic samotným.

Z tohoto důvodu není potřeba vlastní validátor pro Generic.
"""
