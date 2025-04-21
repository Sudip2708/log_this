### **1. Základní implementace (MVP)**
🔹 **Cíl**: Vytvořit funkční jádro knihovny s klíčovými metodami.  
✅ **Akce**:  
- Implementuj **čtyři nejzásadnější metody**:  
  - `catch()`  
  - `handle()`  
  - `verify()`  
  - `set_default_handler()`  
- Napiš základní **testy jednotek** pro ověření funkcionality.  
- Připrav základní **dokumentaci** (krátké popisy metod + příklady použití).  

---

### **2. Refinement & Optimalizace**
🔹 **Cíl**: Vyladit a zpřehlednit základní API.  
✅ **Akce**:  
- Otestuj knihovnu na reálných scénářích.  
- Projděte si názvy metod – jsou dostatečně intuitivní?  
- Optimalizuj výkon a minimalizuj závislosti.  

---

### **3. Rozšíření funkcionality**
🔹 **Cíl**: Přidat užitečné, ale ne kritické metody.  
✅ **Akce**:  
- Implementuj **středně důležité metody**:  
  - `safe_verify()`  
  - `set_log_level()`  
  - `set_message()`  
- Přidej volitelné parametry ke stávajícím metodám pro větší flexibilitu.  
- Rozšiř testovací sadu na více případů použití.  

---

### **4. Pokročilé funkce a modularizace**
🔹 **Cíl**: Připravit rozšířené možnosti pro náročnější uživatele.  
✅ **Akce**:  
- Přidej **méně důležité metody** jako volitelné moduly:  
  - `set_log_format()`, `register_global_handler()`, `create_exception_group()`, `set_retry_strategy()`.  
- Zvaž rozdělení na **jádro + rozšiřující moduly**.  

---

### **5. Publikace a zpětná vazba**
🔹 **Cíl**: Otevřít knihovnu světu a získat zpětnou vazbu.  
✅ **Akce**:  
- Vytvoř **README** s přehledným vysvětlením a příklady.  
- Publikuj balíček na **PyPI**.  
- Sdílej knihovnu a sbírej zpětnou vazbu od uživatelů.  
- Na základě zpětné vazby uprav funkcionalitu nebo API.  

---

