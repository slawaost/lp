from db import DBConnection
from neurepo import BenutzerRepoDB
from service import BenutzerService
#from cli import CLI
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
    
# CLI-Instanz erstellen und mit dem Service initialisieren
    #cli = CLI(service)
# CLI ausführen
   # cli.run()
# Wenn das Skript direkt ausgeführt wird, wird die main()-Funktion aufgerufen, die die gesamte Anwendung startet.
if __name__ == "__main__":
    main()