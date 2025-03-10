from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from datetime import datetime
from typing import Optional


class StyledLogger:
    def __init__(self):
        self.style = Style.from_dict({
            # Základní styly pro různé úrovně logování
            'log.info': 'fg:#00af00',  # zelená
            'log.warning': 'fg:#ffaf00',  # oranžová
            'log.error': 'fg:#ff0000 bold',  # červená tučně
            'log.debug': 'fg:#808080 italic',  # šedá kurzívou

            # Styly pro části log zprávy
            'log.timestamp': 'fg:#4444ff',
            'log.level': 'bold',
            'log.message': '',  # základní styl

            # Styly pro interaktivní výstup
            'interactive.prompt': 'fg:#00ff00 bold',
            'interactive.input': 'fg:#ffffff italic',
            'interactive.error': 'bg:#ff0000 #ffffff bold'
        })

    def _format_log_message(self,
                            level: str,
                            message: str,
                            timestamp: Optional[
                                datetime] = None) -> FormattedText:
        """Vytvoří formátovanou log zprávu."""
        timestamp = timestamp or datetime.now()
        return FormattedText([
            ('class:log.timestamp',
             f'[{timestamp.strftime("%Y-%m-%d %H:%M:%S")}] '),
            ('class:log.level', f'[{level.upper()}] '),
            (f'class:log.{level.lower()}', f'{message}\n')
        ])

    def info(self, message: str) -> None:
        """Logování informační zprávy."""
        formatted_msg = self._format_log_message('INFO', message)
        print_formatted_text(formatted_msg, style=self.style)

    def warning(self, message: str) -> None:
        """Logování varování."""
        formatted_msg = self._format_log_message('WARNING', message)
        print_formatted_text(formatted_msg, style=self.style)

    def error(self, message: str) -> None:
        """Logování chyby."""
        formatted_msg = self._format_log_message('ERROR', message)
        print_formatted_text(formatted_msg, style=self.style)

    def debug(self, message: str) -> None:
        """Logování debug zprávy."""
        formatted_msg = self._format_log_message('DEBUG', message)
        print_formatted_text(formatted_msg, style=self.style)

    # Metody pro interaktivní výstup
    def prompt(self, message: str) -> str:
        """Stylované promptování uživatele."""
        formatted_prompt = FormattedText([
            ('class:interactive.prompt', f'{message}: ')
        ])
        return input(formatted_prompt)

    def print_error(self, message: str) -> None:
        """Zvýraznění chybové zprávy v interaktivním režimu."""
        formatted_msg = FormattedText([
            ('class:interactive.error', f' ERROR: {message} \n')
        ])
        print_formatted_text(formatted_msg, style=self.style)


# Příklad použití
def example_usage():
    logger = StyledLogger()

    # Logování
    logger.info("Aplikace se spouští")
    logger.debug("Načítání konfigurace")
    logger.warning("Některá nastavení chybí")
    logger.error("Nelze se připojit k databázi")

    # Interaktivní použití
    try:
        user_input = logger.prompt("Zadejte své jméno")
        logger.info(f"Uživatel zadal: {user_input}")
    except Exception as e:
        logger.print_error(f"Chyba při zpracování vstupu: {str(e)}")


if __name__ == "__main__":
    example_usage()