from db import DBConnection
from neurepo import BenutzerRepoDB
from service import BenutzerService
from gui import GUI

def main():
    # DB-Verbindung erstellen
    db = DBConnection()
    # BenutzerRepoDB-Instanz erstellen und mit der DB-Verbindung initialisieren
    repo = BenutzerRepoDB(db)
    # BenutzerService-Instanz erstellen und mit dem Repository initialisieren
    service = BenutzerService(repo) 
    gui = GUI(service)
    gui.run()
    
if __name__ == "__main__":
    main()