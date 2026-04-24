class Benutzer:
    def __init__(self, name: str, pas: str, rolle: str = "user"):
        self.name = name
        self.pas = pas
        self.rolle = rolle