### **3️⃣ Návrh ladicích nástrojů (debugging)**  

Každý programovací jazyk potřebuje **dobrý ladicí systém**, aby bylo možné snadno sledovat, co se děje během běhu kódu. Návrh ladicích nástrojů bude obsahovat:  
✔ **Ladicí výpisy (`debug`)**  
✔ **Interaktivní sledování proměnných**  
✔ **Krokování kódu (`step-by-step`)**  
✔ **Zachytávání chyb (`try-catch`)**  

---

### **📌 Ladicí výpisy (`debug`)**  
Bude existovat **speciální funkce `debug()`,** která umožní snadno zobrazit aktuální hodnoty:  
```plaintext
x = 10  
y = 20  
debug(x, y)  # → "DEBUG: x = 10, y = 20"
```
➡ Funguje podobně jako `print()`, ale s označením "DEBUG".  

📌 **Ladicí úroveň (verbosity level)**  
Bude možné nastavit úroveň ladění (od 0 do 3):  
```plaintext
nastav debug 2  
```
| **Úroveň** | **Popis** |
|------------|----------|
| `0` | Ladění vypnuto |
| `1` | Základní výpisy |
| `2` | Detailní výpisy |
| `3` | Všechny interní procesy |

---

### **📌 Interaktivní sledování proměnných (`watch`)**  
Bude možné sledovat proměnnou **během běhu programu**:  
```plaintext
watch(x)  
```
➡ Kdykoliv se `x` změní, vypíše se její nová hodnota.  

📌 **Příklad:**  
```plaintext
x = 5  
watch(x)  
x = 10  # → "WATCH: x změněno na 10"
```
➡ Skvělé pro hledání nečekaných změn!  

---

### **📌 Krokování kódu (`step-by-step`)**  
Bude možné **pozastavit běh programu a provádět ho krok za krokem**:  
```plaintext
pause()  # Pozastaví běh  
step()   # Provede jeden příkaz  
continue()  # Pokračuje v běhu  
```
📌 **Příklad použití:**  
```plaintext
x = 1  
pause()  
x = 2  
y = x + 3  # Tento krok se provede až po `step()`
```
➡ Umožní přesně sledovat, co se kdy provádí.  

---

### **📌 Zachytávání chyb (`try-catch`)**  
Bude možné zachytit chyby a zabránit pádu programu:  
```plaintext
zkus:  
    x = 1 / 0  
chyba:  
    debug("Chyba: dělení nulou!")  
```
➡ Pokud dojde k chybě, program nespadne, ale vypíše varování.  

---

### **🚀 Další krok?**  
✔ **Chceš rozšířit debugging, nebo se přesunout k optimalizaci binární reprezentace?**