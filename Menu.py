from Benutzer import Benutzer
import json 
class Menu:
    def __init__(self):        
        self.__benutzer = []         #eine Liste erstelle fuer mehrere benutzer
        self.aktueller_benutzer = None    #kein loggin
        self.laden()          # rufe sofort benutzerdatei auf
        self.__versuche = []

    def neuBenutzer(self):          #registriere neue benutzer 
        print("Registrierung")
        name = input("geben Sie username ein: ")
        pas = input("und password: ")
        for b in self.__benutzer:    # schleife statt abfrage, damit allebenutzer ueberpruefen
            if name == b.name:          #b ist immer ein benutzer
                #oder! if name in [b.name for b in self.__benutzer]:  # list comprehension
                print("benutzer existiert bereits!")
                return
        self.__benutzer.append(Benutzer(name, pas))  #.append fügt benutzer hinzu
        print("Benutzer anlegen!")
        self.speichern()      #speichere in .json

    def anmelden(self):
        print("geht oder?")
        if not self.__benutzer:     #existiert user oder nicht
            print('kein benutzer, bitte registrieren zuerst')
            return
        
        username = input("username: ")
        benutzer = None   
        #benutzer suchen
        for b in self.__benutzer:
            if b.name == username:
                benutzer = b
                break
                    #wenn nicht user existiert
        if not benutzer:
            print("benutzer existiert nicht")
            self.speichern_versuche(username, False)
            return
            
        for i in range(3):         # 3 versuche für jeder
                password = input("password: ")

                if password == benutzer.pas:   #passwort korrekt
                    print("anmeldung erfolgreich")
                    self.aktueller_benutzer = benutzer

                    print("LOGIN USER:", self.aktueller_benutzer.name)
                    print("ROLLE:", self.aktueller_benutzer.rolle)

                    self.speichern_versuche(username, True)
                    return
                        #wenn passwort falsch
                print("sie haben", i+1, " von 3 versuch gemacht")
                self.speichern_versuche(username, False)
        print("3 flasche versuche, anmeldung gescheitert")

    def speichern(self):       #json speichern
        daten = [{"name": b.name, "pas": b.pas, "rolle": b.rolle} for b in self.__benutzer]
        #python funktion offnet datei im schreibmodus write
        with open("users.json", "w") as f: 
            json.dump(daten, f, indent=4)   # das wandelt daten in json format
            
    def speichern_versuche(self, username, erfolgreich): # einzelnen lpgin versuch speichern
        versuch = {
            "username": username,
            "erfolgreich": erfolgreich
        }
        try:
            # vorhandene datei laden
            with open("versuche.json", "r") as f:
                daten = json.load(f)
        except FileNotFoundError:
            #wenn datei nicht exisitert - neue datei erstellen
            daten = []
        daten.append(versuch)
        # speichere aktualisierte versuche in json datei
        with open("versuche.json", "w") as f:
            json.dump(daten, f, indent=4)

    def laden(self):    #json laden
        try:
            with open("users.json", "r") as f:    #offnet datei im lesenmodus read
                daten = json.load(f)          # f ist geoffnete datei
                # für jeder d-dictionary
                self.__benutzer = [Benutzer(d["name"], d["pas"], d.get("rolle", "user")) for d in daten]  
        except FileNotFoundError:
            print("keine benutzerdatei gefunden")
            self.__benutzer = []       # leere benutzerliste

    def abmelden(self):
        if self.aktueller_benutzer:
            print(f"{self.aktueller_benutzer.name} abgemeldet")
            self.aktueller_benutzer = None
        else:
            print("kein benutzer angemeldet")

    def beenden(self):    
        print("beenden")

    def ist_admin(self):
        # prüfen, ob aktueller benutzer admin ist
        return self.aktueller_benutzer and self.aktueller_benutzer.rolle == "admin"
    
    def benutzer_anzeigen(self):
        print("Benutzerliste:")
        for b in self.__benutzer:
            print(f"Name: {b.name}, Rolle: {b.rolle}")

    def benutzer_loeschen(self):
        name = input("welche benutzer möchten sie löschen? ")
        for b in self.__benutzer: 
            if b.name == name: # finde benutzer mit passendem name
                self.__benutzer.remove(b) # löscht user
                print(f"Benutzer {name} gelöscht.")
                self.speichern()  # Änderungen speichern
                return
        print(f"Benutzer {name} nicht gefunden.")
    def benutzer_bearbeiten(self):
        name = input("welcher benutzer:")

        for b in self.__benutzer:
            if b.name == name:
                neuer_name = input("neuer name :")
                neue_password = input("neues passwort:")

                if neuer_name:
                    b.name = neuer_name
                if neue_password:
                    b.pas = neue_password

                self.speichern()
                print("benutzer aktualisisert")
                return
                print("nicht gefunden")

    def Hauptmenu(self):        #main
        ende = False
        while not ende:
            print("**hauptmenu**")
            print("1 - Anmelden")
            print("2 - Benutzer anlegen")
            print("3 - abmelden")
            print("4 - beenden")

            if self.ist_admin():
                print("5 - benutzer anzeigen")
                print("6 - benutzer löschen")   
                print("7 - benutzer bearbeiten")
            
            wahl = input("was ist eure wahl?")

            if wahl == "1":
                self.anmelden()
            elif wahl == "2":
                self.neuBenutzer()
            elif wahl == "3":
                self.abmelden()
            elif wahl == "4":
                self.beenden()
                ende = True
                # admin funktionen
            elif wahl == "5" and self.ist_admin():
                self.benutzer_anzeigen()
            elif wahl == "6" and self.ist_admin():
                self.benutzer_loeschen()
            elif wahl == "7" and self.ist_admin():
                self.benutzer_bearbeiten()
            else: 
                print("keine ahnung was ist das ")
                
# start
if __name__ == "__main__":
    menu = Menu()
    menu.Hauptmenu()