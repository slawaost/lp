from Benutzer import Benutzer
import json 
class Menu:

    def __init__(self):
        
        self.__benutzer = []  #eine Liste erstelle fuer mehrere benutzer

        self.laden() # rufe sofort benutzerdatei auf

    #registriere neue benutzer
    def neuBenutzer(self):  
        print("Registrierung")
        name = input("geben Sie username ein: ")
        pas = input("und password: ")
        # schleife statt abfrage, damit allebenutzer ueberpruefen
        for b in self.__benutzer:
            #b ist immer ein benutzer
            if name == b.name:
                print("benutzer existiert bereits!")
                return
            #.append fügt benutzer hinzu
        self.__benutzer.append(Benutzer(name, pas))
        print("Benutzer anlegen!")

    def anmelden(self):
      
        if not self.__benutzer:
            print('kein benutzer, bitte registrieren zuerst')
            return
        #benutzer überprüft
        for i in range(3):
            username = input("username: ")
            password = input("password: ")
            #füge da auch schleife hinzu
            for b in self.__benutzer:
                if username == b.name and password == b.pas:
                    print("anmeldung erfolgreich")
                    return
            
            print("sie haben", i+1, "von 3 versuch gemacht")
        
        print("sie haben nur 3 versuche")

    #json speichern
    def speichern(self):
        daten = [{"name": b.name, "pas": b.pas} for b in self.__benutzer]
        #python funktion offnet datei im schreibmodus write
        with open("users.json", "w") as f:
            json.dump(daten, f) # das wandelt daten in json format
    #json laden
    def laden(self):
        #offnet datei im lesenmodus read
        with open("users.json", "r") as f:
            daten = json.load(f) # f- geoffnete datei
            self.__benutzer = [Benutzer(d["name"], d["pas"]) for d in daten]  # für jeder d-dictionary

    def beenden(self):
    
        print("beenden")

        self.speichern() #speichere nach beenden

    def Hauptmenu(self):
        ende = False
        while not ende:
            print("**hauptmenu**")
            print("1 - Anmelden")
            print("2 - Benutzer anlegen")
            print("3 - beenden")
            
            wahl = input("was ist eure wahl?")

            if wahl == "1":
                self.anmelden()
            elif wahl == "2":
                self.neuBenutzer()
            elif wahl == "3":
                self.beenden()
                ende = True
            else: 
                print("keine ahnung was ist das ")

# start
if __name__ == "__main__":
    menu = Menu()
    menu.Hauptmenu()