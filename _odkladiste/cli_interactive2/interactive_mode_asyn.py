from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from typing import Dict, Optional, Any, List, Tuple


class InteractiveMode:
    """
    Třída pro správu interaktivního režimu konfigurace LogThis.

    Poskytuje uživatelské rozhraní pro:
    - Prohlížení a úpravu konfiguračních hodnot
    - Zobrazení nápovědy
    - Navigaci pomocí šipek a potvrzení entrem
    """

    def __init__(self, config_instance):
        """
        Inicializace instance interaktivního režimu.

        Args:
            config_instance: Instance třídy LogThisConfig
        """
        self.config_inst = config_instance
        self.keys_data = config_instance.keys_data
        self.session = PromptSession()

        # Definice stylů pro UI
        self.style = Style.from_dict({
            'dialog': 'bg:#4444aa #ffffff',
            'dialog.body': 'bg:#000000 #ffffff',
            'dialog.border': '#004400',
            'selected': 'bg:#ffffff #000000',
        })

    async def start(self) -> None:
        """Spustí interaktivní režim a zobrazí hlavní menu."""
        print("\nVítejte v interaktivním režimu konfigurace LogThis!")

        while True:
            # Definice hlavního menu
            result = await self._show_main_menu()

            if result == 'exit':
                print("\nUkončuji interaktivní režim...")
                break
            elif result == 'help':
                await self._show_help()
            elif result == 'config':
                await self._handle_config_change()

    async def _show_main_menu(self) -> str:
        """
        Zobrazí hlavní menu s možnostmi výběru.

        Returns:
            str: Klíč vybrané akce
        """
        return await radiolist_dialog(
            title='Hlavní menu',
            text='Vyberte požadovaný úkon:',
            values=[
                ('config', 'Změnit konfiguraci'),
                ('help', 'Zobrazit nápovědu'),
                ('exit', 'Ukončit interaktivní režim')
            ],
            style=self.style
        ).run()

    async def _handle_config_change(self) -> None:
        """Zpracuje proces změny konfigurace."""
        # Nejprve zobrazíme výběr klíče
        key = await self._select_config_key()
        if not key:
            return

        # Pak zobrazíme dialog pro zadání hodnoty
        value = await self._input_config_value(key)
        if value is None:
            return

        # Provedeme validaci a uložení
        if self._validate_and_save(key, value):
            await self._show_success_menu(key, value)

    async def _select_config_key(self) -> Optional[str]:
        """
        Zobrazí menu pro výběr konfiguračního klíče.

        Returns:
            Optional[str]: Vybraný klíč nebo None při zrušení
        """
        values = [
            (key, f"Nastavení pro '{key}' - {self.keys_data[key].INFO}")
            for key in self.keys_data
        ]

        return await radiolist_dialog(
            title='Výběr konfiguračního klíče',
            text='Vyberte klíč pro změnu hodnoty:',
            values=values,
            style=self.style
        ).run()

    async def _input_config_value(self, key: str) -> Optional[Any]:
        """
        Zobrazí dialog pro zadání nové hodnoty.

        Args:
            key: Konfigurační klíč

        Returns:
            Optional[Any]: Zadaná hodnota nebo None při zrušení
        """
        key_instance = self.keys_data[key]
        current_value = self.config_inst.config[key]

        help_text = (
            f"Aktuální hodnota: {current_value}\n"
            f"Výchozí hodnota: {key_instance.default_value}\n\n"
            f"Nápověda:\n{key_instance.HINT}\n\n"
            f"Zadejte novou hodnotu:"
        )

        result = await input_dialog(
            title=f'Nastavení hodnoty pro {key}',
            text=help_text,
            style=self.style
        ).run()

        return self._convert_value(result, key) if result else None

    def _convert_value(self, value: str, key: str) -> Any:
        """
        Převede zadanou hodnotu na správný datový typ.

        Args:
            value: Zadaná hodnota
            key: Konfigurační klíč

        Returns:
            Any: Převedená hodnota
        """
        try:
            if isinstance(self.keys_data[key].default_value, bool):
                return value.lower() in ('true', '1', 'yes')
            elif isinstance(self.keys_data[key].default_value, int):
                return int(value)
            return value
        except ValueError:
            return value

    def _validate_and_save(self, key: str, value: Any) -> bool:
        """
        Validuje a uloží novou hodnotu.

        Args:
            key: Konfigurační klíč
            value: Nová hodnota

        Returns:
            bool: True pokud byla hodnota úspěšně uložena
        """
        if self.keys_data[key].validate(value):
            self.config_inst.config[key] = value
            return True

        print(f"\nChyba: Neplatná hodnota pro klíč '{key}'")
        print(f"Detail: {self.keys_data[key].DETAIL}")
        return False

    async def _show_success_menu(self, key: str, value: Any) -> None:
        """
        Zobrazí potvrzení o úspěšné změně a menu pro další akci.

        Args:
            key: Změněný klíč
            value: Nová hodnota
        """
        print(f"\nÚspěšně jste nastavili klíč '{key}' na hodnotu {value}")

        result = await radiolist_dialog(
            title='Další akce',
            text='Vyberte další akci:',
            values=[
                ('main', 'Hlavní menu'),
                ('exit', 'Ukončit interaktivní režim')
            ],
            style=self.style
        ).run()

        if result == 'exit':
            print("\nUkončuji interaktivní režim...")
            exit(0)

    async def _show_help(self) -> None:
        """Zobrazí nápovědu pro používání interaktivního režimu."""
        help_text = """
        Nápověda pro interaktivní režim:

        1. Navigace
           - Použijte šipky nahoru/dolů pro pohyb v menu
           - Potvrďte výběr klávesou Enter
           - Escape nebo Ctrl+C pro návrat/zrušení

        2. Změna konfigurace
           - Vyberte klíč, který chcete změnit
           - Zadejte novou hodnotu podle zobrazené nápovědy
           - Hodnota bude validována před uložením

        3. Tipy
           - U každého klíče je zobrazena aktuální a výchozí hodnota
           - Nápověda obsahuje povolené hodnoty a jejich význam
        """

        print(help_text)
        input("\nStiskněte Enter pro návrat do hlavního menu...")