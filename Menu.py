from Benutzer import Benutzer

class Menu:

    def __init__(self):
        self.__benutzer = None

    def neuBenutzer(self):
        print("Registrierung")
        name = input("geben Sie username ein: ")
        __pas = input("und password: ")

        if self.__benutzer is not None:
            if name == self.__benutzer.name: 
                print("benutzer existiert bereits!")
                return
        self.__benutzer = Benutzer(name, __pas)
        print("Benutzer anlegen!")


    def anmelden(self):

        if self.__benutzer is None:
            print('kein benutzer, bitte registrieren zuerst')
            return
        
        print("login: ")

        for i in range(3):
            username = input("username: ")
            password = input("password: ")

            if username == self.__benutzer.name and password == self.__benutzer.pas:
                print("anmeldung erfolgreich")
                return
            else:
                print("sie haben", i+1, "von 3 versuch gemacht")
        
        print("sie haben nur 3 versuche")


    def beenden(self):
    
        print("beenden")


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