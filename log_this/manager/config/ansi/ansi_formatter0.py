# file: ansi_formatter.py
from typing import Union, Optional
from ._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS



class StyleBuilder:

    def __init__(self, text, config_dict):
        if isinstance(text, str):
            self.text = text
        else:
            raise ValueError("paramter text není str")
        self._config_dict = config_dict
        self._ansi_codes = []

    def __str__(self):
        pass

    @property
    def prefix(self):
        if self._ansi_codes:
            ansi_codes = ';'.join(self._ansi_codes)
            return "\033[" + ansi_codes + "m"
        else:
            ""

    @property
    def reset(self):
        if self._ansi_codes:
            return "\033[0m"
        else:
            ""

    def manage_text(self):
        if self._ansi_codes:

            # Pokud text nemá žádné vnořené úpravy
            if "\033[" not in self.text:
                return self.prefix + self.text + self.reset

            # Pokud text má vnořené úpravy
            else:


        else:
            return text




    def set(self, *arg):
        if arg:
            for i in arg:
                if i in self._config_dict.key():
                    self._ansi_codes.append(self._config_dict[i])

        return self.manage_text()







class ANSIFormatter:
    """Class for formatting text with ANSI escape sequences."""

    _instance: Optional['ANSIFormatter'] = None
    ESCAPE = "\033["
    RESET = ESCAPE+"0m"

    def __new__(cls) -> 'ANSIFormatter':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Inicializace proběhne pouze jednou díky Singletonu
        if not hasattr(self, '_initialized'):
            self._config_dict = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
            self._builder = StyleBuilder
            self._initialized = True

    def style(self, text):
        return self._builder(text, self._config_dict)





