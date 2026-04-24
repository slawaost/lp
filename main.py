from db import DBConnection
from neurepo import BenutzerRepoDB
from service import BenutzerService
from cli import CLI

def main():
    
    db = DBConnection()

    repo = BenutzerRepoDB(db)

    service = BenutzerService(repo) 

    cli = CLI(service)

    cli.run()

if __name__ == "__main__":
    main()