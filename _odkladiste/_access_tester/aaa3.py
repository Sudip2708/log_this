"""
Ahoj Dalibore! Určitě, tady je seznam výjimek, které by tento kód mohl vyvolat, včetně možných příčin a diagnostiky pro každou z nich. Výjimky jsou seřazeny podle toho, jak by se pravděpodobně vyskytly v průběhu kódu.

### 1. **`FileNotFoundError`** – při čtení souboru
   **Příčina**: Soubory, které se snažíte číst, neexistují, nebo byly odstraněny před jejich otevřením.
   **Diagnostika**: Zkontrolujte, zda soubor existuje před tím, než ho otevřete pro čtení. Pokud používáte `unlink()`, ujistěte se, že soubor je správně smazán a není otevřen pro čtení v daný okamžik.
   ```python
   except FileNotFoundError as e:
       print(f"Soubor nenalezen: {e}")
   ```

### 2. **`PermissionError`** – při pokusu o zápis do souboru
   **Příčina**: Nemáte dostatečná oprávnění pro zápis do souboru v daném adresáři.
   **Diagnostika**: Ujistěte se, že máte oprávnění pro zápis do souboru, a že soubor není otevřen v jiném programu nebo procesu.
   ```python
   except PermissionError as e:
       print(f"Nedostatečná oprávnění pro zápis: {e}")
   ```

### 3. **`IsADirectoryError`** – při otevření souboru pro zápis nebo čtení
   **Příčina**: Pokus o otevření adresáře jako souboru.
   **Diagnostika**: Ujistěte se, že cíl souboru není adresář a že jste správně zadali cestu k souboru.
   ```python
   except IsADirectoryError as e:
       print(f"Je to adresář, nikoliv soubor: {e}")
   ```

### 4. **`OSError`** – při obecném problému s operacemi na souborech
   **Příčina**: Může se objevit, pokud dojde k nějakému hardwarovému nebo systémovému problému při otevření souboru.
   **Diagnostika**: Zkontrolujte, zda existuje problém s disky nebo souborovým systémem. Ujistěte se, že máte dostatek volného místa na disku a že je disk dostupný.
   ```python
   except OSError as e:
       print(f"Obecná chyba při práci se souborem: {e}")
   ```

### 5. **`IOError`** – při problémech s čtením/zápisem do souboru
   **Příčina**: Tento typ výjimky může nastat při problémech s fyzickým čtením nebo zápisem dat (například soubor může být poškozen nebo ztracen při operaci).
   **Diagnostika**: Ověřte, že soubor není poškozen, a zda je možné do něj číst a zapisovat. Zkontrolujte stabilitu disku.
   ```python
   except IOError as e:
       print(f"Chyba při čtení nebo zápisu do souboru: {e}")
   ```

### 6. **`FileExistsError`** – při pokusu o zápis do souboru v případě, že soubor již existuje (pokud by byl použít jiný režim než `'w'`)
   **Příčina**: Pokus o otevření souboru pro zápis v režimu, kde soubor již existuje, a nemá být přepsán (např. `x` režim).
   **Diagnostika**: Pokud máte předem stanovený režim pro zápis, ujistěte se, že se soubor neexistuje, nebo použijte režim `'w'`, který soubor přepíše.
   ```python
   except FileExistsError as e:
       print(f"Soubor již existuje a nelze jej přepsat: {e}")
   ```

### 7. **`ValueError`** – při chybě čtení souboru (pokud by došlo k problémům s datovým formátem)
   **Příčina**: Pokud se pokusíte přečíst soubor s nekompatibilním nebo neočekávaným formátem (třeba pokud čtete binární soubor jako text).
   **Diagnostika**: Zkontrolujte, že soubor, který čtete, má správný formát a že používáte odpovídající režim čtení (např. `'r'` pro textový soubor).
   ```python
   except ValueError as e:
       print(f"Chyba při čtení souboru: {e}")
   ```

### 8. **`NameError`** – pokud `self._test_file` nebo `self._test_message` nejsou definovány
   **Příčina**: Pokud proměnné nebo objekty, které používáte (např. `self._test_file` nebo `self._test_message`), nejsou správně inicializovány nebo jsou nesprávně pojmenovány.
   **Diagnostika**: Ujistěte se, že všechny atributy objektu jsou správně nastaveny a existují před použitím v metodách.
   ```python
   except NameError as e:
       print(f"Neznámý název proměnné nebo atributu: {e}")
   ```

### 9. **`FileNotClosedError`** – pokud soubor není správně uzavřen po operaci
   **Příčina**: Pokud soubor není korektně uzavřen před tím, než ho znovu otevřete nebo provádíte další operace.
   **Diagnostika**: Zkontrolujte, zda jsou všechny soubory uzavřeny pomocí kontextového manažera (`with`), aby se předešlo otevřeným souborům.
   ```python
   except FileNotClosedError as e:
       print(f"Soubor nebyl správně uzavřen: {e}")
   ```

### 10. **`UnlinkError`** – při pokusu o smazání souboru
   **Příčina**: Pokud soubor nemůže být smazán, může to být způsobeno tím, že soubor je otevřený nebo má jiný proces nebo aplikace zámek na soubor.
   **Diagnostika**: Zkontrolujte, zda soubor není používán jiným procesem, a že máte potřebná oprávnění pro jeho odstranění.
   ```python
   except UnlinkError as e:
       print(f"Chyba při mazání souboru: {e}")
   ```

### Shrnutí
Pokud by všechny výjimky byly vyvolány, mohlo by se to stát ve vypsaném pořadí, od problému s čtením, zápisem, přes problémy s oprávněními až po problémy s existencí souboru nebo problémy s uzavřením souboru. Tímto způsobem můžete pokrýt většinu situací a provést diagnostiku, která vám pomůže odhalit příčiny problémů.
"""