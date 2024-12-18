from ._log_one_line import log_one_line
from ._log_simple import log_simple
from ._log_detailed import log_detailed
from ._log_report import log_report
from ._mode_error import mode_error


__all__ = [
    "log_one_line",  # Nastavení pro logování do jednoho řádku
    "log_simple",  # Nastavení pro základní logování (4 řádky)
    "log_detailed",  # Nastavení pro výpis s více detaily (6 řádků)
    "log_report",  # Nastavení pro úplný výpis i výpisem paměti (10+ řádků)
    "mode_error",  # Výjimka pro neplatný mod
]

# """
# 1) Jednořádkový výpis:
# # INFO LogThis('one_line') | 2024-12-09 13:48:36.398274 | try_out_this | [10, 20, 30], 2
#
# 2) Simple:
# # START LogThis('simple') ↓ 2024-12-09 13:48:36.398274 ↓ try_out_this ↓
# # >>> Input parameters: [[10, 20, 30], 2]
# # >>> Outcome: 120
# # END LogThis('simple') ↑ try_out_this ↑
#
# 3) Detailed:
# # START LogThis('detailed') for try_out_this ↓ 2024-12-09 13:48:36.398274 ↓
# # >>> File: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
# # >>> Input parameters: [[10, 20, 30], 2] | Input kwords: {}
# # >>> Outcome: 120 | Type: int
# # >>> Running time: 0.000872 sec | Memory Usage: 640 bytes
# # END LogThis('detailed') for 'try_out_this' ↑ Log duration: 0.002551 sec ↑
#
# 4) Report
# # START LogThis('report') ↓ 2024-12-09 13:48:36.398274 ↓ try_out_this ↓
# # >>> File: C:\Users\Sudip2708\Desktop\planck_units\libraries\log_this\log_this\tests\_try_out_this.py
# # >>> Anotations: {'data_points': typing.List[int], 'multiplier': <class 'int'>, 'return': <class 'int'>}
# # >>> Input parameters: [[10, 20, 30], 2] | Input kwords: {}
# # >>> Docstring: N/A
# # >>> Outcome: 120 | Type: int
# # >>> Running time: 0.000872 sec | Memory Usage: 640 bytes
# # >>> Memory Allocation Listing:
# # >>> > Allocated: 320 bajtů, Line: 560, File: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
# # >>> > Allocated: 320 bajtů, Line: 423, File: C:\Users\Sudip2708\AppData\Local\Programs\Python\Python311\Lib\tracemalloc.py
# # END LogThis('all') ↑ 'try_out_this' ↑ Log duration: 0.002551 sec
# """