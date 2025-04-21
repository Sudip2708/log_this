Výborná otázka! Jde o důležitý koncept při zpracování výjimek v Pythonu.

### Srovnání `sys.exit()` vs `raise`

**`sys.exit()`**:
- Okamžitě ukončí běh celého programu
- Výstupní kód (např. `sys.exit(1)`) signalizuje operačnímu systému, že program skončil chybou
- Žádný další kód po tomto volání se již neprovede
- Nepropaguje výjimku dále v call stacku

**`raise`**:
- Propaguje výjimku nahoru v call stacku
- Umožňuje dalším `try`/`except` blokům v hierarchii volání tuto výjimku zachytit
- Program pokračuje v běhu, pokud je výjimka někde zachycena
- Zachovává celý traceback výjimky

### Kdy použít který přístup?

**Použij `sys.exit()`, když:**
- Chceš zastavit celý program při kritické chybě
- Potřebuješ vlastní formátování výstupu chyby a nechceš, aby se zobrazil standardní traceback
- Jde o skripty nebo aplikace s příkazovým rozhraním, kde má smysl návratová hodnota
- Nechceš, aby výjimka "probublala" nahoru a byla zachycena jinými bloky `try`/`except`

**Použij `raise`, když:**
- Chceš, aby výjimka mohla být zpracována na vyšších úrovních call stacku
- Implementuješ knihovnu nebo komponentu, která by neměla rozhodovat o ukončení celé aplikace
- Chceš zachovat původní traceback pro lepší diagnostiku
- Používáš výjimky jako součást logiky aplikace

### Typické vzory použití

**Ukončení aplikace:**
```python
try:
    # Kritická operace
except CriticalError:
    # Logování nebo výpis vlastního formátu chyby
    print("Kritická chyba: aplikace bude ukončena")
    sys.exit(1)
```

**Propagace výjimky pro vyšší zpracování:**
```python
try:
    # Operace
except Exception as e:
    # Možné logování nebo přidání kontextu
    raise  # nebo raise upravená_výjimka 
```

### K tvé situaci

To, co děláš - zachycení výjimky, vlastní formátování výstupu a pak ukončení programu - je naprosto legitimní přístup, zvláště pro:

1. Skripty a nástroje (na rozdíl od knihoven)
2. Situace, kde chceš mít plnou kontrolu nad formátem výstupu chyb
3. Případy, kdy nechceš, aby výjimky "probublávaly" přes mnoho úrovní

V knihovnách se obvykle vyhýbáme používání `sys.exit()`, protože by to zabránilo aplikacím, které knihovnu používají, aby zpracovaly výjimku vlastním způsobem. V aplikacích a skriptech je to však běžný a užitečný přístup.

### Závěr

Tvůj přístup s `sys.exit()` po zachycení a zpracování výjimky je správný způsob, jak zajistit konzistentní a čitelný výstup chyb, zejména pokud:
- Máš komplexní aplikaci s mnoha vrstvami
- Chceš standardizovat formát chybových hlášení
- Nechceš mít mnohonásobné výstupy ze zanořených `try`/`except` bloků

Je to jeden z běžných vzorů v Pythonu pro práci s chybami v aplikacích, zvláště v nástrojích příkazové řádky nebo skriptech.