def validate_style_and_text(style, text):
    """Zkontroluje, zda styl i text jsou řetězce"""
    if not isinstance(style, str) or not isinstance(text, str):
        raise ValueError("Styl a text musí být typu 'str'")