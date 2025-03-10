from pathlib import Path
import os
import shutil

class ContentMismatchError(Exception):
    """Výjimka vyvolaná, pokud se obsah souboru neshoduje s očekáváním."""
    pass

class AccessTester:
    """Třída pro otestování práce se souborem s přidanou diagnostikou chyb"""

    _path = None
    _dir_path = None
    _test_file = None
    _test_message = "This is a test."
    _content_mismatch = None

    def __call__(self, path: Path) -> bool:
        self._path = path
        self._dir_path = self._path if self._path.is_dir() else self._path.parent
        self._test_file = self._dir_path / f"_test_file_{os.getpid()}.tmp"

        try:
            self._test_file_operations()

        except FileNotFoundError as e:
            """
            * **Příčina:**
                * Adresář, ve kterém se má soubor vytvořit, neexistuje.
                * Nemáš dostatečná oprávnění k zápisu do daného adresáře.
            * **Diagnostika:**
                * Zkontroluj, zda existuje cesta `self._test_file.parent`.
                * Ověř oprávnění k zápisu do adresáře.
                
             – při čtení souboru
           **Příčina**: Soubory, které se snažíte číst, neexistují, nebo byly odstraněny před jejich otevřením.
           **Diagnostika**: Zkontrolujte, zda soubor existuje před tím, než ho otevřete pro čtení. Pokud používáte `unlink()`, ujistěte se, že soubor je správně smazán a není otevřen pro čtení v daný okamžik.
                
            """
            # Zpracování chyby nenalezeného souboru (při otevírání pro čtení, mazání)
            #   - **Příčina**: Adresář, ve kterém se soubor pokouší vytvořit, neexistuje
            #   - **Kontrola**: Ověřit, zda rodičovský adresář `self._test_file.parent` existuje
            print(f"Soubor nenalezen: {e}")

        except PermissionError as e:
            """
            * **Příčina:**
                * Nemáš oprávnění k vytvoření nebo zápisu do souboru v daném adresáři.
                * Soubor nebo adresář je chráněn systémem souborů.
            * **Diagnostika:**
                * Ověř oprávnění pro aktuálního uživatele.
                * Zkontroluj, zda soubor nebo adresář nejsou chráněny.
                
             – při pokusu o zápis do souboru
           **Příčina**: Nemáte dostatečná oprávnění pro zápis do souboru v daném adresáři.
           **Diagnostika**: Ujistěte se, že máte oprávnění pro zápis do souboru, a že soubor není otevřen v jiném programu nebo procesu.
                
            """
            # Zpracování chyby oprávnění (při otevírání pro zápis, čtení, mazání)
            #   - **Příčina**: Nedostatečná oprávnění pro vytvoření nebo zápis do souboru
            #   - **Kontrola**: Ověřit oprávnění uživatele v daném adresáři
            print(f"Nedostatečná oprávnění pro zápis: {e}")

        except IsADirectoryError as e:
            """
             – při otevření souboru pro zápis nebo čtení
               **Příčina**: Pokus o otevření adresáře jako souboru.
               **Diagnostika**: Ujistěte se, že cíl souboru není adresář a že jste správně zadali cestu k souboru.

            """
            # Zachycení pokud cesta neodkazuje na soubor
            #    - **Příčina**: Pokud by `self._test_file` odkazoval na adresář místo na soubor
            #    - **Kontrola**: Ověřit, že cesta skutečně odkazuje na soubor, ne na adresář
            print(f"Je to adresář, nikoliv soubor: {e}")

        except OSError as e:
            """
            OSError:
            * **Příčina:**
                * Nedostatek diskového prostoru.
                * Problémy s diskovým hardwarem.
                * Problémy s připojením síťového disku.
            * **Diagnostika:**
                * Zkontroluj volné místo na disku.
                * Ověř stav disku a síťového připojení.
                * Zkontroluj logy operačního systému.     
                
             – při obecném problému s operacemi na souborech
           **Příčina**: Může se objevit, pokud dojde k nějakému hardwarovému nebo systémovému problému při otevření souboru.
           **Diagnostika**: Zkontrolujte, zda existuje problém s disky nebo souborovým systémem. Ujistěte se, že máte dostatek volného místa na disku a že je disk dostupný.
                       
            """
            # Zpracování obecných chyb souborového systému
            # OSError: (při otevírání pro zápis, čtení, mazání)
            #   - **Příčina**: Obecná chyba operačního systému, např. plný disk, zamčený soubor
            #   - **Kontrola**: Zkontrolovat dostupné místo na disku, zda soubor není používán jiným procesem
            print(f"Obecná chyba při práci se souborem: {e}")

        except IOError as e:
            """
            OSError:
            * **Příčina:**
                * Nedostatek diskového prostoru.
                * Problémy s diskovým hardwarem.
                * Problémy s připojením síťového disku.
            * **Diagnostika:**
                * Zkontroluj volné místo na disku.
                * Ověř stav disku a síťového připojení.
                * Zkontroluj logy operačního systému.   
                
             – při problémech s čtením/zápisem do souboru    
           **Příčina**: Tento typ výjimky může nastat při problémech s fyzickým čtením nebo zápisem dat (například soubor může být poškozen nebo ztracen při operaci).
           **Diagnostika**: Ověřte, že soubor není poškozen, a zda je možné do něj číst a zapisovat. Zkontrolujte stabilitu disku.
         
            """
            # Zpracování obecných chyb souborového systému
            # OSError: (při otevírání pro zápis, čtení, mazání)
            #   - **Příčina**: Obecná chyba operačního systému, např. plný disk, zamčený soubor
            #   - **Kontrola**: Zkontrolovat dostupné místo na disku, zda soubor není používán jiným procesem
            # IOError: (při zápisu)
            #   - **Příčina**: Chyba při zápisu dat, například přerušené síťové spojení u síťových disků
            #   - **Kontrola**: Ověřit stabilitu úložiště, síťové připojení
            print(f"Chyba při čtení nebo zápisu do souboru: {e}")

        except FileExistsError as e:
            """
             – při pokusu o zápis do souboru v případě, že soubor již existuje (pokud by byl použít jiný režim než `'w'`)
               **Příčina**: Pokus o otevření souboru pro zápis v režimu, kde soubor již existuje, a nemá být přepsán (např. `x` režim).
               **Diagnostika**: Pokud máte předem stanovený režim pro zápis, ujistěte se, že se soubor neexistuje, nebo použijte režim `'w'`, který soubor přepíše.

            """
            print(f"Soubor již existuje a nelze jej přepsat: {e}")

        except ValueError as e:
            """
             – při chybě čtení souboru (pokud by došlo k problémům s datovým formátem)
               **Příčina**: Pokud se pokusíte přečíst soubor s nekompatibilním nebo neočekávaným formátem (třeba pokud čtete binární soubor jako text).
               **Diagnostika**: Zkontrolujte, že soubor, který čtete, má správný formát a že používáte odpovídající režim čtení (např. `'r'` pro textový soubor).
            """
            print(f"Chyba při čtení souboru: {e}")

        except NameError as e:
            """
            – pokud `self._test_file` nebo `self._test_message` nejsou definovány
            **Příčina**: Pokud proměnné nebo objekty, které používáte (např. `self._test_file` nebo `self._test_message`), nejsou správně inicializovány nebo jsou nesprávně pojmenovány.
            **Diagnostika**: Ujistěte se, že všechny atributy objektu jsou správně nastaveny a existují před použitím v metodách.
            """
            print(f"Neznámý název proměnné nebo atributu: {e}")

        except FileNotClosedError as e:
            """
             – pokud soubor není správně uzavřen po operaci
           **Příčina**: Pokud soubor není korektně uzavřen před tím, než ho znovu otevřete nebo provádíte další operace.
           **Diagnostika**: Zkontrolujte, zda jsou všechny soubory uzavřeny pomocí kontextového manažera (`with`), aby se předešlo otevřeným souborům.

            """
            print(f"Soubor nebyl správně uzavřen: {e}")

        except UnlinkError as e:
            """
             – při pokusu o smazání souboru
           **Příčina**: Pokud soubor nemůže být smazán, může to být způsobeno tím, že soubor je otevřený nebo má jiný proces nebo aplikace zámek na soubor.
           **Diagnostika**: Zkontrolujte, zda soubor není používán jiným procesem, a že máte potřebná oprávnění pro jeho odstranění.

            """
            print(f"Chyba při mazání souboru: {e}")

        except UnicodeDecodeError as e:
            """
            * **Příčina:**
                * Soubor obsahuje data, která nelze dekódovat s použitým kódováním.
                * Kódování souboru se liší od očekávaného.
            * **Diagnostika:**
                * Ověř kódování souboru.
                * Zkontroluj, zda se kódování shoduje s použitým kódováním při čtení.
            """
            # Zpracování chyby kódování (při čtení)
            #   - **Příčina**: Problém s kódováním při čtení souboru
            #   - **Kontrola**: Zkontrolovat, zda čtení používá správné kódování
            pass
        except AttributeError as e:
            # Zpracování chybějících atributů (při čtení)
            #   - **Příčina**: Pokud by `self._test_message` nebyl správně inicializován
            #   - **Kontrola**: Ověřit, že `self._test_message` byl nastaven před voláním této metody
            pass
        except FileContentMismatchError as e:
            """
            * **Příčina:**
                * Obsah souboru neodpovídá očekávanému textu `self._test_message`.
                * Soubor byl upraven jiným procesem.
            * **Diagnostika:**
                * Zkontroluj, zda se texty shodují.
                * Zkontroluj, zda soubor nebyl upraven jiným procesem.
                * Zkontroluj, zda se texty shodují.            
            """
            # Vlastní výjimka (při čtení)
            pass
        except TypeError as e:
            # Zpracování typové chyby
            #    - **Příčina**: Pokud by `self._test_file` nebyl instance `Path` nebo pokud by `self._test_message` nebyl typu string
            #    - **Kontrola**: Ověřit správné typy atributů třídy
            pass

        except NotADirectoryError as e:
            # Zachycení pokud cesta neodkazuje na soubor
            #    - **Příčina**: Pokud by rodičovská cesta `self._test_file.parent` byla soubor, ne adresář
            #    - **Kontrola**: Ověřit, že rodičovská cesta je skutečně adresář
            pass
        except Exception as e:
            # Zachycení všech ostatních výjimek
            #
            #
            pass


        finally:
            if self._content_mismatch:
                """
                Příčiny neshody textů a jejich zjištění:
                Problémy se zápisem:
                Může se stát, že zápis do souboru nebyl dokončen z důvodu nedostatku diskového prostoru nebo jiných I/O chyb.
                Jak zjistit: Zkontroluj volné místo na disku, logy operačního systému a výjimky při zápisu.
                Problémy s kódováním:
                Pokud se kódování při zápisu a čtení liší, může dojít k poškození textu.
                Jak zjistit: Ověř kódování souboru a ujisti se, že se shoduje s kódováním použitým při čtení a zápisu.
                Souběžný přístup k souboru:
                Pokud jiný proces nebo vlákno souběžně modifikuje soubor, může dojít k nekonzistenci.
                Jak zjistit: Zkontroluj, zda soubor není používán jinými procesy nebo vlákny. Použij zámky (locks) pro synchronizaci přístupu.
                Chyby při čtení:
                Může se stát, že při čtení dojde k chybě, která způsobí, že se přečte neúplný nebo poškozený text.
                Jak zjistit: Ošetři výjimky při čtení a zkontroluj, zda se čtení dokončilo úspěšně.
                Chyby v operačním systému nebo disku:
                Vzácně se může stát, že dojde k chybě v operačním systému nebo na disku, která způsobí poškození dat.
                Jak zjistit: Zkontroluj logy operačního systému a proveď kontrolu disku.
                Chyby v programu:
                Nejčastější příčinou je chyba v programu, která způsobí, že se zapíše nebo přečte nesprávný text.
                Jak zjistit: Zkontroluj kód a ujisti se, že se zapisuje a čte správný text. Přidej logovací hlášky pro sledování hodnot proměnných.
                """



    def _test_file_operations(self):
        """Otestuje zápis, čtení a mazání souboru."""

        # Vytvoření souboru
        with self._test_file.open("w") as f:
            f.write(self._test_message)

        # Čtení souboru
        with self._test_file.open("r") as f:
            if f.read() != self._test_message:
                self._content_mismatch = f.read()

        # Smazání souboru
        self._test_file.unlink()


