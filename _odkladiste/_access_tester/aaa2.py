"""
Ahoj! Jasně, tady je seznam výjimek, které by teoreticky mohl vyvolat tvůj kód `_test_file_operations`, včetně možných příčin a diagnostiky, seřazených v pořadí, v jakém by se mohly vyskytnout:

**1. `FileNotFoundError` (Při otevření souboru pro zápis):**

* **Příčina:**
    * Adresář, ve kterém se má soubor vytvořit, neexistuje.
    * Nemáš dostatečná oprávnění k zápisu do daného adresáře.
* **Diagnostika:**
    * Zkontroluj, zda existuje cesta `self._test_file.parent`.
    * Ověř oprávnění k zápisu do adresáře.

**2. `PermissionError` (Při otevření souboru pro zápis):**

* **Příčina:**
    * Nemáš oprávnění k vytvoření nebo zápisu do souboru v daném adresáři.
    * Soubor nebo adresář je chráněn systémem souborů.
* **Diagnostika:**
    * Ověř oprávnění pro aktuálního uživatele.
    * Zkontroluj, zda soubor nebo adresář nejsou chráněny.

**3. `OSError` (Při otevření souboru pro zápis):**

* **Příčina:**
    * Nedostatek diskového prostoru.
    * Problémy s diskovým hardwarem.
    * Problémy s připojením síťového disku.
* **Diagnostika:**
    * Zkontroluj volné místo na disku.
    * Ověř stav disku a síťového připojení.
    * Zkontroluj logy operačního systému.

**4. `FileNotFoundError` (Při otevření souboru pro čtení):**

* **Příčina:**
    * Soubor nebyl vytvořen (například kvůli výjimce při zápisu).
    * Soubor byl smazán jiným procesem.
* **Diagnostika:**
    * Zkontroluj, zda soubor existuje před pokusem o čtení.
    * Zkontroluj, zda soubor nebyl smazán jiným procesem.

**5. `PermissionError` (Při otevření souboru pro čtení):**

* **Příčina:**
    * Nemáš oprávnění ke čtení souboru.
    * Soubor je chráněn systémem souborů.
* **Diagnostika:**
    * Ověř oprávnění ke čtení souboru.
    * Zkontroluj, zda soubor není chráněn.

**6. `UnicodeDecodeError` (Při čtení souboru):**

* **Příčina:**
    * Soubor obsahuje data, která nelze dekódovat s použitým kódováním.
    * Kódování souboru se liší od očekávaného.
* **Diagnostika:**
    * Ověř kódování souboru.
    * Zkontroluj, zda se kódování shoduje s použitým kódováním při čtení.

**7. `FileContentMismatchError` (Vlastní výjimka):**

* **Příčina:**
    * Obsah souboru neodpovídá očekávanému textu `self._test_message`.
    * Soubor byl upraven jiným procesem.
* **Diagnostika:**
    * Zkontroluj, zda se texty shodují.
    * Zkontroluj, zda soubor nebyl upraven jiným procesem.
    * Zkontroluj, zda se texty shodují.

**8. `FileNotFoundError` (Při smazání souboru):**

* **Příčina:**
    * Soubor již byl smazán jiným procesem.
    * Soubor nebyl nikdy vytvořen.
* **Diagnostika:**
    * Ověř existenci souboru před jeho smazáním.

**9. `PermissionError` (Při smazání souboru):**

* **Příčina:**
    * Nemáš oprávnění ke smazání souboru.
    * Soubor je chráněn systémem souborů.
* **Diagnostika:**
    * Ověř oprávnění ke smazání souboru.
    * Zkontroluj, zda soubor není chráněn.

**10. `OSError` (Při smazání souboru):**

* **Příčina:**
    * Problémy s diskovým hardwarem.
    * Problémy s připojením síťového disku.
* **Diagnostika:**
    * Ověř stav disku a síťového připojení.
    * Zkontroluj logy operačního systému.

**Důležité poznámky:**

* Při ošetřování výjimek je důležité zachytávat konkrétní výjimky, aby se předešlo zachycení neočekávaných chyb.
* Vždy je dobré poskytnout uživateli nebo logovacímu systému smysluplné informace o tom, co se stalo.
* Při testování na zapisovatelnost souboru, je vhodné ošetřit i situaci, kdy se testuje soubor na síťovém disku, který může být dočasně nedostupný.

"""