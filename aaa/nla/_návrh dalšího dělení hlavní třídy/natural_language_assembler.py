from action_manager import ActionManager
from code_generator import CodeGenerator
from text_parser import TextParser


class NaturalLanguageAssembler:
    """
    Základní třída jazyku
    """

    def __init__(self):
        self.objects = {}
        self.action_manager = ActionManager()
        self.text_parser = TextParser()
        self.code_generator = CodeGenerator(self.objects)

        # Další inicializace...

    def compile(self, text):
        """Kompilace textu do vnitřní reprezentace objektů."""
        parsed_result = self.text_parser._process_words(text)

        return {
            "parsed": parsed_result,
            "objects": self.objects
        }

    def generate_python(self):
        """Delegace generování kódu na CodeGenerator"""
        return self.code_generator.generate_python()













