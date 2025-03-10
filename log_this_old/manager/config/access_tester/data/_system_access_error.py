class SystemAccessError(Exception):
    def __init__(self, message: str, detail: str = "", hint: str = ""):
        self.message = message
        self.detail = detail
        self.hint = hint
        super().__init__(self.message)