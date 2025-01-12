# log_this/manager/config/cli/__init__.py
"""
log_this/manager/config/cli/
│
├── __init__.py                 # Exportuje hlavní funkci main()
├── _main.py                    # Hlavní funkce pro CLI
├── parsers/                    # Modul pro správu argumentů
│   ├── __init__.py
│   ├── _create_parser.py      # Vytvoření ArgumentParser
│   └── _validate_args.py      # Validace argumentů
├── handlers/                   # Modul pro zpracování příkazů
│   ├── __init__.py
│   ├── _config_handler.py     # Hlavní handler pro příkazy
│   └── _value_handler.py      # Zpracování a validace hodnot
└── utils/                      # Pomocné utility
    ├── __init__.py
    └── _logging.py            # Nastavení loggingu
"""
from ._main import main

__all__ = ['main']