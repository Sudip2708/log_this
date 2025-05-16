from typing import TypeVar

T = TypeVar("T")  # Typ
T1 = TypeVar("T1")  # Typ 1
T2 = TypeVar("T2")  # Typ 2
T3 = TypeVar("T3")  # Typ 3
K = TypeVar("K")  # Klíč
V = TypeVar("V")  # Hodnota
Y = TypeVar("Y")  # Yieldovaný typ
S = TypeVar("S")  # send
R = TypeVar("R")  # Návratová hodnota
P = TypeVar("P")  # ParamSpec
E = TypeVar('E', bound=Exception)  # Pro definice výjimek (exception: E)
