class CLI:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            print("\n1 Login")
            print("2 Register")
            print("3 Logout")
            print("4 Exit")

            if self.service.ist_admin():
                print("5 anzeigen")
                print("6 löschen")
                print("7 bearbeiten")

            wahl = input("Wahl: ")

            if wahl == "1":
                name = input("Name: ")
                pas = input("Passwort: ")
                print(self.service.anmelden(name, pas))

            elif wahl == "2":
                name = input("Name: ")
                pas = input("Passwort: ")
                print(self.service.erstellen(name, pas))

            elif wahl == "3":
                self.service.logout()

            elif wahl == "4":
                break

            elif wahl == "5" and self.service.ist_admin():
                for b in self.service.anzeigen():
                    print(b.name, b.rolle)

            elif wahl == "6" and self.service.ist_admin():
                name = input("löschen: ")
                self.service.löschen(name)

            elif wahl == "7" and self.service.ist_admin():
                name = input("User: ")
                n = input("Neuer Name: ")
                p = input("Neues Passwort: ")
                self.service.bearbeiten(name, n, p)

            else:
                print("ungültig")