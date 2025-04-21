**Pokyny pro úpravu kódu knihovny**

**Cíl projektu:**  
Knihovna pro začínající programátory, která umožňuje jednoduché logování pomocí dekorátoru `@log_this(mode)`, aniž by se museli učit syntax loggeru.

**Aktuální fáze:**  
Knihovna je již funkčně hotová. Momentálně probíhá úprava kódu do profesionální podoby. Prioritou jsou:
- Docstringy
- Typové anotace
- Struktura importů
- Další drobné úpravy pro čitelnost a kvalitu kódu

**Co neřešíme nyní:**  
- Překlad do angličtiny (zatím vše v češtině)
- Testování (bude řešeno později)

**Konkrétní úpravy:**  
1. **Docstringy**
   - Každá veřejná funkce a třída musí mít jasný a stručný docstring.
   - Používáme formát Google docstring.
   - Popisujeme parametry a návratovou hodnotu.

2. **Typové anotace**
   - Přidat správné typové anotace pro všechny funkce a metody.
   - Pokud se vrací `None`, explicitně uvést `-> None`.
   - Pokud je parametr volitelný, použít `Optional`.

3. **Importy**
   - Seřadit importy abecedně.
   - Struktura importů:
     1. Standardní knihovny
     2. Externí knihovny (např. `prompt_toolkit`)
     3. Interní moduly projektu
     
     Mezi těmito sekcemi musí být prázdný řádek.

4. **Kvalita kódu**
   - Dodržovat PEP 8.
   - Udržovat jasnou a čitelnou strukturu kódu.
   - Rozdělovat dlouhé řádky podle pravidel PEP 8.
   
Tento text mi můžeš kdykoli znovu poslat v dalším vlákně a já podle něj budu pokračovat konzistentně. 😊

