from loginform.repository import BenutzerRepo
from loginform.service import BenutzerService
from loginform.cli import CLI

def main():
    # Repository initialisieren (Datenzugriff)
    repo = BenutzerRepo("users.json")

    # Service (Logik + RBAC)
    service = BenutzerService(repo)

    # CLI (User Interface)
    cli = CLI(service)

    # Programm starten
    cli.run()


if __name__ == "__main__":
    main()