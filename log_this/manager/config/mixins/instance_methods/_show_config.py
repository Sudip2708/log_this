class ShowConfigMixin:

    def show_config(self):
        """Vypíše aktuální konfiguraci pomocí logeru."""
        self.logger(str(self))