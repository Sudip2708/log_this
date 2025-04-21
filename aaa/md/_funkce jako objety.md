Ještě jeden takový datas bokem, že mě napadlo. Zda by mělo CINU navrhnout ten systém tak, že by zjednodušil veškeré zadávání tím, že by všechny funkce tvořily jako objekty a na začáku každé funkce by byla definice proměných a pak v kodu by byly tyhle už použitý, tyhle proměné a ještě mě napadlo, jestli by třeba pomohlo, kdyby na místo všech kontejnerů byl jen jeden kontejner, který by vytvářel tabulku a ten by se používal při jednopoložkových tabulkách jako tuple, při dvoupoložkových tabulkách jako slovník atd. Dával by to nějaké ulehčení celkovým úpůlběhu, když by se vlastně sjednotil zápis na to, že všechno je objekt a tím pádem by byla jedna objektová funkce nebo jedno vytváření objektu, ale v různých podobách.
---

Tohle je hodně zajímavá myšlenka, která by mohla **zjednodušit syntaxi** a zároveň **sjednotit datové struktury**. Pojďme ji rozebrat na jednotlivé části.

---

### **🟢 1) Všechny funkce jako objekty**  
Místo klasického zápisu funkcí bychom mohli mít **objekty funkcí**, kde:
- Parametry se definují při vytváření objektu.
- Funkce se spouští metodou `.run()`, `.execute()` nebo `.call()`.
  
**Příklad v Pythonu (jak by mohl vypadat tento koncept):**  
```python
class Function:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body  # Uložený kód funkce

    def run(self, *args):
        local_vars = dict(zip(self.params, args))
        exec(self.body, {}, local_vars)
        return local_vars.get("result")  # Vrátíme, co bylo přiřazeno do 'result'

# Definice funkce:
add_function = Function(
    "Add",
    ["a", "b"],
    """
result = a + b
""")

# Zavolání:
print(add_function.run(5, 3))  # Výstup: 8
```
Takhle by **každá funkce byla objekt**, který si nese své parametry i kód.

---

### **🔵 2) Všechny datové struktury jako jednotný kontejner**  
Místo `list`, `dict`, `set`, `tuple` bychom mohli mít **jediný objekt "Table"**, který by se choval různě podle počtu sloupců:
- **1 sloupec** → jako `list` nebo `tuple`
- **2 sloupce** → jako `dict`
- **3+ sloupců** → jako `DataFrame` nebo relační tabulka  

#### **Jak by to mohlo vypadat?**
```python
class Table:
    def __init__(self, *columns):
        self.columns = columns
        self.data = []

    def add(self, *values):
        self.data.append(values)

    def get(self, key):
        if len(self.columns) == 1:
            return self.data[key]  # Pokud je jen 1 sloupec, chová se jako list
        elif len(self.columns) == 2:
            return dict(self.data).get(key)  # Pokud jsou 2 sloupce, chová se jako slovník
        return self.data  # Jinak vrátíme celou tabulku

# Vytvoření tabulek:
single_column = Table("Numbers")
single_column.add(1)
single_column.add(2)
print(single_column.get(0))  # Výstup: 1

two_columns = Table("Key", "Value")
two_columns.add("name", "Alice")
two_columns.add("age", 25)
print(two_columns.get("name"))  # Výstup: Alice
```
Tím bychom **sjednotili všechny struktury pod jednu univerzální třídu**.

---

### **🟠 Výhody a nevýhody tohoto přístupu**  
✅ **Jednodušší zápis** – všechno jsou objekty.  
✅ **Jeden systém pro data** – `Table` nahrazuje listy, dicty a datové rámce.  
✅ **Lepší struktura kódu** – všechno je objekt a má metody.  

❌ **Výkon** – Python má optimalizované `list`, `dict` apod., zatímco vlastní `Table` by mohla být pomalejší.  
❌ **Musíme přemýšlet jinak** – programátor by se musel naučit nový přístup.  

---

💡 **Otázka na tebe:**  
Přijde ti tenhle koncept intuitivní? Chtěl bys ho otestovat v nějaké miniverzi, třeba jako knihovnu v Pythonu?