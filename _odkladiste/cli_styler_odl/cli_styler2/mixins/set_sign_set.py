from abc import ABC
from ...abc_helper import abc_method, abc_property


class SetSignSetMixin(ABC):

    _signs_sets = abc_property("_signs_sets")
    _current_signs_set = abc_property("_current_signs_set")
    get_current_styles_attributes = abc_method("get_current_styles_attributes")


    def validate_signs_set(self, signs_set):
        """Metoda pro validaci setu značek"""
        if not signs_set in self._signs_sets.keys():
            raise ValueError(f"Byl zadán neplatný set pro značky. "
                             f"Povolené sety: {self._signs_sets.keys()}")

    def set_sign_set(self, signs_set):
        """
        Metoda pro změnu sady znaků

        Metoda nejprve se pokusí změnit sadu znaků ve třídě CLISigns
        - pokud bude zadat neplatný set metoda change_sign_set vyvolá výjimku

        Následně metoda spustí metodu pro změnu hodnot atributů této třídy
        """
        self.validate_signs_set(signs_set)
        self._current_signs_set = self._signs_sets[signs_set]
        self.get_current_styles_attributes()

