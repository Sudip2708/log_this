Jistě! Tady je tabulka, která shrnuje metody z modulu `traceback`, jejich vrácené hodnoty a způsoby, jak s těmito hodnotami pracovat.

| **Metoda**               | **Co vrací**                                                                 | **Jak s tím pracovat**                                              |
|--------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------|
| **`traceback.format_exc()`** | Vrací **textový řetězec** obsahující kompletní traceback pro poslední výjimku, včetně souboru, řádku a typu chyby. | Tento výstup lze rovnou použít k vypsání chybového výpisu do konzole. Např. `print(traceback.format_exc())` nebo `sys.stderr.write(traceback.format_exc())`. |
| **`traceback.extract_tb(tb)`** | Vrací **seznam** `n` položek typu `FrameSummary`, který obsahuje informace o zásobníku volání. Každý záznam obsahuje soubor, řádek, funkci a kód v daném bodě volání. | Výstup je užitečný pro detailní zpracování tracebacku, např. pro zobrazení souboru a řádku, nebo k jeho vlastní analýze. Můžeš použít smyčku: `for frame in traceback.extract_tb(tb): print(frame)`. |
| **`traceback.format_list(extracted_list)`** | Vrací **seznam** řetězců, které jsou lidsky čitelné a představují formátovaný výstup jednotlivých položek z `extract_tb()`. | Tento výstup lze rovněž použít pro tisk tracebacku ve formátu, který je snadno čitelný uživateli. Např. `print(''.join(traceback.format_list(extracted_list)))`. |
| **`traceback.format_tb(tb)`** | Vrací **seznam řetězců**, které představují formátované textové výstupy z tracebacku, obdobně jako `format_list()`, ale pro konkrétní traceback. | Použití je podobné jako `format_list()`, ale s tím, že pracuje přímo s objektem tracebacku, takže jej lze použít, když máš přístup k `tb` (traceback objektu). Např. `print(''.join(traceback.format_tb(tb)))`. |
| **`traceback.print_exc()`** | Tiskne kompletní traceback na standardní chybový výstup (stderr). Je to ekvivalent k `format_exc()`, ale rovnou tiskne výstup místo jeho vrácení. | Tato metoda je vhodná, když chceš okamžitě vypsat celý traceback bez nutnosti jeho předchozího uchovávání v proměnné. Např. `traceback.print_exc()` ve výjimce. |
| **`traceback.print_tb(tb)`** | Tiskne traceback na standardní chybový výstup (stderr), ale na rozdíl od `print_exc()` tiskne **pouze** informace o zásobníku volání (ne celé chybové hlášení). | Tento výstup je vhodný, pokud chceš tisknout pouze informace o volání, bez detailních informací o chybě (např. o typu výjimky). Použití: `traceback.print_tb(tb)`. |

---

### **Příklady použití:**

1. **`traceback.format_exc()`**:
   ```python
   try:
       1 / 0
   except Exception:
       print(traceback.format_exc())  # Vytiskne celý traceback v textovém formátu
   ```

2. **`traceback.extract_tb()`**:
   ```python
   try:
       1 / 0
   except Exception as e:
       tb = e.__traceback__
       extracted = traceback.extract_tb(tb)
       for frame in extracted:
           print(frame)  # Každý záznam je typu FrameSummary
   ```

3. **`traceback.format_list()`**:
   ```python
   try:
       1 / 0
   except Exception as e:
       tb = e.__traceback__
       extracted = traceback.extract_tb(tb)
       formatted = traceback.format_list(extracted)
       print(''.join(formatted))  # Vytiskne formátovaný seznam tracebacku
   ```

4. **`traceback.print_exc()`**:
   ```python
   try:
       1 / 0
   except Exception:
       traceback.print_exc()  # Okamžitě vytiskne celý traceback na stderr
   ```

---

Tato tabulka ti poskytne přehled o možnostech, jak s tracebackem pracovat. Záleží na tvých potřebách, jestli chceš **formatovaný text** pro pohodlný výstup, nebo jestli potřebuješ detailnější **zpracování zásobníku volání** s možností vlastní analýzy nebo výstupu.