"""
Tady je seznam výjimek, které by mohl kód `_test_file_operations` vyvolat, seřazených podle pořadí, v jakém by mohly nastat během vykonávání kódu:

1. **FileNotFoundError**
   - **Příčina**: Adresář, ve kterém se soubor pokouší vytvořit, neexistuje
   - **Kontrola**: Ověřit, zda rodičovský adresář `self._test_file.parent` existuje

2. **PermissionError** (při otevírání pro zápis)
   - **Příčina**: Nedostatečná oprávnění pro vytvoření nebo zápis do souboru
   - **Kontrola**: Ověřit oprávnění uživatele v daném adresáři

3. **OSError** (při otevírání pro zápis)
   - **Příčina**: Obecná chyba operačního systému, např. plný disk, zamčený soubor
   - **Kontrola**: Zkontrolovat dostupné místo na disku, zda soubor není používán jiným procesem

4. **IOError** (při zápisu)
   - **Příčina**: Chyba při zápisu dat, například přerušené síťové spojení u síťových disků
   - **Kontrola**: Ověřit stabilitu úložiště, síťové připojení

5. **FileNotFoundError** (při otevírání pro čtení)
   - **Příčina**: Soubor byl mezi zápisem a čtením smazán nebo přesunut jiným procesem
   - **Kontrola**: Ověřit, zda jiné procesy nemanipulují se soubory v dané lokaci

6. **PermissionError** (při otevírání pro čtení)
   - **Příčina**: Nedostatečná oprávnění pro čtení souboru (může nastat při změně oprávnění mezi zápisem a čtením)
   - **Kontrola**: Ověřit, zda se oprávnění souboru nemění jinými procesy

7. **OSError** (při otevírání pro čtení)
   - **Příčina**: Obecná chyba operačního systému, např. poškozený souborový systém
   - **Kontrola**: Zkontrolovat integritu souborového systému

8. **UnicodeDecodeError** (při čtení)
   - **Příčina**: Problém s kódováním při čtení souboru
   - **Kontrola**: Zkontrolovat, zda čtení používá správné kódování

9. **AttributeError** (při čtení)
   - **Příčina**: Pokud by `self._test_message` nebyl správně inicializován
   - **Kontrola**: Ověřit, že `self._test_message` byl nastaven před voláním této metody

10. **FileNotFoundError** (při mazání)
    - **Příčina**: Soubor byl mezitím smazán jiným procesem
    - **Kontrola**: Ověřit, zda jiné procesy nemanipulují se soubory v dané lokaci

11. **PermissionError** (při mazání)
    - **Příčina**: Nedostatečná oprávnění pro odstranění souboru
    - **Kontrola**: Ověřit oprávnění uživatele pro mazání v adresáři

12. **OSError** (při mazání)
    - **Příčina**: Obecná chyba operačního systému, např. soubor je otevřen jiným procesem
    - **Kontrola**: Ověřit, zda soubor není používán jiným procesem

13. **TypeError**
    - **Příčina**: Pokud by `self._test_file` nebyl instance `Path` nebo pokud by `self._test_message` nebyl typu string
    - **Kontrola**: Ověřit správné typy atributů třídy

14. **IsADirectoryError**
    - **Příčina**: Pokud by `self._test_file` odkazoval na adresář místo na soubor
    - **Kontrola**: Ověřit, že cesta skutečně odkazuje na soubor, ne na adresář

15. **NotADirectoryError**
    - **Příčina**: Pokud by rodičovská cesta `self._test_file.parent` byla soubor, ne adresář
    - **Kontrola**: Ověřit, že rodičovská cesta je skutečně adresář

Při implementaci zachytávání výjimek je efektivní seřadit je od konkrétních po obecné, například:

```python
try:
    self._test_file_operations()
except FileNotFoundError as e:
    # Zpracování chyby nenalezeného souboru
except PermissionError as e:
    # Zpracování chyby oprávnění
except (IOError, OSError) as e:
    # Zpracování obecných chyb souborového systému
except UnicodeDecodeError as e:
    # Zpracování chyby kódování
except TypeError as e:
    # Zpracování typové chyby
except Exception as e:
    # Zachycení všech ostatních výjimek
```

Tento přístup ti umožní rozlišit běžné chyby a poskytovat uživatelům přesnější informace o problému.
"""