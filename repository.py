import json
from model import Benutzer

class BenutzerRepo:
    def __init__(self, datei="users.json"):
        self.datei = datei

    def laden(self):
        try:
            with open(self.datei, "r") as f:
                daten = json.load(f)
                return [
                    Benutzer(d["name"], d["pas"], d.get("rolle", "user"))
                    for d in daten
                ]
        except FileNotFoundError:
            return []

    def speichern(self, benutzer_liste):
        daten = [
            {"name": b.name, "pas": b.pas, "rolle": b.rolle}
            for b in benutzer_liste
        ]
        with open(self.datei, "w") as f:
            json.dump(daten, f, indent=4)