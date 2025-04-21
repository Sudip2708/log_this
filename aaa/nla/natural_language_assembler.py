from action_manager import ActionManager
from prasser_mixins import (
    ParseTextMixins,
    ProcessSentencesMixins,
    SplitIntoWordsMixins,
    SplitIntoClausesMixins,
    ProcessWordsMixins
)
from assembler_mixins import (
    CompileMixins,
    GeneratePythonMixins
)

class NaturalLanguageAssembler(
    ParseTextMixins,
    ProcessSentencesMixins,
    SplitIntoWordsMixins,
    SplitIntoClausesMixins,
    ProcessWordsMixins,
    CompileMixins,
    GeneratePythonMixins
):
    """
    Základní třída jazyku
    """

    def __init__(self):

        # Vytvoření slovníku pro definovaání vlastních objetů
        self.objects = {}
        self.action_manager = ActionManager()
        self.action_manager.set_objects(self.objects)
        self.actions = self.action_manager.get_actions_dict()
















