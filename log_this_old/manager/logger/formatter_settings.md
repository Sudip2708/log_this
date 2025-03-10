### Parametry a jejich výstupy


1. **`%(asctime)s`**
   - Popis: Časová známka.
   - Výstup: `2025-01-08 12:34:56,789`
   - Formát: Datum a čas s milisekundami (lze přizpůsobit pomocí `datefmt`).


2. **`%(levelname)s`**
   - Popis: Úroveň záznamu (např. DEBUG, INFO, WARNING, ERROR, CRITICAL).
   - Výstup: `INFO`


3. **`%(message)s`**
   - Popis: Text zprávy, kterou zapisuješ pomocí `logger.info()` nebo podobných metod.
   - Výstup: `This is a log message.`


4. **`%(name)s`**
   - Popis: Jméno loggeru.
   - Výstup: `root`


5. **`%(pathname)s`**
   - Popis: Plná cesta ke skriptu, který vyvolal záznam.
   - Výstup: `/path/to/script.py`


6. **`%(filename)s`**
   - Popis: Jméno souboru, který vyvolal záznam.
   - Výstup: `script.py`


7. **`%(module)s`**
   - Popis: Jméno modulu, který vyvolal záznam (název souboru bez přípony `.py`).
   - Výstup: `script`


8. **`%(funcName)s`**
   - Popis: Jméno funkce, která vyvolala záznam.
   - Výstup: `my_function`


9. **`%(lineno)d`**
   - Popis: Číslo řádku ve skriptu, kde byl záznam vytvořen.
   - Výstup: `42`


10. **`%(process)d`**
    - Popis: ID procesu, který záznam vytvořil.
    - Výstup: `12345`


11. **`%(processName)s`**
    - Popis: Jméno procesu, který záznam vytvořil.
    - Výstup: `MainProcess`


12. **`%(thread)d`**
    - Popis: ID vlákna, které záznam vytvořilo.
    - Výstup: `140735641438208`


13. **`%(threadName)s`**
    - Popis: Jméno vlákna, které záznam vytvořilo.
    - Výstup: `MainThread`


14. **`%(created)d`**
    - Popis: Čas vytvoření záznamu ve formátu Unix Epoch (sekundy od 1. 1. 1970).
    - Výstup: `1704729312.345`
    

15. **`%(relativeCreated)d`**
    - Popis: Čas (v milisekundách) od spuštění programu do vytvoření záznamu.
    - Výstup: `12345`


16. **`%(msecs)d`**
    - Popis: Milisekundy z časové známky.
    - Výstup: `789`


17. **`%(levelno)d`**
    - Popis: Číselná hodnota úrovně záznamu (např. DEBUG=10, INFO=20).
    - Výstup: `20`


18. **`%(args)s`**
    - Popis: Argumenty předané metodě záznamu (pokud nějaké jsou).
    - Výstup: `None` (pokud nejsou žádné argumenty).


19. **`%(exc_info)s`**
    - Popis: Informace o výjimce, pokud byla záznamu předána.
    - Výstup: `None` (pokud není žádná výjimka).

---

### Ukázka formátovací šablony a výstupu

```python
import logging

# Vytvoření loggeru
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# Vytvoření handleru
console_handler = logging.StreamHandler()

# Vytvoření formátovače
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s - [%(filename)s:%(lineno)d]'
)
console_handler.setFormatter(formatter)

# Přidání handleru loggeru
logger.addHandler(console_handler)

# Záznam zprávy
logger.info("This is a test log message.")
```

### Výstup
```
2025-01-08 12:34:56,789 - INFO - example_logger - This is a test log message. - [script.py:42]
```

---

### **Doporučené rozdělení barev:**

1. **`black` (30)**  
   Použij pro méně důležité informace nebo části zprávy, které mají být přítomné, ale nemají rušit.  
   - **Využití:** Název loggeru (`%(name)s`), pokud jej nepovažuješ za klíčový.  

2. **`red` (31)**  
   Barva pro chyby nebo kritické zprávy, které vyžadují okamžitou pozornost.  
   - **Využití:** `%(levelname)s` při úrovních `ERROR` nebo `CRITICAL`.  

3. **`green` (32)**  
   Barva pro úspěšné operace nebo informace.  
   - **Využití:** `%(levelname)s` při úrovni `INFO` nebo jako zvýraznění úspěšných stavů.  

4. **`yellow` (33)**  
   Barva pro varování nebo upozornění na potenciální problémy.  
   - **Využití:** `%(levelname)s` při úrovni `WARNING`.  

5. **`blue` (34)**  
   Barva pro neutrální a stabilní prvky, které slouží k orientaci.  
   - **Využití:** Časová značka (`%(asctime)s`).  

6. **`magenta` (35)**  
   Barva pro ladění nebo testovací zprávy, případně další meta informace.  
   - **Využití:** `%(levelname)s` při úrovni `DEBUG`.  

7. **`cyan` (36)**  
   Barva pro hlavní obsah zprávy, která by měla být výrazná a snadno čitelná.  
   - **Využití:** `%(message)s`.  

8. **`white` (37)**  
   Barva pro jasné označení důležitého kontextu nebo výrazného prvku.  
   - **Využití:** Statické oddělovače nebo části, jako je `-` nebo `[ ]` kolem záznamů.  

9. **`default` (39)**  
   Barva, která může být použita pro části, které nemají být výrazně formátovány.  
   - **Využití:** Návrat k normálnímu textu po každé zvýrazněné části.  

---

### **Ukázka implementace v kódu:**

```python
import logging

class ColorFormatter(logging.Formatter):
    COLORS = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "default": "39",
    }
    
    def format(self, record):
        # Barevné přiřazení
        asctime = f"\033[{self.COLORS['blue']}m{record.asctime}\033[0m"  # Časová značka
        levelname_color = {
            "DEBUG": f"\033[{self.COLORS['magenta']}m",
            "INFO": f"\033[{self.COLORS['green']}m",
            "WARNING": f"\033[{self.COLORS['yellow']}m",
            "ERROR": f"\033[{self.COLORS['red']}m",
            "CRITICAL": f"\033[{self.COLORS['red']}m\033[1m",  # Tučné červené
        }.get(record.levelname, f"\033[{self.COLORS['default']}m")
        
        levelname = f"{levelname_color}{record.levelname}\033[0m"
        message = f"\033[{self.COLORS['cyan']}m{record.getMessage()}\033[0m"
        name = f"\033[{self.COLORS['black']}m{record.name}\033[0m"
        
        # Poskládání zprávy
        formatted = f"{asctime} - {name} - {levelname} - {message}"
        return formatted

# Logger
logger = logging.getLogger("BarevnýLogger")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Test logů
logger.debug("Toto je DEBUG zpráva!")
logger.info("Toto je INFO zpráva!")
logger.warning("Toto je WARNING zpráva!")
logger.error("Toto je ERROR zpráva!")
logger.critical("Toto je CRITICAL zpráva!")
```

---

### **Vysvětlení výstupu:**
- **Časová značka (`%(asctime)s`)**: **Modrá** (stabilní a neutrální).
- **Název loggeru (`%(name)s`)**: **Černá** (málo důležité).
- **Úroveň (`%(levelname)s`)**: Různé barvy podle závažnosti:
  - DEBUG – Magenta.
  - INFO – Zelená.
  - WARNING – Žlutá.
  - ERROR – Červená.
  - CRITICAL – Tučně červená.
- **Zpráva (`%(message)s`)**: **Azurová** (hlavní obsah, čitelný).

---



"""

    @staticmethod
    def get_formatter(self):
        formatter = logging.Formatter(

            '%(asctime)s'  # Časová známka: 2025-01-08 12:34:56,789
            '%(levelname)s'  # Úroveň záznamu: DEBUG, INFO, WARNING, ERROR, CRITICA
            '%(message)s'  # Zpráva: This is a log message.
            '%(name)s'  # Logger: root, LogThisConfig
            '%(pathname)s'  # Cesta k souboru: /path/to/script.py
            '%(filename)s'  # Soubor: script.py
            '%(module)s'  # Modul: script
            '%(funcName)s'  # Funkce: my_function
            '%(lineno)d'  # Řádek: 42
            '%(process)d'  # PID: 12345
            '%(processName)s'  # Název procesu: MainProcess
            '%(thread)d'  # ID vlákna: 140735641438208
            '%(threadName)s'  # Název vlákna: MainThread
            '%(created)d'  # Unix čas: 1704729312.345
            '%(relativeCreated)d'  # Od startu (ms): 12345
            '%(msecs)d'  # Milisekundy: 789
            '%(levelno)d'  # Číselná úroveň: 20
            '%(args)s'  # Argumenty: None
            '%(exc_info)s'  # Výjimka: None
            # Symbols
            ' - '
            '[%(levelname)s]'  # Úroveň v hranatých závorkách: [INFO]
            '<%(module)s>'  # Modul v lomených závorkách: <script>
            '{%(funcName)s}'  # Funkce v složených závorkách: {my_function}
            '|%(lineno)d|'  # Řádek ve svislítkách: |42|
        )
        return formatter

    class LoggingFormatterPalette:
        @staticmethod
        def get_formatter_palette():
            """
            Generates a palette of formatter strings for all logging attributes.
            Each line contains an attribute, a comment describing it, and an example output.
            """
            formatter = logging.Formatter(
                '%(asctime)s: 2025-01-08 12:34:56,789  # Timestamp with date, time, and milliseconds\n'
                '%(levelname)s: INFO  # Log level name\n'
                '%(message)s: This is a log message.  # Log message text\n'
                '%(name)s: root  # Logger name\n'
                '%(pathname)s: /path/to/script.py  # Full path to the script\n'
                '%(filename)s: script.py  # Name of the script file\n'
                '%(module)s: script  # Module name (file name without .py)\n'
                '%(funcName)s: my_function  # Function name that logged the message\n'
                '%(lineno)d: 42  # Line number where the log call was made\n'
                '%(process)d: 12345  # Process ID that logged the message\n'
                '%(processName)s: MainProcess  # Name of the process\n'
                '%(thread)d: 140735641438208  # Thread ID\n'
                '%(threadName)s: MainThread  # Name of the thread\n'
                '%(created)d: 1704729312.345  # Timestamp in Unix epoch\n'
                '%(relativeCreated)d: 12345  # Time since program start (ms)\n'
                '%(msecs)d: 789  # Milliseconds part of the timestamp\n'
                '%(levelno)d: 20  # Numeric level of the log (e.g., INFO=20)\n'
                '%(args)s: None  # Arguments passed to the log message\n'
                '%(exc_info)s: None  # Exception info, if any\n'
                '
                # Symbols often used in logs\n'
                '[%(levelname)s]: INFO  # Log level in square brackets\n'
                '<%(module)s>: script  # Module name in angle brackets\n'
                '{%(funcName)s}: my_function  # Function name in curly braces\n'
                '|%(lineno)d|: 42  # Line number in vertical bars\n'
            )
            return formatter

"""