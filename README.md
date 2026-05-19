# Benutzerverwaltung

## Beschreibung

Dieses Projekt ist eine einfache Benutzerverwaltung in Python mit:

* Registrierung
* Login
* Benutzerverwaltung (Admin)
* Speicherung in einer MySQL-Datenbank

Das Programm läuft 

## Architektur

Das Projekt ist in Schichten aufgebaut:

* Service (Login, RBAC)
* Repository (SQL)
* DBConnection (DBVerbindung)
* Model (Benutzer)
* GUI mit tkinter erstellt wurde

##  Rollen (RBAC)

Das System unterstützt Rollen:

* `user` → normaler Benutzer
* `admin` → darf Benutzer verwalten

Admin kann:

## Datenbank

## Admin erstellen

## Konfiguration

Datenbankverbindung wird über `config.json` gesteuert:

## Programm starten

```bash
python main.py
```

## Autor

[slawaost]