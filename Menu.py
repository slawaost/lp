from Benutzer import Benutzer
import json 
class Menu:

    def __init__(self):
        
        self.__benutzer = []  #eine Liste erstelle fuer mehrere benutzer
        self.aktueller_benutzer = None
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
        self.speichern() #speichere in .json


    def anmelden(self):
      
        if not self.__benutzer:
            print('kein benutzer, bitte registrieren zuerst')
            return
        
        while True:
            username = input("username: ")

            #benutzer suchen
            benutzer = None
            for b in self.__benutzer:
                if b.name == username:
                    benutzer = b 
                    break

            if not benutzer:
                print("benutzer existiert nicht")
                continue

            # 3 versuche für jeder 

            for i in range(3):
                password = input("password: ")

                if password == benutzer.pas:

                    print("anmeldung erfolgreich")
                    self.aktueller_benutzer = benutzer
                    return

                print("sie haben", i+1, " von 3 versuch gemacht")
            print("sie haben nur 3 versuche")


    #json speichern
    def speichern(self):
        daten = [{"name": b.name, "pas": b.pas} for b in self.__benutzer]
        #python funktion offnet datei im schreibmodus write
        with open("users.json", "w") as f:
            json.dump(daten, f, indent=4) # das wandelt daten in json format 


    #json laden
    def laden(self):
        try:
            #offnet datei im lesenmodus read
            with open("users.json", "r") as f:
                daten = json.load(f) # f- geoffnete datei
                self.__benutzer = [Benutzer(d["name"], d["pas"]) for d in daten]  # für jeder d-dictionary
        except FileNotFoundError:
            print("keine benutzerdatei gefunden")
            self.__benutzer = [] # leere benutzerliste

    def abmelden(self):
        if self.aktueller_benutzer:
            print(f"{self.aktueller_benutzer.name} abgemeldet")
            self.aktueller_benutzer = None
        else:
            print("kein benutzer angemeldet")


    def beenden(self):    
        print("beenden")

      
    def Hauptmenu(self):
        ende = False
        while not ende:
            print("**hauptmenu**")
            print("1 - Anmelden")
            print("2 - Benutzer anlegen")
            print("3 - abmelden")
            print("4 - beenden")
            
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
            else: 
                print("keine ahnung was ist das ")
                
# start
if __name__ == "__main__":
    menu = Menu()
    menu.Hauptmenu()