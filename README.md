# Benutzerverwaltung

Eine Python-basierte Benutzerverwaltungsanwendung mit tkinter GUI, MySQL-Datenbank und rollenbasierter Zugriffskontrolle (RBAC).

## Features

- **Registrierung & Login** – Benutzer können sich registrieren und anmelden
- **Rollenbasierte Zugriffskontrolle (RBAC)** – Admin- und Benutzerrollen
- **Benutzerverwaltung** – Nur Admins können Benutzer verwalten
- **Benutzerdeaktivierung** – Benutzer können deaktiviert/aktiviert werden
- **Geplante Löschung** – Benutzer können zum späteren Zeitpunkt gelöscht werden
- **Lagerverwaltung** – Integrierte Warehouse-GUI für angemeldete Benutzer
- **MySQL-Persistenz** – Alle Benutzerdaten werden in MySQL gespeichert

## Installation

1. Abhängigkeiten installieren:
```bash
pip install mysql-connector-python
```

## Programm starten

```bash
python main.py
```

Das Programm öffnet ein Fenster mit dem Login-Bildschirm.

## Admin-Benutzer erstellen

Führen Sie SQL-Befehl aus:
```sql
INSERT INTO python (name, pas, rolle, aktiv) VALUES ('admin', 'admin123', 'admin', TRUE);
```

Oder manuell beim ersten Start mit der Anwendung registrieren und anschließend in der Datenbank die Rolle auf `admin` setzen:
```sql
UPDATE python SET rolle = 'admin' WHERE name = 'admin';
```

## Benutzerverwaltung (Admin)
Nach erfolgreichem Admin-Login werden zusätzliche Buttons angezeigt:
- **Benutzer anzeigen** – Listet alle registrierten Benutzer auf
- **Benutzer sofort löschen** – Löscht einen Benutzer sofort
- **Benutzer später löschen** – Plant eine Löschung für einen zukünftigen Zeitpunkt
- **Benutzer bearbeiten** – Ändert Namen/Passwort eines Benutzers
- **Benutzer aktivieren/deaktivieren** – Deaktiviert Logins für einen Benutzer
- **Geplante Löschungen anzeigen** – Zeigt Benutzer, die geplant gelöscht werden

## Lagerverwaltung

Alle angemeldeten Benutzer können auf die Lagerverwaltung (Warehouse) zugreifen. Diese wird in einem separaten Fenster geöffnet.

## Autor

[slawaost]