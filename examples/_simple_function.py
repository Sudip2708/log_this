from typing import List
from log_this import log_this

def try_out_simple(log_level_1: int, log_level_2: int):
    """Demonstrační funkce pro ukázku různých úrovní logování.

    Args:
        log_level_1 (int): Úroveň logování pro první vnořenou funkci.
        log_level_2 (int): Úroveň logování pro druhou vnořenou funkci.

    Returns:
        int: Výsledek analýzy dat po aplikaci multiplikátoru.
    """

    @log_this(log_level_1)
    def test_function(data_points: List[int], multiplier: int = 1) -> int:
        """Testovací funkce s vnitřní logikou pro výpočet.

        Args:
            data_points (List[int]): Seznam datových bodů k analýze.
            multiplier (int, optional): Multiplikátor pro výpočet. Defaults to 1.

        Returns:
            int: Výsledek analýzy dat.
        """
        return analyze_data(data_points, multiplier)

    @log_this(log_level_2)
    def analyze_data(data_points: List[int], multiplier: int = 1) -> int:
        """Analyzuje dataset s vnitřní logikou a rozhodováním.

        Args:
            data_points (List[int]): Seznam datových bodů k analýze.
            multiplier (int, optional): Multiplikátor pro výpočet. Defaults to 1.

        Returns:
            int: Výsledek analýzy dat, nebo None pokud je vstupní seznam prázdný.
        """
        if not data_points:
            return None

        processed_data = [point * multiplier for point in data_points]
        return sum(processed_data)

    # Spuštění demonstrace s fixními hodnotami
    return test_function([10, 20, 30], 2)

