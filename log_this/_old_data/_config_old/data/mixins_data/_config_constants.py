class ConfigConstants:
    "Třída reprezentující defaultní hodnoty"
    DEFAULT_CONFIG = {

        'skip_this': 0,  # Textová reprezentce pro mod 0
        'one_line': 1,  # Textová reprezentce pro mod 1
        'simple': 2,  # Textová reprezentce pro mod 2
        'detailed': 3,  # Textová reprezentce pro mod 3
        'report': 4,  # Textová reprezentce pro mod 4

        'true': 1,   # Další možnost zápisu pro mod 1
        'false': 0,   # Další možnost zápisu pro mod 0
        'none': 0,   # Další možnost zápisu pro mod 0
        'empty': 0,   # Prázdné závorky jako prostředek pro jakoukoliv hodnotu (defaultně 0)

        'indent': 2,  # Počet znaků pro odsazení od kraje při zanoření (0-4)
        'blank_lines': True,  # Zobrazení prázdného řádku mezi jednotlivými logy (True/False)
        'docstring_lines': 3,  # Počet řádků z docstringu pro report (int a nebo 'all' pro všechny)
        'max_depth': 100,  # Úroveň maximálního zanoření pro detekci cyklického vstupu

    }