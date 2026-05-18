class Benutzer:
    #erstellt die Klasse Benutzer mit den Attributen name, pas und rolle. Die Rolle hat einen Standardwert von "user". Das Attribut expiry_date wird hinzugefügt, um das Ablaufdatum eines Benutzers zu speichern, falls dieser in Zukunft gelöscht werden soll.
    def __init__(self, name: str, pas: str, rolle: str = "user", expiry_date=None, aktiv=True):
        self.name = name
        self.pas = pas
        self.rolle = rolle
        self.expiry_date = expiry_date
        self.aktiv = aktiv