from typing import Union

class GetLimitedDocstringMixin:

    def get_limited_docstring(self, docstring: str) -> str:
        """
        Vrátí zkrácenou verzi docstringu s maximálním počtem řádků.

        Prázdné řádky jsou vynechány.

        Args:
            docstring (str): Docstring, který se má oříznout.

        Returns:
            str: Oříznutý docstring.
        """

        # Pokud není docstring uveden, nebo je zadaná špatná hodnota
        if not docstring or not isinstance(docstring, str):
            return "N/A"

        # Kontrola nastavení pro počet řádek
        max_lines = self.config["docstring_lines"]
        if max_lines == 'all':
            return docstring

        # Rozdělení docstringu na jednotlivé řádky a odstranění prázdných
        lines = [line for line in docstring.strip().splitlines() if line.strip()]

        # Kontrola počtu řádků
        if len(lines) <= max_lines:
            return "\n".join(lines)

        # Vrácení odpovídajícího počtu řádků
        return "\n".join(lines[:max_lines]) + " (...)"