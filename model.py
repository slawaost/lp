class Benutzer:
    #erstellt die Klasse Benutzer mit den Attributen name, pas und rolle. Die Rolle hat einen Standardwert von "user".
    def __init__(self, name: str, pas: str, rolle: str = "user"):
        self.name = name
        self.pas = pas
        self.rolle = rolle