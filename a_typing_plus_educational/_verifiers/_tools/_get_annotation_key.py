"""
Doplnit docstring a zjistit zda je to optimální způsob
"""

def get_annotation_key(annotation) -> str:
    """Funkce pro převod anotace na klíč"""
    try:

        # Přřevod anotace na řetězec
        str_annotation = str(annotation)

        # Načtení indexu první hranaté otevřené závorky
        index = str_annotation.find('[')

        # Pokud závorka je nalezena
        if index != -1:

            # Ořízni text anotace po tuto závorku
            str_annotation = str_annotation[:index]

        # Navrácení řetězce převedeného na malá písmena a oříznutí prázdných znaků
        return str_annotation.lower().strip()

    # Zachycení všeobecné výjimky
    except Exception:

        # Navrácentí str typu anotace (nemělo by nastat)
        return str(type(annotation)).lower().strip()