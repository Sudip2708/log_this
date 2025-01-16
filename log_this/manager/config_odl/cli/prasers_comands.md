### Odpovědi na otázky a podrobnosti k funkcím a argumentům v `argparse`

---

#### 1) **Mám řešit kontrolu, zda byly argumenty zadány?**
- **Pokud nastavíte `required=True`, nemusíte manuálně kontrolovat, zda byly argumenty zadány.** 
  - `argparse` automaticky ošetří tento scénář: Pokud uživatel nezadá povinný argument, zobrazí chybovou zprávu a ukončí program. 
  - Např. pro `--file` u `export` nebo `import` subparserů se při absenci argumentu zobrazí automatická zpráva:
    ```
    error: the following arguments are required: --file
    ```
- **Validace hodnot však stále zůstává na vás.**  
  Například u argumentu `--key` byste mohli zkontrolovat, zda je to platný klíč ve vaší konfiguraci.

---

#### 2) **Popis hlavních parametrů pro jednotlivé části `argparse`**

Níže uvádím tabulku nejčastěji používaných voleb v různých částech konfigurace parseru.

---

### **1. Hlavní parser (`ArgumentParser`)**

| **Parametr**      | **Význam**                                                                                      | **Příklad**                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| `description`      | Text, který se zobrazí v nápovědě programu.                                                   | `description="Nástroj pro správu konfigurace."`               |
| `epilog`           | Text, který se zobrazí na konci nápovědy.                                                     | `epilog="Děkujeme za použití našeho nástroje!"`               |
| `prog`             | Jméno programu (přepíše název automaticky generovaný).                                        | `prog="log-this-config"`                                      |
| `usage`            | Uživatelská definice způsobu použití (přepíše automatickou nápovědu).                         | `usage="log-this-config <command> [options]"`                 |
| `add_help`         | Pokud je `False`, vypne automatickou nápovědu `-h/--help`.                                     | `add_help=False`                                              |
| `allow_abbrev`     | Povolit automatické zkrácení dlouhých argumentů. Výchozí je `True`.                            | `allow_abbrev=False`                                          |

---

### **2. Subparsery (`add_subparsers`)**

| **Parametr**      | **Význam**                                                                                      | **Příklad**                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| `dest`            | Název atributu, do kterého se uloží zadaný subpříkaz.                                           | `dest="command"`                                              |
| `help`            | Text pro popis dostupných subpříkazů v nápovědě.                                                | `help="Dostupné příkazy"`                                     |
| `required`        | Pokud je `True`, vyžaduje zadání subpříkazu (Python >=3.7).                                     | `required=True`                                               |
| `metavar`         | Zobrazí název místo generického "command" v nápovědě.                                           | `metavar="ACTION"`                                            |

---

### **3. Subparser (`add_parser`)**

| **Parametr**      | **Význam**                                                                                      | **Příklad**                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| `name`            | Jméno subpříkazu, které bude použito při volání programu.                                       | `name="reset"`                                                |
| `help`            | Popis subpříkazu, který se zobrazí v nápovědě.                                                  | `help="Resetuje konfiguraci."`                                |
| `description`     | Detailnější popis příkazu, který se zobrazí v nápovědě pro tento subparser.                     | `description="Resetuje veškerou konfiguraci do výchozího stavu."` |
| `epilog`          | Text, který se zobrazí na konci nápovědy subparseru.                                            | `epilog="Tento příkaz nenávratně odstraní všechny změny."`    |
| `aliases`         | Seznam alternativních názvů pro subpříkaz.                                                      | `aliases=["restore"]`                                         |
| `add_help`        | Pokud je `False`, vypne automatickou nápovědu `-h/--help` pro tento subparser.                  | `add_help=False`                                              |

---

### **4. Argumenty (`add_argument`)**

| **Parametr**         | **Význam**                                                                                      | **Příklad**                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| `name_or_flags`       | Jméno argumentu (krátké/dlouhé).                                                               | `"--file"` nebo `"-f"`                                        |
| `help`               | Popis argumentu, který se zobrazí v nápovědě.                                                  | `help="Cesta k souboru."`                                     |
| `required`           | Pokud je `True`, argument musí být zadán.                                                      | `required=True`                                               |
| `default`            | Výchozí hodnota argumentu, pokud není zadán.                                                   | `default="config.json"`                                       |
| `choices`            | Omezuje možné hodnoty na seznam/iterovatelný objekt.                                           | `choices=["json", "yaml"]`                                    |
| `type`               | Typ hodnoty argumentu (automaticky zkontrolováno).                                             | `type=int` nebo `type=str`                                    |
| `nargs`              | Počet očekávaných hodnot: číslo, `*` (libovolné), `+` (alespoň jedna), nebo `?` (volitelný).    | `nargs="*"`                                                   |
| `metavar`            | Zobrazí vlastní jméno argumentu místo generického `[FILE]`.                                    | `metavar="PATH"`                                              |
| `dest`               | Jméno atributu, pod kterým bude hodnota uložena do `args`.                                     | `dest="output_path"`                                          |
| `action`             | Specifikuje způsob zpracování argumentu, např. `store`, `store_true`, `append`, atd.            | `action="store_true"`                                         |

---

#### 3) **Doporučené použití:**

- **`description` a `help`:** Vždy uveďte, protože jsou užitečné pro uživatele.
- **`required`:** Používejte pouze pro argumenty, které jsou nezbytné.
- **`type`:** Pokud pracujete s čísly, daty nebo jinými specifickými typy, vždy nastavte.
- **`choices`:** Pokud argument přijímá omezené množství hodnot, použijte `choices`.

Pokud máte složitější požadavky, jako například vzájemnou exkluzivitu argumentů nebo povolení více formátů, můžete použít další funkce `argparse`, jako jsou `add_mutually_exclusive_group`. 😊

---

Tohle jsou detailní otázky, pojďme si na ně odpovědět systematicky:

---

### 1. **Hlavní parser (`ArgumentParser`)**

**`prog`:**  
- **Co dělá?** Tento parametr přepíše automaticky generovaný název programu, který se obvykle odvozuje z názvu skriptu, jímž je CLI voláno. Například pokud spustíte skript `python myscript.py`, implicitní název bude `myscript.py`. Pomocí `prog` jej můžete změnit na něco čitelnějšího, třeba `log-this-config`.
- **Použití:** Tato změna se projeví zejména v nápovědě, kde se bude zobrazovat zadaný název místo výchozího.
- **Vhodné pro:** Když chcete uživateli nabídnout přehlednější jméno programu, než je název souboru.

---

### 2. **Subparsery (`add_subparsers`)**

**`required`:**  
- **Co dělá?** Určuje, zda je zadání jednoho z příkazů povinné. Pokud je `required=True`, uživatel **musí** zadat některý ze subpříkazů, jinak se zobrazí chyba. Bez této volby je možné zavolat hlavní program bez příkazů, což obvykle zobrazí hlavní nápovědu.
- **Použití:** Pro povinné příkazy, pokud nemá hlavní program jinou výchozí akci než zobrazit nápovědu.

**`metavar`:**  
- **Co dělá?** Ovlivňuje, jak se název subpříkazů zobrazí v nápovědě. Standardně jsou vypsány jako seznam, ale s `metavar` je můžete zjednodušit na zadaný text (například `commands` místo výčtu všech příkazů).
- **Použití:** Pro zkrácení nebo vizuální zlepšení nápovědy.

---

### 3. **Subparser (`add_parser`)**

**`help`, `description`, `epilog`:**  
- **`help`:** Krátký popis subpříkazu zobrazený v seznamu příkazů.  
- **`description`:** Delší popis zobrazený na začátku nápovědy konkrétního subpříkazu.  
- **`epilog`:** Text zobrazený na konci nápovědy subpříkazu (například poznámky nebo příklady použití).
- **Smysl:** Tyto tři části umožňují strukturovat nápovědu tak, aby byla přehledná a logicky rozdělená.

**`aliases`:**  
- **Co dělá?** Umožňuje definovat alternativní názvy příkazu. Například `aliases=["r"]` by umožnilo spustit příkaz `reset` i jako `r`.
- **Použití:** Pokud chcete podpořit rychlé psaní nebo konzistenci se zvyklostmi uživatelů.
- **Smysl zkratek:** Zkrácené zadávání je běžné a doporučené, pokud zlepší použitelnost. Pro delší příkazy nebo argumenty je standardem nabídnout kratší varianty, například:
  - Dlouhý příkaz: `export`
  - Zkratka: `e`
  - Dlouhý argument: `--file`
  - Zkratka: `-f`
  Zkracuje se obvykle na jedno písmeno, ale lze použít i více. Standardy neexistují, ale důležité je, aby zkratky byly snadno zapamatovatelné a konzistentní.

---

### 4. **Argumenty (`add_argument`)**

**`name_or_flags`:**  
- Pro použití obou variant zadejte:  
  ```python
  parser.add_argument("--file", "-f", required=True, help="Cesta k souboru.")
  ```

**`default`:**  
- **Smysl:** Nastavit výchozí hodnotu argumentu, pokud uživatel nic nezadá. Například u `--file` by bylo možné nastavit výchozí cestu na plochu.  
- **Praktická doporučení:** Výchozí hodnoty jsou vhodné, pokud existuje logická volba, kterou lze použít bez explicitního zadání uživatelem. U importu/exportu bych ale raději vyžadoval zadání cesty (bez `default`), protože uživatel obvykle chce kontrolovat, kam soubor uložit.

**`choices` a `type`:**  
- **`choices`:** Omezuje povolené hodnoty. Například pro klíče konfigurace:  
  ```python
  parser.add_argument("--key", choices=["log_level", "output_format"], help="Klíč konfigurace.")
  ```
- **`type`:** Určuje datový typ. Například pro číselné hodnoty:
  ```python
  parser.add_argument("--value", type=int, help="Hodnota.")
  ```
- **Použití:** Obě volby lze kombinovat, pokud má smysl omezit hodnoty i určit jejich typ. Validace nad rámec těchto voleb (např. podle klíče různé typy hodnot) je lepší provádět při zpracování argumentů, ne přímo v parseru.

**`nargs`:**  
- **Co dělá?** Určuje, kolik hodnot může argument přijmout.  
  - `1`: Jedna hodnota.  
  - `*`: Libovolný počet hodnot.  
  - `+`: Jeden nebo více.  
  - `?`: Nula nebo jedna.  
- **Použití:** Pokud má smysl, aby uživatel zadal více hodnot (například seznam klíčů), nastavte `nargs="+"`. Pro běžné případy ale stačí výchozí hodnota (`1`).

**`metavar`, `dest`, `action`:**  
- **`metavar`:** Zobrazuje vlastní název v nápovědě místo výchozího jména.  
  ```python
  parser.add_argument("--file", metavar="FILEPATH", help="Cesta k souboru.")
  ```
- **`dest`:** Určuje jméno, pod kterým bude hodnota argumentu dostupná v `args`. Obvykle není potřeba měnit.  
- **`action`:** Určuje speciální chování. Například `store_true` pro logické přepínače:
  ```python
  parser.add_argument("--verbose", action="store_true", help="Zapne podrobné výpisy.")
  ```

---

### 5. **Knihovna `argparse`**

`argparse` je součástí standardní knihovny Pythonu, což znamená, že není potřeba ji instalovat zvlášť. Je nejpoužívanější pro základní správu CLI, ale existují i alternativy jako `click` nebo `typer`, které nabízejí pohodlnější API pro složitější CLI aplikace.

---

Rád ti na vše odpovím podrobně! 😊

### 1) **Parametr `name_or_flags`**
Ano, chápeš to v zásadě správně:

- **Pro `add_argument`:** Parametr `name_or_flags` umožňuje zadat více variant jmen nebo zkratek pro stejný argument. Například:
  ```python
  parser.add_argument("--file", "-f", help="Cesta k souboru.")
  ```
  Tento argument umožní volání:
  ```bash
  script.py --file cesta/k/souboru
  script.py -f cesta/k/souboru
  ```
  Tato varianta je velmi užitečná pro uživatelskou přívětivost.

- **Pro `add_parser`:** Parametr `name` slouží k pojmenování subpříkazu a podporuje pouze jednu hodnotu, která je povinná. Pro dodatečné varianty názvů (aliasy) se používá parametr `aliases`. 
  ```python
  subparsers = parser.add_subparsers()
  export_parser = subparsers.add_parser("export", aliases=["e"], help="Export dat.")
  ```
  To umožní volat:
  ```bash
  script.py export
  script.py e
  ```

- **Rozdíl:** V `add_argument` se varianta zkratek zadává přímo (`--flag`, `-f`), zatímco `add_parser` k tomu využívá `aliases`.

### 2) **Parametry `choices` a `type`**
- **Výchozí hodnoty:** Pokud nejsou zadány, `choices` ani `type` nemají výchozí hodnotu. Bez specifikace:
  - `choices` neomezuje vstup.
  - `type` je ve výchozím stavu `str` (řetězec).

- **Použití `choices` s klíči:**
  Pokud máš 10 klíčů v konfiguraci, určitě je dobré je použít v `choices`. Například:
  ```python
  parser.add_argument("key", choices=list(config.DEFAULTS.keys()), help="Nastavení klíče.")
  ```
  Výhoda:
  - Automatická validace uživatelem zadaného klíče.
  - Klíče se zobrazí v nápovědě.

  Pokud uživatel může zobrazit klíče pomocí příkazu `show`, záleží na tobě, jestli chceš mít redundantní způsoby (např. dynamické generování `choices` je přesto elegantní).

### 3) **Parametr `metavar`**
- **Výchozí hodnota v nápovědě:** Argumenty používají automaticky své `name_or_flags`. Například:
  ```python
  parser.add_argument("--file", "-f", help="Cesta k souboru.")
  ```
  Výstup nápovědy bude:
  ```bash
  --file FILE, -f FILE   Cesta k souboru.
  ```
  Kde `FILE` je výchozí hodnota (dle názvu argumentu).

- **Použití `metavar`:** Pokud chceš zobrazit jiný popisek, použij `metavar`:
  ```python
  parser.add_argument("--file", "-f", metavar="SOUBOR", help="Cesta k souboru.")
  ```
  Výstup nápovědy:
  ```bash
  --file SOUBOR, -f SOUBOR   Cesta k souboru.
  ```

Použití `metavar` je tedy užitečné, pokud výchozí názvy nejsou dostatečně popisné.

### 4) **Parametr `action`**
- **Funkce `action`:** Tento parametr ovlivňuje, co se má stát, když je argument použit. Má hlubší kontext a může spouštět specifické akce. Například:
  - `store`: Výchozí akce, která uloží hodnotu argumentu.
  - `store_true` / `store_false`: Nastaví hodnotu na `True` / `False`, pokud je argument přítomen.
  - `append`: Přidá hodnoty do seznamu.
  - Vlastní akce: Můžeš definovat vlastní třídu pro specifické chování.

- **Příklad s exportem:**
  Můžeš vytvořit vlastní akci, která otevře okno pro výběr cesty:
  ```python
  class OpenFileDialog(argparse.Action):
      def __call__(self, parser, namespace, values, option_string=None):
          import tkinter as tk
          from tkinter import filedialog

          root = tk.Tk()
          root.withdraw()  # Skryje hlavní okno
          file_path = filedialog.asksaveasfilename(initialfile=values)
          setattr(namespace, self.dest, file_path)

  parser.add_argument("--file", "-f", action=OpenFileDialog, help="Vyberte cestu k uložení.")
  ```

- **Platformní omezení:** Tento přístup je přátelský, ale nemusí být vždy konzistentní mezi systémy. Pokud chceš konzistenci, je lepší držet se textového zadávání cesty.

---

Pokud máš další dotazy, sem s nimi! 😊

