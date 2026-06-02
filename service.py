from neurepo import BenutzerRepoDB
from model import Benutzer
from datetime import date, timedelta
import hashlib

# classBenutzerService ist die zentrale Klasse, die die Logik für die Benutzerverwaltung enthält.
class BenutzerService:
    def __init__(self, repo: BenutzerRepoDB):
        # repo ist eine Instanz von BenutzerRepoDB, die für die Interaktion mit der Datenbank verantwortlich ist. 
        self.repo = repo
        self.benutzer = repo.laden()
        self.aktueller = None

    def registrieren(self, name, pas, rolle="user"):
        if any(b.name == name for b in self.benutzer):
            return "Benutzer existiert bereits"
        # Andernfalls wird ein neues Benutzer-Objekt erstellt, zur Liste der Benutzer hinzugefügt und in der Datenbank gespeichert. 
        hash_password = hashlib.sha256(pas.encode("utf-8")).hexdigest() # Passwort wird gehashed, um es sicherer zu speichern.
        self.benutzer.append(Benutzer(name, hash_password, rolle))
        # einfach speichern
        self.repo.speichern(self.benutzer)
        return "Benutzer erstellt"
    
        # Die Methode anmelden() überprüft, ob ein Benutzer mit dem angegebenen Namen existiert. Wenn ja, wird das Passwort überprüft.
    def anmelden(self, name, pas):
        self.abgelaufende_benutzer_entfernen()
        # alle benutzer aus der datenbank laden, um sicherzustellen, dass die neursten daten verwendet werden. Dies ist wichtig, falls sich die benutzerliste geändert hat.
        self.benutzer = self.repo.laden()
        for b in self.benutzer:
            if b.name == name:
                if not b.aktiv:
                    return "Benutzer ist deaktiviert"
                hash_password = hashlib.sha256(pas.encode("utf-8")).hexdigest()
                if b.pas == hash_password:
                    self.aktueller = b
                    return "Login erfolgreich"
                return "Falsches Passwort"
        return "Benutzer nicht gefunden"

    # aktiv deaktiv in db
    def deaktiv(self, name):
        for b in self.benutzer:
            if b.name == name:
                if b.aktiv == True:
                    b.aktiv = False 
                    self.repo.speichern(self.benutzer)
                    return "Benutzer deaktiviert"
                else:
                    b.aktiv = True 
                    self.repo.speichern(self.benutzer)
                return "Benutzer aktiviert " 
        return "Benutzer nicht gefunden"
    
    # Die Methode löschen() entfernt einen Benutzer mit dem angegebenen Namen aus der Liste der Benutzer und speichert die aktualisierte Liste in der Datenbank. 
    def löschen(self, name):
        self.benutzer = self.repo.laden() # lade aktuell daten
        # vorher die Anzahl der Benutzer speichern, um später zu überprüfen, ob ein Benutzer gelöscht wurde
        vorher = len(self.benutzer)
        self.benutzer = [b for b in self.benutzer if b.name != name]
        if len(self.benutzer) == vorher:
            return "Benutzer nicht gefunden"
        self.repo.speichern(self.benutzer)
        return "Benutzer gelöscht"
    
    # diese methode setzt das ablaufdatum eines benutzers auf eine woche in der zukunft, damit er in eiener woche automatisch gelöscht wird. 
    
    #NICHT LÖSCHT IN DATENBANK!!!!
    
    def löschen_spaeter(self, name, tage):
        self.benutzer = self.repo.laden()
        expiry = date.today() + timedelta(days=int(tage))
        # Dann wird die Liste der Benutzer durchlaufen
        for b in self.benutzer:
            if b.name == name:
                b.expiry_datetime = expiry
                self.repo.speichern(self.benutzer)
                return f"Benutzer wird am {expiry} gelöscht"
        return "Benutzer nicht gefunden"
    
    def abgelaufende_benutzer_entfernen(self):
        self.benutzer = self.repo.laden()

        self.benutzer = [ b for b in self.benutzer if b.expiry_datetime is None or b.expiry_datetime.date() > date.today() ]

        self.repo.speichern(self.benutzer)

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

    def löschen_sofort(self, name):
        return self.löschen(name)

    def geplante_loeschungen_anzeigen(self):
        return [b for b in self.benutzer if b.expiry_datetime is not None]
    
    def anzeigen(self):
        return self.benutzer
    