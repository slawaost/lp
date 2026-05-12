from neurepo import BenutzerRepoDB 
from model import Benutzer
from db import DBConnection
from model import Benutzer
from datetime import date, timedelta
# Die Klasse BenutzerService bietet Methoden zur Registrierung, Anmeldung, Anzeige, Löschung und Bearbeitung von Benutzern.
class BenutzerService:
    def __init__(self, repo):
        # repo ist eine Instanz von BenutzerRepoDB, die für die Interaktion mit der Datenbank verantwortlich ist. 
        self.repo = repo
        self.benutzer = repo.laden()
        self.aktueller = None

# Die Methode registrieren() überprüft, ob ein Benutzer mit dem angegebenen Namen bereits existiert. Wenn ja, wird eine Fehlermeldung zurückgegeben. Andernfalls wird ein neues Benutzer-Objekt erstellt, zur Liste der Benutzer hinzugefügt und in der Datenbank gespeichert. Schließlich wird eine Erfolgsmeldung zurückgegeben.
    def registrieren(self, name, pas, rolle="user"):
        if any(b.name == name for b in self.benutzer):
            return "Benutzer existiert bereits"
# Andernfalls wird ein neues Benutzer-Objekt erstellt, zur Liste der Benutzer hinzugefügt und in der Datenbank gespeichert. Schließlich wird eine Erfolgsmeldung zurückgegeben.
        self.benutzer.append(Benutzer(name, pas, rolle))
        self.repo.speichern(self.benutzer)
        return "Benutzer erstellt"
# Die Methode anmelden() überprüft, ob ein Benutzer mit dem angegebenen Namen existiert. Wenn ja, wird das Passwort überprüft. Bei erfolgreicher Anmeldung wird der aktuelle Benutzer gesetzt und eine Erfolgsmeldung zurückgegeben. Bei falschem Passwort oder nicht gefundenem Benutzer werden entsprechende Fehlermeldungen zurückgegeben.
    def anmelden(self, name, pas):
        for b in self.benutzer:
            if b.name == name:
                if b.pas == pas:
                    self.aktueller = b
                    return "Login erfolgreich"
                return "Falsches Passwort"

        return "Benutzer nicht gefunden"

    def anzeigen(self):
        return self.benutzer

    def löschen(self, name):
        vorher = len(self.benutzer)
        self.benutzer = [b for b in self.benutzer if b.name != name]
        if len(self.benutzer) == vorher:
            return "Benutzer nicht gefunden"
        self.repo.speichern(self.benutzer)
        return "Benutzer gelöscht"
    
    def löschen_sofort(self, name):
        return self.löschen(name)

    def löschen_in_woche(self, name):
        expiry = date.today() + timedelta(days=7)

        for b in self.benutzer:
            if b.name == name:
                b.expiry_date = expiry
                self.repo.speichern(self.benutzer)
                return f"Benutzer wird am {expiry} gelöscht"
            
        return "Benutzer nicht gefunden"

    def geplante_loeschungen_anzeigen(self):
        return [b for b in self.benutzer if b.expiry_date is not None]
    
    

    def bearbeiten(self, name, neuer_name=None, neues_pass=None):
        for b in self.benutzer:
            if b.name == name:
                if neuer_name:
                    b.name = neuer_name
                if neues_pass:
                    b.pas = neues_pass

                self.repo.speichern(self.benutzer)
                return "Benutzer bearbeitet"
        return "Benutzer nicht gefunden"

    def ist_admin(self):
        return self.aktueller and self.aktueller.rolle == "admin"

    def logout(self):
        self.aktueller = None

    def check_alte_benutzer(self):
        # Beispiel: Alle Benutzer mit Passwort "1234" als unsicher markieren
        for b in self.benutzer:
            if b.pas == "1234":
                print(f"Benutzer {b.name} hat ein unsicheres Passwort!")