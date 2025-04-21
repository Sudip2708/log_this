from .method_mixins import (
    ActionTextMixins,
    ActionPrintMixins,
    ConditionIfMixins,
    ConditionElseMixins,
    ExpectValueMixins,
    OperationPlusMixins,
    ObjectUseMixins,
    ObjectCreateMixins
)


class ActionManager(
    ActionTextMixins,
    ActionPrintMixins,
    ConditionIfMixins,
    ConditionElseMixins,
    ExpectValueMixins,
    OperationPlusMixins,
    ObjectUseMixins,
    ObjectCreateMixins

):
    """
    Pomocná třída pro definici základních operací
    """

    def __init__(self):
        self.current_object = None
        self.current_context = []
        self.objects = {}
        self._initialize_actions()

    def _initialize_actions(self):
        """Inicializace slovníku dostupných akcí."""
        self.actions = {
            "create": {
                "object": self._object_create
            },
            "object": self._object_use,
            "expect": {
                "value": self._expect_value
            },
            "print": self._action_print,
            "if": self._condition_if,
            "else": self._condition_else,
            "plus": self._operation_plus,
            "text": self._action_text
        }

    def get_actions_dict(self):
        """Vrátí slovník akcí pro použití v assembleru."""
        return self.actions

    def __call__(self):
        """Alternativní způsob získání slovníku akcí."""
        return self.actions

    def set_objects(self, objects):
        """Nastaví seznam objektů pro práci s akcemi."""
        self.objects = objects

    def get_objects(self):
        """Vrátí aktuální seznam objektů."""
        return self.objects

