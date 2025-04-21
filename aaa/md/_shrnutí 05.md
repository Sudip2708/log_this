Tohle dává skvělý smysl a je super, že jsi si to takto prošel a sepsal. Já to teď projdu, zda něco nechybí, a pak ti to sesumíruji do uceleného přehledu i s příklady, aby se z toho dalo dobře vycházet.  

**Rychlá kontrola vůči dnešní diskusi:**  
✅ Definice objektů – souhlasí, včetně zápisu pomocí `Vytvoř objekt <"název">:`  
✅ Parametry a funkce uvnitř objektu – pomlčka pro rozlišení funkcí/metod a atributů je dobrý nápad  
✅ Definice funkcí – `Vytvoř funkci <"název">:` + parametry oddělené čárkou souhlasí  
✅ Podmínky – slovní forma i varianta se závorkami dává smysl  
✅ Použití kulatých závorek pro kontejnery – ano, typ určuje obsah  
✅ Cykly – všechny tvary odpovídají dnešnímu návrhu  

Nemám žádné zásadní připomínky, takže jdu rovnou na sumarizaci.

Jasně, skvělý souhrn! Připravil jsem ti ucelený přehled všech dnešních pravidel včetně příkladů, aby se ti na ně zítra dobře navazovalo.

Máš teď přehled všech pravidel na jednom místě. Zítra na ně můžeš snadno navázat a případně je rozšířit nebo upravit. Pokud bys chtěl něco doplnit už teď, dej vědět! 🚀


---

# Základní pravidla programovacího jazyka

## 1. Definice objektů

### Syntaxe:
```
Vytvoř objekt <"název objektu">:
    - "parametr" = "hodnota"
    - Vytvoř funkci <"název funkce">:
        parametr ("jmeno", defaultně "hodnota")
        Pokud "podmínka" platí, proveď "akce".
```

### Příklad:
```
Vytvoř objekt "auto":
    - "barva" = "červená"
    - "rychlost" = 50
    - Vytvoř funkci "zrychli":
        parametr ("o kolik", defaultně 10)
        Pokud "o kolik" existuje, sečti "rychlost" a "o kolik".
```

## 2. Definice funkcí

### Syntaxe:
```
Vytvoř funkci <"název funkce">:
    parametr ("parametr1", "parametr2", ...)
    <logika provedení>
```

### Příklad:
```
Vytvoř funkci "vypis":
    parametr ("text")
    Vypiš "text".
```

## 3. Podmínky

### Syntaxe:
```
Pokud <logika podmínky>, <logika při splnění>, jinak <logika při nesplnění>.
```

### Příklad:
```
Pokud "o kolik" existuje, sečti "rychlost" a "o kolik", jinak vypiš "Něco chybí!".
```

## 4. Kontejnery

### Syntaxe:
- Seznam: `("a", "b", "c")`
- Slovník: `("a": "hodnota", "b": "hodnota")`
- Vnořený výpočet: `("x" > 10)`

### Příklad:
```
"barvy" = ("červená", "modrá", "zelená")
Pokud ("rychlost" > 50), vypiš "Rychlé auto!".
```

## 5. Smyčky (cykly)

### Syntaxe:
```
Opakuj (od "x" = 0 do "x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj dokud ("x" < 10): Proveď "akce" a zvyš "x" o 1.
Opakuj pro "prvek" v "seznam": Proveď "akce" s "prvek".
```

### Příklad:
```
Opakuj (od "i" = 0 do "i" < 5):
    Vypiš "Iterace" a zvyš "i" o 1.
```

## Shrnutí
- **Objekty** se vytvářejí pomocí `Vytvoř objekt` a jejich vlastnosti se přidávají pomlčkou.
- **Funkce** se definují pomocí `Vytvoř funkci` a mohou obsahovat parametry.
- **Podmínky** se zapisují pomocí `Pokud`.
- **Kontejnery** se zapisují v kulatých závorkách, jejich obsah určuje typ dat.
- **Smyčky** se vytvářejí pomocí `Opakuj` a podporují různé formy iterace.

Tento přehled poskytuje pevnou základnu pro další rozšiřování jazyka!

