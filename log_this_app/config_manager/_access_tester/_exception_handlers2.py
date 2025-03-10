from cli_styler import styler

class ExceptionHandlers:

    def __call__(self, exception_message):

        styler.cli_print.warning.title("Zapisování do souboru není možné")


