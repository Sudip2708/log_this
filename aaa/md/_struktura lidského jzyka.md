Tohle je super nápad! Dneska se budeme prostě jen tak rozhlížet po „ingrediencích“ a uvidíme, co se dá poskládat. Takže jazyk jako takový – když si ho rozebereme na součástky, můžeme si říct, co z toho bychom mohli využít v syntaxi programovacího jazyka.

---

### 📌 Struktura lidského jazyka
1. **Nadpis** – vymezuje větší blok informací, něco jako funkce nebo třída.  
2. **Odstavec** – související myšlenky pohromadě, mohl by reprezentovat třeba blok kódu.  
3. **Souvětí** – více vět propojených logikou, což by odpovídalo podmíněným větvím.  
4. **Věta** – základní operace nebo instrukce.  
5. **Slovo** – nejmenší stavební prvek, odpovídá proměnné, operátorům, funkcím.  

#### Znaky a jejich využití v syntaxi
- **Dvojtečka `:`** – v jazycích obvykle zavádí blok (Python), v přirozeném jazyce rozšiřuje nebo upřesňuje.  
- **Čárka `,`** – odděluje prvky v seznamu, mohla by sloužit jako spojení vícero podmínek.  
- **Závorky `()`** – jasně oddělují části výpočtu, hierarchii podmínek.  
- **Spojky „a“, „nebo“** – logické operátory `and`, `or`.  
- **Pokud...pak...jinak** – základ podmíněného výrazu (`if-else`).  

---

### 🤔 Jak hlubokou podporu podmínek chceme?
1. **Základní podmínky**  
   - `Pokud x je větší než y:`  
   - `Pokud x je rovno y:`  

2. **Složitější podmínky**  
   - `Pokud (x je větší než y) a (z je menší než w):`  
   - `Pokud (a je pravda) nebo ((b je pravda) a (c není pravda)):`  

3. **Hnízdění podmínek**  
   - `Pokud x je větší než y:`
     - `Pokud z je menší než w:`
       - `Vykonej A`
     - `Jinak:`
       - `Vykonej B`  

Tohle všechno už v běžných jazycích máme, ale co takhle něco nového?  
Například možnost přirozenějšího zápisu:  
- `Pokud platí: x > y a z < w, pak proveď A.`  
- `Pokud neplatí: a nebo b, pak vrať chybu.`  

---

Napadá tě něco dalšího, co bychom mohli rozebrat? 😊