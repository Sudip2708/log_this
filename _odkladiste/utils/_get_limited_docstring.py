from typing import Union

def get_limited_docstring(docstring: str, max_lines: Union[int, str] = 3) -> str:
    """
    Vrátí zkrácenou verzi docstringu s maximálním počtem řádků.
    Prázdné řádky jsou vynechány.

    Args:
        docstring (str): Docstring, který se má oříznout.
        max_lines (Union[int, str]): Maximální počet řádků nebo 'all' pro zobrazení všech řádků.
            Pokud je 'all', funkce vrátí celý docstring.

    Returns:
        str: Oříznutý docstring.
    """

    # Pokud není docstring uveden
    if not docstring:
        return "N/A"

    if max_lines == 'all':
        return docstring

    # Rozdělení docstringu na jednotlivé řádky a odstranění prázdných
    lines = [line for line in docstring.strip().splitlines() if line.strip()]

    # Kontrola počtu řádků
    if len(lines) <= max_lines:
        return "\n".join(lines)

    # Vrácení odpovídajícího počtu řádků
    return "\n".join(lines[:max_lines]) + " (...)"