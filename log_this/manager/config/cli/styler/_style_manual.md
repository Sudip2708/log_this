# Předefinované třídy v prompt_toolkit

## Základní UI komponenty

| Třída | Popis | Běžné použití |
|-------|-------|---------------|
| `dialog` | Základní styl pro dialogová okna | Celkový vzhled dialogu |
| `dialog.body` | Tělo dialogového okna | Hlavní obsah dialogu |
| `dialog.border` | Okraje dialogového okna | Rámeček dialogu |
| `dialog.title` | Titulek dialogu | Nadpis v horní části |
| `dialog.footer` | Patička dialogu | Spodní část dialogu |
| `dialog.shadow` | Stín dialogu | Vizuální efekt stínu |

## Interaktivní prvky

| Třída | Popis | Běžné použití |
|-------|-------|---------------|
| `button` | Základní styl tlačítka | Neaktivní tlačítko |
| `button.focused` | Aktivní tlačítko | Tlačítko s fokusem |
| `selected` | Vybraná položka | Aktuálně vybraná položka v seznamu |
| `selected.focused` | Vybraná položka s fokusem | Aktivně vybraná položka |
| `checkbox` | Zaškrtávací pole | Základní vzhled checkboxu |
| `checkbox.checked` | Zaškrtnutý checkbox | Aktivní checkbox |
| `radiolist` | Seznam s možností výběru | Základní vzhled radio seznamu |
| `search` | Vyhledávací pole | Vstupní pole pro vyhledávání |
| `search.current` | Aktuální výsledek vyhledávání | Zvýraznění aktuálního nálezu |

## Menu a seznamy

| Třída | Popis | Běžné použití |
|-------|-------|---------------|
| `menu-bar` | Hlavní menu | Horní lišta s menu |
| `menu` | Položka menu | Jednotlivé položky v menu |
| `menu.border` | Okraj rozbalovacího menu | Rámeček menu |
| `completion-menu` | Menu pro automatické doplňování | Seznam návrhů |
| `completion-menu.completion` | Položka v menu doplňování | Jednotlivé návrhy |
| `completion-menu.completion.current` | Aktuální položka | Vybraný návrh |

## Textové editory

| Třída | Popis | Běžné použití |
|-------|-------|---------------|
| `prompt` | Základní prompt | Výzva k zadání |
| `prompt.arg.text` | Text argumentu | Zvýraznění argumentů |
| `prompt.completions` | Seznam doplnění | Nabídka doplnění |
| `prompt.cursor` | Kurzor | Pozice kurzoru |
| `prompt.search` | Vyhledávací prompt | Pole pro vyhledávání |

# Předdefinované barvy a kódy

## Základní barvy

| Název | Hex kód | Použití ve stylu |
|-------|----------|-----------------|
| `black` | `#000000` | `fg:#000000` nebo `bg:#000000` |
| `red` | `#ff0000` | `fg:#ff0000` nebo `bg:#ff0000` |
| `green` | `#00ff00` | `fg:#00ff00` nebo `bg:#00ff00` |
| `yellow` | `#ffff00` | `fg:#ffff00` nebo `bg:#ffff00` |
| `blue` | `#0000ff` | `fg:#0000ff` nebo `bg:#0000ff` |
| `magenta` | `#ff00ff` | `fg:#ff00ff` nebo `bg:#ff00ff` |
| `cyan` | `#00ffff` | `fg:#00ffff` nebo `bg:#00ffff` |
| `white` | `#ffffff` | `fg:#ffffff` nebo `bg:#ffffff` |

## Šedé odstíny

| Název | Hex kód | Použití ve stylu |
|-------|----------|-----------------|
| `gray` | `#808080` | `fg:#808080` nebo `bg:#808080` |
| `brightblack` | `#404040` | `fg:#404040` nebo `bg:#404040` |
| `darkgray` | `#a9a9a9` | `fg:#a9a9a9` nebo `bg:#a9a9a9` |
| `lightgray` | `#d3d3d3` | `fg:#d3d3d3` nebo `bg:#d3d3d3` |

## Formátovací vlastnosti

| Vlastnost | Popis | Příklad použití |
|-----------|-------|-----------------|
| `bold` | Tučné písmo | `bold` |
| `italic` | Kurzíva | `italic` |
| `underline` | Podtržení | `underline` |
| `reverse` | Prohození barev pozadí a popředí | `reverse` |
| `hidden` | Skrytý text | `hidden` |

## Příklady kombinací

```python
style = Style.from_dict({
    # Základní kombinace
    'warning': 'fg:#ffff00 bg:#000000 bold',  # Žlutý text na černém pozadí, tučně
    'error': 'fg:#ff0000 italic',  # Červený text kurzívou
    'success': 'fg:#00ff00 underline',  # Zelený podtržený text
    
    # Komplexní kombinace
    'special': 'fg:#ff00ff bg:#ffffff bold italic',  # Růžový tučný text kurzívou na bílém pozadí
    'highlight': 'fg:#ffffff bg:#0000ff reverse',  # Prohození modré a bílé
})
```

## Tipy pro používání

1. Barvy lze definovat pomocí:
   - Hex kódů: `#ff0000`
   - ANSI názvů: `red`, `blue`
   - RGB hodnot: `rgb(255,0,0)`

2. Každá třída může kombinovat:
   - Barvu popředí (`fg`)
   - Barvu pozadí (`bg`)
   - Formátovací vlastnosti

3. Při definici vlastních tříd je dobré držet se konvence:
   - Používat tečkovou notaci pro hierarchii (`dialog.body`)
   - Používat popisné názvy (`warning`, `error`)
   - Dodržovat konzistenci napříč aplikací

---

# ANSI barvy v Python prompt_toolkit

## Dostupné ANSI barvy

### Základní barvy
- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`

### Světlé varianty
- `brightblack`
- `brightred`
- `brightgreen`
- `brightyellow`
- `brightblue`
- `brightmagenta`
- `brightcyan`
- `brightwhite`

## Příklad komplexního použití

```python
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

# Definice stylů
style = Style.from_dict({
    'info': 'fg:green',
    'warning': 'fg:yellow bold',
    'error': 'fg:red bold italic',
    'help': 'fg:cyan underline'
})

# Stylovaný výstup
def print_styled(message, style_type):
    # Použití HTML-like syntaxe
    print_formatted_text(
        HTML(f'<{style_type}>{message}</{style_type}>'), 
        style=style
    )

# Příklady použití
print_styled("Informační zpráva", "info")
print_styled("Varování!", "warning")
print_styled("Kritická chyba!", "error")
print_styled("Nápověda", "help")
```

## Alternativa pro klasické CLI

```python
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text

# Pro běžné CLI výstupy
def cli_print(message, style_type):
    # Použití FormattedText pro flexibilnější formátování
    formatted_text = FormattedText([
        (f'class:{style_type}', message)
    ])
    print_formatted_text(formatted_text, style=style)
```

## Stylovací vlastnosti
- `bold`
- `italic`
- `underline`
- `reverse`
- `blink`
- `hidden`

## Tipy
- Kombinujte barvy a stylovací vlastnosti
- Používejte sémantické názvy tříd
- Pro konzistenci definujte styly centrálně