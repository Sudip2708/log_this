class ShowConfigMixin:

    def show_config(self):
        """Vypíše aktuální konfiguraci pomocí logeru."""
        self.cli_log.info(str(self))