def attribute_error_handler(e):
    print("Popis výjimky: Chyba atributu.")
    print("Možné příčiny: Vyvolá se, když je nesprávně definovaný některý atribut.")
    print("Možné řešení: Ujistěte se, zda má správně definované všechny potřebné atributy.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def type_error_handler(e):
    print("Popis výjimky: Chyba typu souboru")
    print("Možné příčiny: Vyvolá se, když atribut odkazující na cestu není instancí Path.")
    print("Možné řešení: Ujistěte se, zda je atribut správně definován.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def file_not_found_error_handler(e):
    print("Popis výjimky: Chyba v definici cesty k souboru.")
    print("Možné příčiny: Vyvolá se, když atribut _test_file má špatně definovanou cestu a některý z adresářů je uveden jako soubor")
    print("Možné řešení: Kontrola kodu, zda je atribut správně definován.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def not_a_directory_error_handler(e):
    print("Popis výjimky: Chyba v definici cesty k souboru.")
    print("Možné příčiny: Vyvolá se, když atribut _test_file má špatně definovanou cestu a rodičovská cesta není adresář")
    print("Možné řešení: Ujistěte se, že rodičovská cesta je skutečně adresář.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def permission_error_handler(e):
    print("Popis výjimky: Nedostatečná oprávnění pro zápis.")
    print("Možné příčiny: Nemáte dostatečná oprávnění pro zápis do souboru v daném adresáři.")
    print("Možné řešení: Ujistěte se, že máte oprávnění pro zápis do souboru, a že soubor není otevřen v jiném programu nebo procesu.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def os_error_handler(e):
    print("Popis výjimky: Chyba při operacemi se souborem.")
    print("Možné příčiny: Může se objevit, pokud dojde k nějakému hardwarovému nebo systémovému problému při práci se souborem.")
    print("Možné řešení: Zkontrolujte, zda existuje problém s disky nebo souborovým systémem. Ujistěte se, že máte dostatek volného místa na disku a že je disk dostupný.")
    print(f"Zachycené podrobnosti: {e}")
    return False

def content_mismatch_error_handler(e):
    print("Popis výjimky: Chyba při zápisu, a čtení souboru.")
    print("Možné příčiny: Výjimka je vyvolaná, pokud načtený testovací obsah neodpovídá ukloženému.")
    print("Možné řešení: Je potřeba zkontrolovat proces ukládání a načítání dat.")
    print(f"Zachycené podrobnosti: {e}")
    return False

