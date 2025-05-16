from ..._exceptions import (
    VerifyUnexpectedInternalError,
    VerifyAttributeMissingInternalError
)

class AttributesCheck:

    # Definice povinných atributů, které musí mít každá validační třída
    REQUIRED_ATTRIBUTES = [
        "VALIDATOR_KEY",
        "ANNOTATION",
        "IS_INSTANCE",
        "DUCK_TYPING",
        "DESCRIPTION",
        "LONG_DESCRIPTION"
    ]

    def __call__(self, cls):
        """
        Kontroluje přítomnost všech povinných atributů BaseValidator v potomcích.

        Jedná se o pomocnou funkci která je úzce spojena se základní třídou BaseValidator,
        a která slouží při inicializaci potomka pro kontrolu všech poviných atributů.

        Poviné atributy jsou uvedené zde a váží se tedy k validačním třídám.

        Vzhledem k tomu, že se jedná o interní funcki která nemá být použita vně knihovny,
        a vzhledem k tomu, že je volaná při inicializaci potomka,
        při ošetření výjimek se nepočítá s tím, že by nebyla předaná instance,
        a tak metoda zacytává pouze všeobecné výjimky pro neočekávané stavy.
        Žádný by se ale neměl přirozeně vyskytnout.

        Tato funkce ověřuje, zda validační třída definuje všechny požadované atributy,
        které jsou nezbytné pro správné fungování validačního systému. Pokud nějaký
        atribut chybí, vyvolá výjimku s podrobným popisem problému.

        Funkce je definována mimo třídu BaseValidator, aby zbytečně nezatěžovala
        potomky a umožnila izolaci této kontrolní logiky.

        Args:
            cls (class): Třída k ověření

        Raises:
            VerifyNotImplementedAttributeError: Pokud některý z povinných atributů chybí
        """
        try:

            # Kontrola zda jsou všechny atributy přítomné
            missing = self._get_missing(cls)

            # Pokuň některý chybý
            if missing:

                # Vyvolá se výjimka s oznamem
                raise VerifyAttributeMissingInternalError(
                    cls, missing, self.REQUIRED_ATTRIBUTES
                )

        except Exception as e:
            raise VerifyUnexpectedInternalError

    def _get_missing(self, cls):
        """
        Ověří atributy třídy oproti požadovaným a vrátí ty které chybí

        """
        return [
            attr
            for attr in self.REQUIRED_ATTRIBUTES
            if not hasattr(cls, attr)
        ]

attributes_check = AttributesCheck()