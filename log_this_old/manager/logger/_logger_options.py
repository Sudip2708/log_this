import logging

def get_formatter():
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