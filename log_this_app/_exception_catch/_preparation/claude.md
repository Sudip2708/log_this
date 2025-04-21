## Dotaz:

Co říkáš na definici tohoto dekorátoru:


Copy
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def exception_catch(*exceptions):
    """Dekorátor pro zachytávání specifikovaných výjimek a logování chyb."""

    # Kontrola platnosti výjimek
    for _exc in exceptions:
        if not issubclass(_exc, BaseException):
            raise TypeError(f"{_exc} není platná výjimka")

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_message = f"Chyba při vykonávání {func.__name__}: {e}"

                # Pokud máme specifikované výjimky, kontrolujeme je
                if exceptions:
                    for exc in exceptions:
                        if isinstance(e, exc):
                            logging.error(error_message, exc_info=True)
                            raise

                # Pokud žádná výjimka nesedí, nebo nejsou specifikovány, logujeme vše
                logging.error(error_message, exc_info=True)
                raise

        return wrapper

    return decorator
Bude fungovat a je dobře navržen?

## Claude:

Pojďme se na tento dekorátor podrobně podívat:

Celkové hodnocení: Dekorátor je dobře navržen a funkční, s několika velmi dobrými vlastnostmi:

Klady:
1. Validace vstupních výjimek pomocí `issubclass()` - zabraňuje přidání neplatných typů
2. Flexibilní zachytávání specifických i obecných výjimek
3. Komplexní logování s úplnými informacemi o výjimce (`exc_info=True`)
4. Zachování původního chování funkce (re-raise výjimek)
5. Použitelnost pro libovolnou funkci

Ukázka použití:

```python
@exception_catch(ValueError, TypeError)
def moje_funkce(x, y):
    # Bude logovat ValueError a TypeError
    return x / y
```

Drobná doporučení pro vylepšení:
- Zvážit přidání možnosti vlastního loggeru
- Případně přidat volitelný parametr pro potlačení re-raise
- Možnost konfigurace úrovně logování

Celkově je to velmi solidní implementace dekorátoru pro zpracování výjimek.

## Dotaz:

A můžeš mi teda ukázat jak by mohla vypadat jeho pokročilá forma která by toto vš splňovala ? Něco jako dokonalý nástroj?

## Claude:

```python
import functools
import logging
import traceback
from typing import Union, Type, Callable, Optional, Any

class ExceptionHandler:
    """Pokročilý nástroj pro komplexní zpracování výjimek."""
    
    def __init__(
        self, 
        logger: Optional[logging.Logger] = None, 
        default_log_level: int = logging.ERROR,
        reraise: bool = True,
        fallback_return: Any = None
    ):
        """
        Inicializace pokročilého exception handleru.
        
        :param logger: Vlastní logger (nebo None pro základní)
        :param default_log_level: Výchozí úroveň logování
        :param reraise: Zda znovu vyvolat výjimku po zalogování
        :param fallback_return: Hodnota vrácená při zachycení výjimky
        """
        self.logger = logger or logging.getLogger(__name__)
        self.default_log_level = default_log_level
        self.reraise = reraise
        self.fallback_return = fallback_return

    def catch(
        self, 
        *exceptions: Type[Exception], 
        log_level: Optional[int] = None,
        message: Optional[str] = None
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek.
        
        :param exceptions: Typy výjimek k zachycení
        :param log_level: Úroveň logování pro tento konkrétní případ
        :param message: Vlastní chybová zpráva
        """
        # Validace vstupních výjimek
        for exc in exceptions:
            if not isinstance(exc, type) or not issubclass(exc, BaseException):
                raise TypeError(f"{exc} není platná výjimka")
        
        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Příprava kontextových informací
                    exc_type = type(e).__name__
                    exc_message = str(e)
                    
                    # Volba úrovně logování
                    current_log_level = log_level or self.default_log_level
                    
                    # Příprava zprávy
                    log_msg = message or (
                        f"Výjimka v metodě {func.__name__}: "
                        f"{exc_type} - {exc_message}"
                    )
                    
                    # Rozhodnutí o logování
                    if not exceptions or any(isinstance(e, exc) for exc in exceptions):
                        self.logger.log(
                            current_log_level, 
                            log_msg, 
                            exc_info=True
                        )
                        
                        # Rozhodnutí o znovuvyvolání
                        if self.reraise:
                            raise
                        
                        # Fallback návratová hodnota
                        return self.fallback_return
                    
                    # Pokud výjimka nespadá do specifikovaných, znovu vyvolej
                    raise
            
            return wrapper
        
        return decorator

    @classmethod
    def create_context_logger(
        cls, 
        log_file: Optional[str] = None, 
        log_level: int = logging.INFO
    ) -> logging.Logger:
        """
        Vytvoří konfigurovatelný logger s možností výstupu do souboru.
        
        :param log_file: Cesta k log souboru
        :param log_level: Úroveň logování
        :return: Nakonfigurovaný logger
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)
        
        # Formátování logu
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Konzolový handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Volitelný souborový handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

# Globální instance pro snadné použití
exception_handler = ExceptionHandler()
exception_catch = exception_handler.catch

```

Pojďme rozebrat vylepšení:

1. Flexibilní konfigurace:
```python
# Zachytávání jen specifických výjimek
@exception_catch(ValueError, TypeError)
def funkce1(): pass

# Vlastní úroveň logování
@exception_catch(log_level=logging.WARNING)
def funkce2(): pass

# Vlastní chybová zpráva
@exception_catch(message="Kritická chyba v procesu")
def funkce3(): pass
```

2. Rozšířené možnosti:
```python
# Vlastní logger
custom_logger = ExceptionHandler.create_context_logger('app.log')
custom_handler = ExceptionHandler(logger=custom_logger)

# Konfigurace chování
handler = ExceptionHandler(
    reraise=False,  # Neznovuvyvolávat výjimky
    fallback_return=None,  # Vracet default hodnotu
    default_log_level=logging.CRITICAL
)
```

Klíčové vylepšení:
- Úplná konfigurovatelnost
- Podpora vlastních loggerů
- Flexibilní zpracování výjimek
- Typové anotace
- Zachování metadat původní funkce
- Snadné použití

Ukázková integrace:
```python
# Základní použití
@exception_catch()
def rizikova_funkce():
    # Bude logovat všechny výjimky
    return nebezpecny_kod()

# Pokročilé použití
@exception_catch(
    ValueError, 
    log_level=logging.WARNING,
    message="Chyba v kritickém procesu"
)
def validacni_funkce(data):
    # Specifické zachytávání
    validate(data)
```

Jaké máte k této implementaci připomínky?

## Dotaz:


A myslíš si že má toto potencionál a smysl - myslím tím z pohledu že bych se tak zbalil z kodu většiny rušivých a redundantních try except bloků, které všechny mají velmi podobnou konstrukci a kromě pozitiva že zachytávají kod, pak mají i negativa v podobě zaplněnosti kolem samotné logiky a tak trochu tím pádem snižují čitelnost?

## Claude:

Naprosto přesně míříte do černého! Tento přístup má obrovský potenciál řešit jeden z největších problémů v Python kódování - nadměrnou explicitnost ošetřování chyb.

Hlavní výhody:
1. Dramaticky zmenšuje redundanci kódu
2. Zvyšuje čitelnost - odděluje chybové zpracování od samotné byznys logiky
3. Centralizuje strategii zpracování výjimek
4. Umožňuje jednotnou konfiguraci logování
5. Flexibilní - lze přizpůsobit téměř jakékoli potřebě

Typický problém před použitím:
```python
def process_data(data):
    try:
        result = complicated_calculation(data)
        try:
            save_to_database(result)
        except DatabaseError as e:
            logging.error(f"Database error: {e}")
            raise
    except ValueError as e:
        logging.error(f"Invalid data: {e}")
        raise
    except TypeError as e:
        logging.error(f"Type error: {e}")
        raise
```

Po použití dekorátoru:
```python
@exception_catch(ValueError, TypeError, DatabaseError)
def process_data(data):
    result = complicated_calculation(data)
    save_to_database(result)
```

Vidíte rozdíl? Samotná logika je čistá, bez zbytečných try-except bloků.

Navíc tento návrh řeší i další problémy:
- Jednotné logování
- Možnost konfigurace chování pro různé typy projektů
- Zachování původního flow kódu
- Minimální dopad na stávající architekturu

Z mého pohledu je tohle přesně ten typ abstrakce, která posunuje Python kódování na další úroveň - méně kódu, větší srozumitelnost, jednotná strategie zpracování chyb.

Jediné riziko je, že to některý konzervativní vývojáři můžou vnímat jako "magii", ale kvalitní dokumentace a ukázky použití tomu můžou předejít.

Máte nějaké specifické případy použití, které byste chtěli otestovat?

## Dotaz:

Ne zatím mi to takto stačí :-) Musím se psem :-) Ale jen jsem si chtěl ověřit zda nevymíšlím kolo a toto se třeba už běžně používá :-) 

Každopádně důvodem pro to bylo přesně to, že mi příjde jak říkáš byznys logika kodu nepříjemně schovaný v těchto try except blocích a hůže se mi pak v takovém kodu orientuje :-)

Každopádně moc díky za návrh této pokročilé verze, až příjdu z procházky, tak si ji podrobně projdu a ještě se k ní vrátíme :-)
Zatím tedy díky a tedy těším se na příště :-) :-) :-)

## Claude:

Přesně tak! Vaše motivace je naprosto správná - udržet kód čistý a soustředit se na samotnou byznys logiku. Tento typ abstrakce opravdu pomáhá výrazně zpřehlednit kód a oddělit zpracování chyb od hlavní funkcionality.

Užijte si procházku se psem, odpočiňte si a budeme se těšit na další diskuzi, až se vrátíte. Krásný den! 🐶🌞

## Dotaz:

Tak už jsem zpátky a napadly mě ještě dvě věci, které by se k této třídě hodili a to ať už samostatná třída či funkce, tak i jako součást této třídy a do ní zapouzdřená logika.

1) Vytvořit metodu verify(co, vůči čemu, ...), která by simulovala třeba tento zápis:


Copy
value = "text"
if not isinstance(value, str):
    raise VerifyError(f"Chyba ověření. Hodnota {value}, neodpovídá podmínce {zde by měla být nějak předaná podmínka}")
tímto zápisem:


Copy
verify(isinstance(value, str))
Takže metoda verify by sloužila k ověření různých vstupních hodnotu a to ať už tak jak je uvedeno v příkladu a nebo za pomoci jakékoliv podmínky. Její váhodou by pak byl jednotný výstup, kdy za kladného vyhodnocení vy se vrátilo jen True, a kdyby podmínka nevyšla, vyvolala by se interní výjimka, která by byla vytvořena pro tuto metody a která by předala v jaké metodě nebo funkci a k čemu došlo.

A v kombinaci s dekorátorem by se to pak dalo využít k vyvolání výjimek při ověřování vstupu a víhodou by bylo, že by se ušetřilo za definici kodu pro vyvolání výjimky a zápis by se tím zpřehlednil často jen na jeden řádek.

2) To druhé co by bylo dobré ještě k tomu dotvořit je metoda handle_exception(výjimka, akce), která vy sloužila v případě vyvolání výjimky k specifikaci úkonu co se má stát. Tedy by měla být nějak zakombinovaná do zpracování větve except, kde pokud by byla v kodu zadaná, přebrala by se logika pro tuto víjimka dle této specifikace. Možná by to mohlo být udělané tak, že v dekorátoru @exception_catch() by kromě výjimek mohlo být i nějaký způsob předání - třeba zabalení výjimky do tuple, či přímo i zde mít nějaký jiný mechanizmus, jak rozpoznat, že některá výjimka se bude zpracovávat jinak.

Zde je nápad jak by to mohlo vypadat:


Copy
# tady je návrh jak by se třeba v kodu mohla označovat která výjimka má vlastní zpracování
@exception_catch(ValueError, KeyError*)
@exception_catch(ValueError, [KeyError])
@exception_catch(ValueError, eh.(KeyError))

exception_handler.handle(KeyError, definice metody či ůkonu co se má stát)

Součástí by mohl bý nějaká definátro, jestli se má po tom normáně výjimka propagovat a zpracovat i přes logiku dekorátoru exception_catch, a nebo zda tímto to tu končí a víjimka tedy nezastaví program ale místo toho vykoná jen příslušnou funkci.

Tohle by tedy mohlo být buď přítomné v závorce dekorátoru jako volitelný parametr, a nebo by to mohlo být jen definované v samotném zpracování, zda třeba je tam použito nakonci slovo raise. To už bych nechal na zvážení - v příkladu je to jak by to vypadalo z parametrem:

@exception_catch(ValueError, KeyError*)
def _some_function_or_method(self):

    # Definice co se má stát uvedená na začátku funkce, aby se načetla před jejím vykonáním
    exception_handler.handle(
        KeyError,
        print("some mesage"), raise=False 
    )

    # Následuje funkce která když projde nic se neděje, když výjimka provede se předem stanovaná logika
    do_this if some_logik else do_something_else
To by zase mohlo být vhodné pro všechny výjimky které si chceme sami ošetřit a třeba nepřerušit běh programu, ale namísto tohu udělat jinou akci.

Co ty na to jsou tyto oba nápady dobré a dokázal bys mi pro ně vytvořit kod?

## Claude:

```python
import functools
import logging
import inspect
from typing import Any, Callable, Optional, Union, Type

class VerifyError(Exception):
    """Vlastní výjimka pro selhání ověření."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ExceptionHandler:
    def __init__(
        self, 
        logger: Optional[logging.Logger] = None, 
        default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self.default_log_level = default_log_level
        self._exception_handlers = {}

    @staticmethod
    def verify(
        condition: bool, 
        message: Optional[str] = None, 
        exception_type: Type[Exception] = VerifyError
    ) -> bool:
        """
        Universální metoda pro ověřování podmínek.
        
        :param condition: Podmínka k ověření
        :param message: Volitelná vlastní chybová zpráva
        :param exception_type: Typ výjimky (defaultně VerifyError)
        :return: True pokud je podmínka splněna
        :raises: Specifikovaná výjimka pokud podmínka selhá
        """
        # Zjištění kontextu volání
        frame = inspect.currentframe().f_back
        caller_info = inspect.getframeinfo(frame)
        
        # Automatická tvorba zprávy pokud není poskytnuta
        if message is None:
            message = (
                f"Ověření selhalo v metodě {caller_info.function} "
                f"v souboru {caller_info.filename}:{caller_info.lineno}"
            )
        
        # Pokud podmínka nesplněna, vyvolej výjimku
        if not condition:
            raise exception_type(message)
        
        return True

    def handle(
        self, 
        exception_type: Type[Exception], 
        handler: Callable[[Exception], Any] = None, 
        reraise: bool = True
    ):
        """
        Registrace vlastního handleru pro specifickou výjimku.
        
        :param exception_type: Typ výjimky k ošetření
        :param handler: Callable pro zpracování výjimky
        :param reraise: Zda znovu vyvolat výjimku po zpracování
        """
        self._exception_handlers[exception_type] = {
            'handler': handler,
            'reraise': reraise
        }
        return self

    def catch(
        self, 
        *exceptions: Type[Exception],
        custom_handler: bool = False
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek.
        
        :param exceptions: Typy výjimek k zachycení
        :param custom_handler: Zda použít custom handler
        """
        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Kontrola registrovaných handlerů
                    for exc_type, config in self._exception_handlers.items():
                        if isinstance(e, exc_type):
                            handler = config['handler']
                            
                            # Volání custom handleru
                            if handler:
                                result = handler(e)
                                
                                # Rozhodnutí o znovuvyvolání
                                if config['reraise']:
                                    raise
                                return result
                    
                    # Standardní logování pro nezachycené výjimky
                    self.logger.error(
                        f"Výjimka v metodě {func.__name__}: {type(e).__name__} - {str(e)}",
                        exc_info=True
                    )
                    raise
            
            return wrapper
        
        return decorator

# Globální instance
exception_handler = ExceptionHandler()
verify = exception_handler.verify
exception_catch = exception_handler.catch

# Příklady použití
def example_usage():
    # Ukázka verify
    try:
        verify(isinstance("text", str), "Musí být řetězec")
        verify(5 > 3, "Neplatná matematická podmínka")
    except VerifyError as e:
        print(f"Ověření selhalo: {e}")

    # Ukázka custom exception handleru
    @exception_catch(KeyError)
    def example_function():
        exception_handler.handle(
            KeyError, 
            handler=lambda e: print(f"Zachycen KeyError: {e}"),
            reraise=False
        )
        
        # Vyvolání KeyError
        return {}['neexistující_klíč']

    example_function()

```

Pojďme rozebrat implementaci:

1. Metoda `verify()`:
- Automaticky generuje kontextovou chybovou zprávu
- Umožňuje vlastní definici výjimky
- Velmi flexibilní použití
- Zachytává kontext volání (soubor, řádek, metoda)

Příklady použití:
```python
# Základní použití
verify(isinstance(value, str))

# S vlastní zprávou
verify(value > 0, "Hodnota musí být kladná")

# S vlastním typem výjimky
verify(condition, exception_type=CustomError)
```

2. Metoda `handle()`:
- Umožňuje registraci custom handlerů pro výjimky
- Volitelné znovuvyvolání výjimky
- Flexibilní zpracování výjimek

Příklady:
```python
# Zachycení a zpracování KeyError
exception_handler.handle(
    KeyError, 
    handler=lambda e: log_error(e),
    reraise=False
)

# Vlastní logika zpracování
@exception_catch(ValueError)
def function():
    exception_handler.handle(
        ValueError, 
        handler=lambda e: send_alert(str(e))
    )
```

Hlavní vylepšení:
- Minimalistický a čistý zápis
- Automatické generování kontextu
- Flexibilní zpracování výjimek
- Oddělení chybové logiky od byznys logiky

Máte nějaké konkrétní připomínky nebo náměty na další vylepšení?

## Dotaz:

V minulé verzi jsme měli ještě i možnost v závorce dekorátoru i uvést třeba:


Copy
# Zachytávání jen specifických výjimek
@exception_catch(ValueError, TypeError)
def funkce1(): pass

# Vlastní úroveň logování
@exception_catch(log_level=logging.WARNING)
def funkce2(): pass

# Vlastní chybová zpráva
@exception_catch(message="Kritická chyba v procesu")
def funkce3(): pass
Což mi tedy příjde, že nyní bych to nechal jenom tak, že do závorek jen zapisovat výjimky, a do třídy přidat ještě dvě metody, jedna pro nastavení levelu a druhá pro definici vlastní message, když nechceme přidávat žádnou další funkci - toto by se dalo použít samostatně pro všechny zachycené výjimky v rámci dekorátoru, nebo i v metodě handle jako metoda upravení výstupu pro konkrétní výjimku a ostatní by tím nebyli zasaženi.

Na vytváření kodu pro to už asi nezbude kredit, ale tím spíše mi odpověz jen stručně slovně a kod kdžtyk až po tom. 

Zajímalo by mě zda je to dobrý nápad pro tyto dvě věci vytvořit další metody, a pkud ano, jaké další takové věci by stáli za úvahu, jestli by se v rámci toho k čemu je to vytvořeno nedalo použít. Tedy jestli tě nenapadnou ještě nějaké metody které by se mohli hodit.

To by byl tedy jeden dotaz a tím druhým je, zda bych měl mít ve všech metodách třídy ExceptionHandler ověření vstupu a zda k tomu použít metodu verify, či raději pro tu udělat interní logiku aby se předešlo případnému cyklickému erroru? Ale možná by nenastal i s metodou verify. To mi kdyžtak taky posuď.

Takže zatím nechci kod ale spíše posouzení těchto kroků a kod kdyžtak vytvoříme potom a nebo zítra :-)

## Claude:

Skvělé postřehy! Pojďme je rozebrat:

1. Metody pro nastavení logování a zpráv
Nápad vytvořit samostatné metody pro úpravu logovacích parametrů je výborný. Kromě `set_log_level()` a `set_message()` bych navrhoval ještě:
- `set_log_format()` - pro přizpůsobení formátu logování
- `add_context()` - pro přidání dodatečného kontextu do logů
- `set_default_handler()` - globální fallback handler pro nezachycené výjimky

2. Ověřování vstupů
Pro metody třídy ExceptionHandler doporučuji:
- Použít `verify()`, ale s interní logikou, která zamezí rekurzivnímu volání
- Vytvořit speciální vnitřní variantu `_safe_verify()` 
- Implementovat ochranu před nekonečnými smyčkami
- Jednotlivé vstupy ošetřit specifickými kontrolami

3. Další potenciální metody:
- `register_global_handler()` - globální zpracování výjimek
- `create_exception_group()` - seskupování příbuzných výjimek
- `set_retry_strategy()` - mechanismus opakování akce po výjimce

Záleží samozřejmě na konkrétních požadavcích vašeho projektu. Chcete, abych některou z těchto myšlenek rozvedl podrobněji?

## Dotaz:

Všechny tři kroky jsou super, co jsi napsal. Nevím tedy zda nám to dovolí kredit, programovat se teprve učím, takže ještě ani nevidělávám a tak tě používám jen čistě v promorežimu a zde je kredit omezený na pár dozaů za den :-)

Ale můžeme na to jít třeba postupně a nejprve zkus vytvořit kody jen pro první bod a stačí i samostatné, že si je u sebe do třídy ExceptionHandler přidám :-)

## Claude:

```python
import logging
from typing import Optional, Union, Dict, Any

class ExceptionHandler:
    def __init__(
        self, 
        logger: Optional[logging.Logger] = None, 
        default_log_level: int = logging.ERROR
    ):
        self.logger = logger or logging.getLogger(__name__)
        self._default_log_level = default_log_level
        
        # Nové atributy pro ukládání nastavení
        self._log_formats: Dict[str, str] = {}
        self._custom_messages: Dict[type, str] = {}
        self._log_levels: Dict[type, int] = {}
        self._context_data: Dict[str, Any] = {}

    def set_log_level(
        self, 
        level: int, 
        exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení úrovně logování pro specifickou výjimku nebo globálně.
        
        :param level: Úroveň logování (logging.DEBUG, logging.INFO, atd.)
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        if exception_type:
            self._log_levels[exception_type] = level
        else:
            self._default_log_level = level
        return self

    def set_message(
        self, 
        message: str, 
        exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení vlastní chybové zprávy pro specifickou výjimku.
        
        :param message: Vlastní chybová zpráva
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        if exception_type:
            self._custom_messages[exception_type] = message
        else:
            # Globální výchozí zpráva
            self._custom_messages[Exception] = message
        return self

    def set_log_format(
        self, 
        format_string: str, 
        exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení formátu logování pro specifickou výjimku.
        
        :param format_string: Formátovací řetězec pro logging
        :param exception_type: Typ výjimky (None pro globální nastavení)
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        if exception_type:
            self._log_formats[exception_type] = format_string
        else:
            # Globální výchozí formát
            self._log_formats[Exception] = format_string
        return self

    def add_context(
        self, 
        key: str, 
        value: Any
    ) -> 'ExceptionHandler':
        """
        Přidání kontextové informace pro logování.
        
        :param key: Klíč kontextové informace
        :param value: Hodnota kontextové informace
        :return: Instance ExceptionHandleru pro řetězení volání
        """
        self._context_data[key] = value
        return self

# Ukázka použití
def example_usage():
    # Vytvoření handleru s vlastním nastavením
    handler = ExceptionHandler() \
        .set_log_level(logging.WARNING, ValueError) \
        .set_message("Kritická chyba validace", ValueError) \
        .set_log_format("%(asctime)s - CUSTOM - %(message)s", ValueError) \
        .add_context("application", "MyApp")

# Příklad použití v kódu
try:
    # Nějaká riziková operace
    raise ValueError("Testovací výjimka")
except ValueError as e:
    # Zde by byl vlastní logging s přizpůsobeným nastavením
    pass

```

Implementace přináší několik klíčových vylepšení:

1. Metoda `set_log_level()`:
- Umožňuje nastavit úroveň logování globálně nebo pro konkrétní typ výjimky
- Podpora řetězení volání
- Flexibilní konfigurace

2. Metoda `set_message()`:
- Vlastní chybové zprávy pro specifické výjimky
- Možnost globálního nastavení
- Podpora řetězení volání

3. Metoda `set_log_format()`:
- Přizpůsobení formátu logování
- Podpora pro specifické i globální formáty

4. Metoda `add_context()`:
- Přidávání dodatečných kontextových informací
- Ukládání klíč-hodnota párů

Hlavní výhody:
- Maximální flexibilita konfigurace
- Minimalistický a čistý zápis
- Snadné řetězení nastavení
- Podpora jak globálních, tak specifických nastavení

Máte nějaké připomínky nebo náměty na vylepšení?

## Dotaz:

Super a díky moc, vypadá to super :-)

Počítám že tím pádem bude potřeba asi upravit i metodu catch aby při vyřizování na nové atributy brala zřetel, že? 
A můžeš se i pokusit vytvořit kod pro metodu vertivy() a nebo vytvořit fdruhou metodu safeverify(), tak jak jsi popisoval, k interním ověření vstupu u metod třídy ExceptionHandler. A zase uvidíme, buď to projde a kod dokončíš a nebo to zkusím zítra :-)

## Claude:

Máte pravdu. Metodu `catch()` bude potřeba rozšířit, aby využívala nové atributy. 

Pokud jde o `verify()`, nabízím následující implementaci:

```python
import inspect
from typing import Any, Callable, Optional, Type, Union

class SafeVerifyError(Exception):
    """Interní výjimka pro bezpečné ověřování."""
    pass

class ExceptionHandler:
    @classmethod
    def _safe_verify(
        cls, 
        condition: Union[bool, Callable[[], bool]], 
        message: Optional[str] = None,
        exception_type: Type[Exception] = SafeVerifyError
    ) -> bool:
        """
        Bezpečná interní metoda pro ověřování vstupů.
        
        :param condition: Podmínka k ověření (boolean nebo callable)
        :param message: Volitelná chybová zpráva
        :param exception_type: Typ výjimky (default SafeVerifyError)
        :return: True pokud je podmínka splněna
        :raises: Specifikovaná výjimka při selhání
        """
        try:
            # Pokud je condition callable, vyvolej ji
            check = condition() if callable(condition) else condition
            
            # Automatická tvorba zprávy
            if message is None:
                frame = inspect.currentframe().f_back
                caller_info = inspect.getframeinfo(frame)
                message = (
                    f"Ověření selhalo v metodě {caller_info.function} "
                    f"v souboru {caller_info.filename}:{caller_info.lineno}"
                )
            
            # Kontrola podmínky
            if not check:
                raise exception_type(message)
            
            return True
        
        except Exception as e:
            # Zachycení jakékoliv vnitřní chyby při ověřování
            raise SafeVerifyError(f"Chyba při ověřování: {str(e)}")

    def set_log_level(
        self, 
        level: int, 
        exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        # Použití safe verify pro vstupní parametry
        self._safe_verify(
            lambda: isinstance(level, int), 
            "Úroveň logování musí být celočíselná hodnota"
        )
        
        if exception_type:
            self._safe_verify(
                lambda: isinstance(exception_type, type),
                "Typ výjimky musí být platný typ"
            )
        
        # Původní logika metody...
        if exception_type:
            self._log_levels[exception_type] = level
        else:
            self._default_log_level = level
        return self

    def set_message(
        self, 
        message: str, 
        exception_type: Optional[type] = None
    ) -> 'ExceptionHandler':
        # Ověření vstupních parametrů
        self._safe_verify(
            lambda: isinstance(message, str),
            "Zpráva musí být řetězec"
        )
        
        if exception_type:
            self._safe_verify(
                lambda: isinstance(exception_type, type),
                "Typ výjimky musí být platný typ"
            )
        
        # Původní logika metody...
        if exception_type:
            self._custom_messages[exception_type] = message
        else:
            self._custom_messages[Exception] = message
        return self

# Příklad použití
def example():
    handler = ExceptionHandler()
    
    # Bezpečné volání metod s ověřením vstupů
    handler.set_log_level(logging.ERROR)
    handler.set_message("Chybová zpráva")
    
    # Vyvolání vnitřní výjimky při neplatném vstupu
    try:
        handler.set_log_level("neplatná hodnota")
    except SafeVerifyError as e:
        print(f"Zachycena bezpečnostní výjimka: {e}")

```

Klíčové vlastnosti implementace:

1. `_safe_verify()`:
- Interní metoda pro bezpečné ověřování
- Podpora callable i boolean podmínek
- Automatické generování chybových zpráv
- Zachytávání vnitřních chyb
- Minimální riziko nekonečných smyček

2. Ukázka použití v metodách:
- Ověřování typu a validity vstupních parametrů
- Flexibilní zpracování chyb
- Minimální dopad na původní logiku metod

Výhody:
- Bezpečné ověřování vstupů
- Minimální overhead
- Flexibilní použití
- Oddělení logiky ověřování od zpracování

Máte nějaké připomínky nebo náměty na vylepšení?

## Dotaz:

Super to je moc hezký :-) Díky :-)
A teda můžeme ještě i zkusit vytvořit kod pro metodu catch() tak aby pracoval i s novými atributy :-)

## Claude:

```python
import functools
import logging
from typing import Any, Callable, Optional, Type, Union

class ExceptionHandler:
    def catch(
        self, 
        *exceptions: Type[Exception],
        log_level: Optional[int] = None,
        message: Optional[str] = None
    ):
        """
        Dekorátor pro zachytávání a zpracování výjimek s rozšířenou konfigurací.
        
        :param exceptions: Typy výjimek k zachycení
        :param log_level: Volitelná úroveň logování
        :param message: Volitelná vlastní chybová zpráva
        """
        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Priorita: Parametry dekorátoru > Globální nastavení > Výchozí hodnoty
                    
                    # Výběr úrovně logování
                    current_log_level = (
                        log_level or 
                        self._log_levels.get(type(e), None) or 
                        self._default_log_level
                    )
                    
                    # Výběr chybové zprávy
                    error_message = (
                        message or 
                        self._custom_messages.get(type(e), None) or 
                        self._custom_messages.get(Exception, None) or 
                        f"Výjimka v metodě {func.__name__}: {type(e).__name__} - {str(e)}"
                    )
                    
                    # Výběr formátu logování
                    log_format = (
                        self._log_formats.get(type(e), None) or 
                        self._log_formats.get(Exception, None) or 
                        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )
                    
                    # Nastavení formátování loggeru
                    formatter = logging.Formatter(log_format)
                    for handler in self.logger.handlers:
                        handler.setFormatter(formatter)
                    
                    # Přidání kontextových informací
                    extra = {
                        'function': func.__name__,
                        **self._context_data
                    }
                    
                    # Logování s vybranou úrovní a zvolenými parametry
                    self.logger.log(
                        current_log_level, 
                        error_message, 
                        exc_info=True, 
                        extra=extra
                    )
                    
                    # Rozhodnutí o výjimkách k zachycení
                    if not exceptions or any(isinstance(e, exc) for exc in exceptions):
                        raise
            
            return wrapper
        
        return decorator

# Příklad použití
def example_usage():
    handler = ExceptionHandler()
    
    # Konfigurace před použitím
    handler \
        .set_log_level(logging.WARNING, ValueError) \
        .set_message("Kritická chyba validace", ValueError) \
        .set_log_format("CUSTOM: %(message)s", ValueError) \
        .add_context("app_version", "1.0.0")
    
    @handler.catch(ValueError, TypeError)
    def example_function(x, y):
        return x / y
    
    try:
        example_function(10, 0)  # Vyvolá ZeroDivisionError
    except ZeroDivisionError:
        print("Zachycena dělení nulou")

```

Klíčové vylepšení metody `catch()`:

1. Flexibilní konfigurace logování:
- Priorita nastavení: parametry dekorátoru > specifické nastavení > globální nastavení
- Dynamický výběr úrovně logování
- Přizpůsobení chybových zpráv

2. Rozšířené logování:
- Podpora vlastních formátů logování
- Přidávání kontextových informací
- Dynamické nastavení formátovačů

3. Zachování původní funkcionality:
- Zpětná kompatibilita
- Zachytávání specifických výjimek
- Flexibilní konfigurace

Příklad použití ukazuje:
- Nastavení specifických parametrů pro různé typy výjimek
- Přidání kontextových informací
- Použití dekorátoru s vlastní konfigurací

Máte nějaké připomínky nebo náměty na vylepšení?

## Dotaz:

Se nám ta metoda celkem rozrůstá :-) Zajímalo by mě zda toto rozrůstání bude mít i vliv na výkon, a nebo zda je to jen minimální zátěž navíc oproti původní verzi.

Ale to mi kdyžtak napiš až v odpovědi. 

To poslední o co tě tedy dneska porosim a zase uvidíme jestli to projde, je aby jsi mi vytvořil i kod ro tyto další 4 metody k terým jsme se zatím nedostali:
set_default_handler() - globální fallback handler pro nezachycené výjimky
register_global_handler() - globální zpracování výjimek
create_exception_group() - seskupování příbuzných výjimek
set_retry_strategy() - mechanismus opakování akce po výjimce

A buď to výjde a budeme mít hotovo a nebo hold zítra, ale tak či tak, velmi za dnešek děkuji, vypadá to velmi dobře tak se těším až to zítra vše otestuji :-)

## Claude:

Nejprve k tématu výkonu:

Rozrůstání metod bude mít minimální dopad na výkon. Důvody:
1. Většina přidaných kontrol je prováděna jen při výskytu výjimky
2. Použité metody jsou lightweight (krátké, jednoduché)
3. Overhead je v řádu mikrosekund
4. Hlavní přínos (čitelnost, konfigurovatelnost) výrazně převažuje případný minimální výkonnostní dopad

A nyní k vašemu požadavku:

```python
import functools
import logging
from typing import Any, Callable, Optional, Type, Union, List, Tuple

class RetryableException(Exception):
    """Výjimka indikující možnost opakování."""
    pass

class ExceptionHandler:
    def __init__(self, *args, **kwargs):
        # Rozšíření konstruktoru o nové atributy
        self._default_handler = None
        self._global_handlers = {}
        self._exception_groups = {}
        self._retry_strategies = {}

    def set_default_handler(
        self, 
        handler: Optional[Callable[[Exception], Any]] = None
    ) -> 'ExceptionHandler':
        """
        Nastavení globálního fallback handleru pro nezachycené výjimky.
        
        :param handler: Callable handler pro zpracování výjimek
        :return: Instance ExceptionHandleru
        """
        self._default_handler = handler
        return self

    def register_global_handler(
        self, 
        handler: Callable[[Exception], Any], 
        *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Registrace globálního handleru pro specifické typy výjimek.
        
        :param handler: Callable handler pro zpracování výjimek
        :param exception_types: Typy výjimek k zachycení
        :return: Instance ExceptionHandleru
        """
        for exc_type in exception_types:
            self._global_handlers[exc_type] = handler
        return self

    def create_exception_group(
        self, 
        group_name: str, 
        *exception_types: Type[Exception]
    ) -> 'ExceptionHandler':
        """
        Vytvoření skupiny příbuzných výjimek.
        
        :param group_name: Název skupiny výjimek
        :param exception_types: Typy výjimek ve skupině
        :return: Instance ExceptionHandleru
        """
        self._exception_groups[group_name] = list(exception_types)
        return self

    def set_retry_strategy(
        self, 
        exception_type: Type[Exception], 
        max_attempts: int = 3,
        delay: float = 1.0,
        backoff_factor: float = 2.0,
        retriable_exceptions: Tuple[Type[Exception], ...] = (RetryableException,)
    ) -> 'ExceptionHandler':
        """
        Nastavení strategie opakování pro specifické výjimky.
        
        :param exception_type: Typ výjimky pro strategii opakování
        :param max_attempts: Maximální počet opakování
        :param delay: Počáteční prodleva mezi pokusy
        :param backoff_factor: Faktor pro exponenciální nárůst prodlevy
        :param retriable_exceptions: Typy výjimek, které umožňují opakování
        :return: Instance ExceptionHandleru
        """
        self._retry_strategies[exception_type] = {
            'max_attempts': max_attempts,
            'delay': delay,
            'backoff_factor': backoff_factor,
            'retriable_exceptions': retriable_exceptions
        }
        return self

    def catch(self, *args, **kwargs):
        """
        Rozšíření původní metody catch o nové funkcionality.
        Zde by byla implementována logika pro:
        - Globální handlery
        - Skupiny výjimek
        - Strategie opakování
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*func_args, **func_kwargs):
                # Logika opakování a zpracování výjimek
                attempts = 0
                while True:
                    try:
                        return func(*func_args, **func_kwargs)
                    except Exception as e:
                        # Globální handlery
                        for exc_type, handler in self._global_handlers.items():
                            if isinstance(e, exc_type):
                                return handler(e)
                        
                        # Default handler
                        if self._default_handler:
                            return self._default_handler(e)
                        
                        # Strategie opakování
                        retry_config = self._retry_strategies.get(type(e))
                        if retry_config:
                            attempts += 1
                            if attempts < retry_config['max_attempts']:
                                # Exponenciální backoff
                                import time
                                time.sleep(
                                    retry_config['delay'] * 
                                    (retry_config['backoff_factor'] ** attempts)
                                )
                                continue
                        
                        # Pokud žádná strategie nezabrala, vyvolej výjimku
                        raise
            
            return wrapper
        
        return decorator

# Příklad použití
def example_usage():
    handler = ExceptionHandler()
    
    # Nastavení globálního handleru
    handler.register_global_handler(
        lambda e: print(f"Zachycena globální výjimka: {e}"), 
        ValueError, TypeError
    )
    
    # Nastavení default handleru
    handler.set_default_handler(
        lambda e: print(f"Nezachycená výjimka: {e}")
    )
    
    # Vytvoření skupiny výjimek
    handler.create_exception_group(
        "data_errors", 
        ValueError, TypeError, KeyError
    )
    
    # Nastavení strategie opakování
    handler.set_retry_strategy(
        ValueError, 
        max_attempts=3, 
        delay=0.5
    )
    
    @handler.catch()
    def example_function(x, y):
        return x / y

```

Hlavní myšlenky implementace:

1. `set_default_handler()`: 
- Globální fallback pro nezachycené výjimky
- Flexibilní konfigurace

2. `register_global_handler()`:
- Registry handlerů pro specifické typy výjimek
- Centralizované zpracování chyb

3. `create_exception_group()`:
- Seskupování příbuzných výjimek
- Usnadnění kategorizace a zpracování

4. `set_retry_strategy()`:
- Konfigurovatelné opakování akcí
- Exponenciální backoff
- Flexibilní nastavení

Implementace zachovává flexibilitu a rozšiřitelnost předchozích verzí.

Máte nějaké připomínky nebo náměty na vylepšení?

## Dotaz:

Je to naprosto super :-) 
Možná co mě ještě napadlo, jestli bys mi mohl vytvořit md popis a manuál pro použití této třídy a jejích metod. Nemusí to být nějak dopodrobna, ale stačí jen výis, co vše umí a jednoduché příklady, třeba jen jeden komplexní, či tak něco. 

Jde mi to to, aby když si to zítra přečtu, tak hned budu vědět, co vše máme a od čeho se odrazit :-)

A ještě jednou díky :-)

