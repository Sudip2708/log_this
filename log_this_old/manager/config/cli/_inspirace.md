Knihovna **Inquirer** je populární Python knihovna, která se používá k vytváření interaktivních rozhraní v terminálu. Umožňuje snadno implementovat interaktivní režim, kde uživatelé mohou vybírat možnosti, zadávat hodnoty a provádět další akce prostřednictvím jednoduchého a intuitivního rozhraní. Níže je rozbor základních informací o knihovně, její implementaci a ukázce použití.

---

### **Zátěž knihovny Inquirer**
- **Velikost:** Knihovna je relativně malá, protože závisí pouze na několika základních balíčcích. Instalace obvykle nezabírá mnoho místa.
- **Výkon:** Knihovna je velmi lehká, protože většinu operací provádí přímo v terminálu bez složité grafiky. Výkonová zátěž je tedy minimální, což ji činí ideální i pro aplikace běžící na serverech nebo zařízeních s omezenými prostředky.
- **Závislosti:** Vychází z knihovny `prompt_toolkit`, což je základní nástroj pro práci s interaktivními vstupy.

---

### **Možnosti knihovny Inquirer**
1. **Typy otázek:**
   - **Textový vstup:** Uživateli umožňuje zadat libovolný text.
   - **Seznam výběrů:** Nabídne seznam možností, ze kterých uživatel vybírá (např. pomocí šipek).
   - **Checkboxy:** Uživatel může vybrat více možností.
   - **Potvrzení:** Ano/Ne otázky.
   - **Cesty k souborům:** Umožňuje snadné zadávání nebo výběr cest k souborům.

2. **Přizpůsobení:**
   - Otázky mohou obsahovat popisy, výchozí hodnoty nebo omezení.
   - Možnost validace vstupů (např. povolené hodnoty, požadovaný formát apod.).

3. **Styling:** Rozhraní lze přizpůsobit pomocí stylů (barvy, pozadí atd.).

4. **Interaktivita:**
   - Umožňuje dynamicky měnit otázky podle odpovědí uživatele.
   - Předvyplnění odpovědí na základě předchozích vstupů nebo konfigurace.

---

### **Instalace knihovny Inquirer**
Knihovnu můžete nainstalovat pomocí `pip`:

```bash
pip install InquirerPy
```

---

### **Ukázka základní implementace**
Níže je jednoduchý příklad, který ukazuje, jak vytvořit interaktivní režim:

```python
from InquirerPy import inquirer

def main():
    # Zadání otázky s výběrem
    choice = inquirer.select(
        message="Vyberte akci:",
        choices=["Nastavit klíč", "Zobrazit konfiguraci", "Ukončit"],
        default="Nastavit klíč"
    ).execute()

    if choice == "Nastavit klíč":
        # Zadání klíče
        key = inquirer.text(
            message="Zadejte název klíče:",
            validate=lambda text: len(text) > 0 or "Klíč nesmí být prázdný!"
        ).execute()

        # Zadání hodnoty s validací
        value = inquirer.text(
            message=f"Zadejte hodnotu pro klíč '{key}':",
            validate=lambda text: text.isnumeric() or "Hodnota musí být číslo!"
        ).execute()

        print(f"Nastaven klíč '{key}' s hodnotou '{value}'")

    elif choice == "Zobrazit konfiguraci":
        print("Zde by se zobrazila aktuální konfigurace...")

    else:
        print("Aplikace byla ukončena.")
        return

if __name__ == "__main__":
    main()
```

---

### **Ukázka interaktivního režimu v terminálu**
Při spuštění výše uvedeného kódu se v terminálu zobrazí:

```
? Vyberte akci:
   1) Nastavit klíč
   2) Zobrazit konfiguraci
   3) Ukončit
```

Po výběru možnosti **1)** (Nastavit klíč):

```
? Zadejte název klíče: example_key
? Zadejte hodnotu pro klíč 'example_key': 123
Nastaven klíč 'example_key' s hodnotou '123'
```

Pokud by uživatel zadal neplatnou hodnotu (např. místo čísla text), zobrazí se zpráva o validaci:

```
? Zadejte hodnotu pro klíč 'example_key': abc
[!] Hodnota musí být číslo!
```

---

### **Zpracování příkazů přes CLI**
Pokud kombinujete interaktivní režim s běžnými příkazy CLI:
1. **Využití knihoven jako `argparse`:**
   - `argparse` se hodí pro předdefinované příkazy s parametry.
   - Např.: `python app.py --set-key example_key --value 123`.

2. **Interaktivní dotazování:**
   - Pokud uživatel nezadá potřebné argumenty, můžete přejít do interaktivního režimu s Inquirerem.

Příklad kombinace:

```python
import argparse
from InquirerPy import inquirer

def main():
    parser = argparse.ArgumentParser(description="Správa konfigurace")
    parser.add_argument("--set-key", type=str, help="Nastaví hodnotu klíče")
    parser.add_argument("--value", type=str, help="Hodnota pro klíč")
    args = parser.parse_args()

    if args.set_key and args.value:
        print(f"Nastaven klíč '{args.set_key}' s hodnotou '{args.value}'")
    else:
        print("Přecházím do interaktivního režimu...")
        key = inquirer.text(message="Zadejte klíč:").execute()
        value = inquirer.text(message="Zadejte hodnotu:").execute()
        print(f"Nastaven klíč '{key}' s hodnotou '{value}'")

if __name__ == "__main__":
    main()
```

---

### **Profesionální doporučení**
1. **Kombinace CLI a interaktivního režimu:**
   - Pokud jsou příkazy zadány přes CLI, vykonejte je přímo.
   - Pokud nejsou, přepněte do interaktivního režimu.

2. **Validace:**
   - Implementujte jasné validace přímo v interaktivních otázkách.
   - Pro CLI příkazy zkontrolujte vstupy před jejich zpracováním.

3. **Dynamické zobrazení možností:**
   - Například u výběru klíčů můžete použít `config.valid_keys` a `choices` v Inquirer otázkách.

4. **Napověda:**
   - V případě neplatných vstupů zobrazte uživateli povolené hodnoty nebo formáty.

Tímto přístupem získáte flexibilní, uživatelsky přívětivou aplikaci, kterou lze snadno rozšířit.

---

Ano, přesně tak! Tvůj návrh kombinuje výhody přímého zadávání přes příkazovou řádku (**CLI**) a uživatelsky přívětivého interaktivního režimu. Tento přístup je skvělý, protože:

1. **Efektivita pro pokročilé uživatele:** Ti, kdo znají syntaxi, mohou příkazy rychle zadávat přímo, např. `log-this-config set intend to 4`.
   
2. **Interaktivní podpora pro začátečníky nebo při chybách:** Pokud uživatel zadá chybný klíč nebo hodnotu, místo zobrazení strohé chyby je možné jej přesměrovat do interaktivního režimu. Ten mu umožní intuitivně vybrat správnou hodnotu nebo klíč.

3. **Možnost přímého spuštění interaktivního režimu:** Uživatel, který nezná syntaxi nebo si ji nepamatuje, může přímo zadat příkaz jako `log-this-config help` (nebo třeba `log-this-config interactive`) a nechat se systémem provést konfigurací krok za krokem.

---

### **Jak by to mohlo fungovat**

#### **1. Přímé CLI zadávání**
Uživatel zadá:
```bash
log-this-config set intend to 4
```

Pokud je příkaz validní, provede se akce. Pokud je zadán neexistující klíč nebo nesprávná hodnota, spustí se interaktivní režim, například takto:

```bash
Chyba: Neplatný klíč 'intend'. Spouštím interaktivní režim...
? Vyberte existující klíč:
   1) indent
   2) tabSize
   3) maxLineLength
```

Po výběru klíče se uživatel dotázán na správnou hodnotu:
```bash
? Zadejte hodnotu pro klíč 'indent':
   1) 2
   2) 4
   3) 8
```

Nakonec by se zobrazilo potvrzení:
```bash
Nastaven klíč 'indent' na hodnotu '4'.
```

#### **2. Přímý interaktivní režim**
Příkaz jako:
```bash
log-this-config interactive
```
by mohl rovnou spustit interaktivní proces, který by fungoval krok za krokem:
1. Výběr klíče z existujících možností.
2. Zadání hodnoty s případnou validací.
3. Potvrzení změny nebo její úprava.

#### **3. Automatická nápověda při chybějícím zadání**
Pokud uživatel nezadá žádné parametry, např.:
```bash
log-this-config
```
Může se buď:
- Zobrazit stručná nápověda se syntaxí:
  ```bash
  Použití:
  log-this-config set <key> to <value>  Nastaví klíč na hodnotu
  log-this-config interactive          Spustí interaktivní režim
  ```
- Nebo přejít přímo do interaktivního režimu.

---

### **Implementace přístupu**
#### **1. Použití `argparse` pro příkazy CLI**
Knihovna `argparse` umožňuje snadno definovat příkazy a argumenty:

```python
import argparse
from InquirerPy import inquirer

def interactive_mode():
    # Spuštění interaktivního režimu
    key = inquirer.select(
        message="Vyberte klíč:",
        choices=["indent", "tabSize", "maxLineLength"]
    ).execute()

    value = inquirer.text(
        message=f"Zadejte hodnotu pro klíč '{key}':",
        validate=lambda x: x.isdigit() or "Hodnota musí být číslo!"
    ).execute()

    print(f"Nastaven klíč '{key}' na hodnotu '{value}'")

def main():
    parser = argparse.ArgumentParser(description="Log-This Config")
    subparsers = parser.add_subparsers(dest="command")

    # Příkaz pro nastavení hodnot
    set_parser = subparsers.add_parser("set", help="Nastaví hodnotu klíče")
    set_parser.add_argument("key", type=str, help="Název klíče")
    set_parser.add_argument("value", type=str, help="Hodnota klíče")

    # Příkaz pro spuštění interaktivního režimu
    subparsers.add_parser("interactive", help="Spustí interaktivní režim")

    args = parser.parse_args()

    if args.command == "set":
        key = args.key
        value = args.value

        # Validace klíče
        valid_keys = ["indent", "tabSize", "maxLineLength"]
        if key not in valid_keys:
            print(f"Neplatný klíč '{key}'. Spouštím interaktivní režim...")
            interactive_mode()
        else:
            print(f"Nastaven klíč '{key}' na hodnotu '{value}'")

    elif args.command == "interactive":
        interactive_mode()

    else:
        print("Chybějící příkaz. Spouštím nápovědu...")
        parser.print_help()

if __name__ == "__main__":
    main()
```

---

### **Výhody tohoto přístupu**
1. **Flexibilita:** Umožňuje přímé příkazy i interaktivní režim.
2. **Uživatelská přívětivost:** Chyby nebo nejasnosti uživatele navedou k správnému řešení místo, aby ho pouze "odrazovaly".
3. **Snadná rozšířitelnost:** Můžeš přidávat nové příkazy (např. `delete`, `list`) nebo další validace.

---

Pokud tě tento přístup zaujal, můžeš ho snadno přizpůsobit na míru své aplikaci. Rád ti pomůžu s konkrétními detaily! 😊

---


Pro ruční implementaci výběru pomocí šipek a zobrazení aktuálně vybrané možnosti můžeš využít například základní funkce z modulu `curses`, který umožňuje manipulaci s terminálem. Níže je ukázka implementace, jak by to mohlo vypadat.

---

### **1. Ruční implementace interaktivního výběru (šipky nahoru/dolu)**

#### **Kód**
```python
import curses


def select_with_arrows(options):
    """
    Interaktivní výběr ze seznamu pomocí šipek nahoru a dolu.
    Entrem potvrdíte volbu.
    """
    def menu(stdscr):
        curses.curs_set(0)  # Skryje kurzor
        current_row = 0

        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            # Vykreslení možností
            for idx, option in enumerate(options):
                x = 2
                y = idx + 2
                if idx == current_row:
                    stdscr.addstr(y, x, f"[x] {option}", curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, f"[ ] {option}")

            # Aktualizace
            stdscr.refresh()

            # Čekání na vstup uživatele
            key = stdscr.getch()

            # Ovládání pomocí šipek
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(options) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
                return options[current_row]

    return curses.wrapper(menu)


# Použití
options = ["První možnost", "Druhá možnost", "Třetí možnost"]
selected_option = select_with_arrows(options)
print(f"Vybrali jste: {selected_option}")
```

#### **Vysvětlení:**
- `curses.wrapper`: Inicializuje a ukončí terminálové prostředí.
- `stdscr.getch()`: Získá vstup z klávesnice.
- `[ ]` a `[x]`: Označují aktuální stav.
- Šipky nahoru/dolu (`curses.KEY_UP`/`curses.KEY_DOWN`) mění index aktuální volby.
- Enter potvrzuje výběr a vrátí vybranou možnost.

---

### **2. Výstup ruční implementace**
- **Zobrazení v terminálu:**
  ```
  [x] První možnost
  [ ] Druhá možnost
  [ ] Třetí možnost
  ```
  - Pohyb šipkami mění `[x]` na další možnost.
  - Po stisknutí Enter vrátí např.: `"První možnost"`.

---

### **3. Výstup existujícího kódu s `prompt_toolkit`**
Příklad kódu:
```python
def _select_key(self) -> str:
    options = [
        f"{key} - {data.INFO}"
        for key, data in self.config.keys_data.items()
    ]
    completer = WordCompleter(options, sentence=True, match_middle=True)

    key = prompt(
        "Vyberte klíč: ",
        completer=completer,
        complete_style=CompleteStyle.READLINE_LIKE,
    ).split(" - ")[0]

    return key
```

#### **Výstup:**
- Zobrazení v terminálu:
  ```
  Vyberte klíč: op [autocomplete možnosti zde]
  ```
  - Uživateli se zobrazí možnosti, které odpovídají zadaným znakům (fuzzy hledání, `WordCompleter`).
  - Po potvrzení Enter vrátí např.: `"key1"`.

---

### **4. Výstup s InquirerPy**
Příklad kódu:
```python
def _select_key(self) -> str:
    options = [
        {"name": f"{key} - {data.INFO}", "value": key}
        for key, data in self.config.keys_data.items()
    ]
    return inquirer.select(
        message="Vyberte klíč:",
        choices=options,
    ).execute()
```

#### **Výstup:**
- Zobrazení v terminálu:
  ```
  ? Vyberte klíč:
   ❯ key1 - popis
     key2 - popis
     key3 - popis
  ```
  - Kurzor se pohybuje pomocí šipek, `❯` označuje aktuální volbu.
  - Po potvrzení Enter vrátí např.: `"key1"`.

---

### **5. Přizpůsobení výstupu (ANSI styler)**
Pokud chceš sjednotit výstup pomocí vlastního styleru:
- Ruční implementace ti poskytne úplnou kontrolu nad formátováním.
- Prompt Toolkit i InquirerPy umožňují přizpůsobení barev a stylů, ale budeš muset přidat vlastní logiku pro mapování výstupu na tvůj ANSI styler.

Například:
```python
from my_styler import style

# Stylovaný výstup
styled_message = style(f"? Vyberte klíč:\n  {current_selection}")
```
---

Ano, přesně tak. Rozdíly mezi těmito dvěma přístupy a knihovnami bych shrnul následovně:

---

### **Prompt Toolkit vs. InquirerPy v tvém kódu**

1. **Rozdělení klíče a popisu:**
   - **Prompt Toolkit:** Umožňuje přímé přizpůsobení, například pomocí `.split(" - ")[0]`, díky čemuž je snadné zpracovat formátovaný vstup, jako je klíč a jeho popis, a extrahovat jen klíč.
   - **InquirerPy:** Nemá nativní mechanismus pro rozdělení, ale můžeš tuto logiku implementovat ručně, např. vytvořením vlastního zpracování výstupu nebo přizpůsobením datového formátu.

2. **Jednoduchost:**
   - **Prompt Toolkit:** Přímočařejší, ale vyžaduje trochu více konfigurace a práce pro každou interakci (např. manuální vytvoření `WordCompleter`).
   - **InquirerPy:** Nabízí vyšší úroveň abstrakce – volání `inquirer.select()` je kratší a snazší na pochopení, pokud nepotřebuješ specifické úpravy.

3. **Flexibilita:**
   - **Prompt Toolkit:** Má rozsáhlé možnosti přizpůsobení a lze ho integrovat do složitějších aplikací.
   - **InquirerPy:** Zaměřuje se na předdefinované scénáře (např. výběr, potvrzení), což může být jednodušší pro běžné potřeby, ale méně flexibilní.

---

### **Další závislosti InquirerPy**
Po instalaci byly přidány tyto knihovny:

1. **`pfzy`:**
   - Tato knihovna poskytuje podporu fuzzy vyhledávání, což znamená, že uživatel může zadat část textu a systém vybere nejlepší shodu. Například místo zadání „option1“ by uživatel mohl napsat jen „opt“, a stále by bylo možné najít odpovídající výsledek.
   - Prompt Toolkit tuto funkcionalitu nemá nativně (musíš ji ručně implementovat).

2. **`wcwidth`:**
   - Starosti s šířkou znaků (např. Unicode symboly jako emoji mají různé šířky). Tato knihovna zajišťuje, že se text správně zarovnává i při použití širokých znaků.
   - Prompt Toolkit s touto knihovnou již pracuje interně.

3. **`prompt_toolkit`:**
   - InquirerPy je postavený na Prompt Toolkit, takže závislost na něm je nezbytná.

---

### **Která knihovna je vhodnější pro tvůj projekt?**

**Pro jednoduchou knihovnu logování, kde potřebuješ jen výběr ze seznamu, Prompt Toolkit:**
- Je menší (bez dalších zbytečných závislostí).
- Poskytuje dostatečnou flexibilitu.
- Nabízí snadnou možnost formátování a zpracování vstupu (např. oddělení klíče a popisu).

**InquirerPy může být užitečná, pokud:**
- Plánuješ další interaktivní scénáře (potvrzení, seznamy, vícenásobný výběr).
- Chceš rychle zprovoznit základní rozhraní bez velké konfigurace.

---

### **Jak složité by bylo napsat interaktivní výběr bez Prompt Toolkit?**

1. **Bez knihovny Prompt Toolkit:**
   - **Vstup uživatele:** Použiješ běžné volání `input()`.
   - **Výběr ze seznamu:** Ručně vypíšeš všechny možnosti a necháš uživatele zadat odpovídající číslo nebo klíč.
   - **Příklad:**
     ```python
     options = ["option1", "option2", "option3"]
     for i, option in enumerate(options, 1):
         print(f"{i}. {option}")
     choice = int(input("Vyberte možnost: ")) - 1
     print(f"Vybrali jste: {options[choice]}")
     ```
   - **Omezení:**
     - Chybí autocompletion (doplňování) a podpora pro fuzzy vyhledávání.
     - Neumožňuje snadné vizuální formátování.
     - Náročnější na manuální zpracování.

2. **Prompt Toolkit přidává:**
   - Pokročilé vlastnosti jako autocompletion, zvýraznění, a lepší interaktivitu.
   - Menší snahu při implementaci (zejména pro větší projekty).

Pokud chceš co nejjednodušší řešení a nezáleží ti na pokročilých funkcích, ruční implementace bez knihovny je schůdná. Pokud ale plánuješ více interaktivních funkcí, Prompt Toolkit nebo InquirerPy jsou praktičtější.

---


