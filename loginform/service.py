from loginform.model import Benutzer

class BenutzerService:
    def __init__(self, repo):
        self.repo = repo
        self.benutzer = repo.laden()
        self.aktueller = None

    # ---------- REGISTER ----------
    def erstellen(self, name, pas):
        if any(b.name == name for b in self.benutzer):
            return "Benutzer existiert bereits"

        self.benutzer.append(Benutzer(name, pas))
        self.repo.speichern(self.benutzer)
        return "Benutzer erstellt"

    # ---------- LOGIN ----------
    def anmelden(self, name, pas):
        for b in self.benutzer:
            if b.name == name:
                if b.pas == pas:
                    self.aktueller = b
                    return "Login erfolgreich"
                return "Falsches Passwort"

        return "Benutzer nicht gefunden"

    # ---------- ADMIN ----------
    def anzeigen(self):
        return self.benutzer

    def löschen(self, name):
        self.benutzer = [b for b in self.benutzer if b.name != name]
        self.repo.speichern(self.benutzer)

    def bearbeiten(self, name, neuer_name=None, neues_pass=None):
        for b in self.benutzer:
            if b.name == name:
                if neuer_name:
                    b.name = neuer_name
                if neues_pass:
                    b.pas = neues_pass

        self.repo.speichern(self.benutzer)

    # ---------- RBAC ----------
    def ist_admin(self):
        return self.aktueller and self.aktueller.rolle == "admin"

    def logout(self):
        self.aktueller = None