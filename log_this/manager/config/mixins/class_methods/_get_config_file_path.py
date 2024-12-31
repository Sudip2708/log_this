from pathlib import Path


class GetConfigFilePathMixin:

    @classmethod
    def _get_config_file_path(
        cls,
        file_name: str = "config.json",
    ) -> Path:
        """
        Vytvoří cestu ke konfiguračnímu souboru.

        Pokud je zadaný `file_name` jiný než výchozí, zkontroluje:
        - zda je typu `str`, jinak vyvolá výjimku.
        - zda má koncovku `.json`. Pokud ne, automaticky ji přidá.

        Returns:
            str: Absolutní cesta ke JSON souboru.

        Raises:
            ValueError: Pokud `file_name` není typu `str`.
        """

        # Validace typu `file_name`
        if not isinstance(file_name, str):
            raise ValueError(f"Argument `file_name` musí být typu `str`, byl předán: {type(file_name).__name__}")

        # Kontrola a doplnění přípony `.json`, pokud chybí
        if not file_name.endswith(".json"):
            file_name += ".json"

        # Vrácení cesty s odkazem na soubor
        return Path(cls._config_dir) / file_name
