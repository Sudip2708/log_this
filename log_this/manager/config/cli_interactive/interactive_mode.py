from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

from .all_mixins import AllMixins
from log_this.manager.config import config


class InteractiveMode(AllMixins):
    """
    Třída pro správu interaktivního režimu konfigurace LogThis.

    Poskytuje uživatelské rozhraní pro:
    - Prohlížení a úpravu konfiguračních hodnot
    - Zobrazení nápovědy
    - Navigaci pomocí šipek a potvrzení entrem
    """

    def __init__(self):
        """
        Inicializace instance interaktivního režimu.
        """
        self.config_inst = config
        self.keys_data = config.keys_data
        self.session = PromptSession()

        # Definice stylů pro UI
        self.style = Style.from_dict({
            'dialog': 'bg:#4444aa #ffffff',
            'dialog.body': 'bg:#000000 #ffffff',
            'dialog.border': '#004400',
            'selected': 'bg:#ffffff #000000',
        })

