# Benutzerverwaltung (CLI + MySQL)

## Beschreibung

Dieses Projekt ist eine einfache Benutzerverwaltung in Python mit:

* Registrierung
* Login
* Benutzerverwaltung (Admin)
* Speicherung in einer MySQL-Datenbank

Das Programm läuft über CLI

## Architektur

Das Projekt ist in Schichten aufgebaut:

* CLI (Input/Output)
* Service (Login, RBAC)
* Repository (SQL)
* DBConnection (DBVerbindung)
* Model (Benutzer)

##  Rollen (RBAC)

Das System unterstützt Rollen:

* `user` → normaler Benutzer
* `admin` → darf Benutzer verwalten

Admin kann:

* Benutzer anzeigen
* Benutzer löschen
* Benutzer bearbeiten

## Datenbank

### Tabelle: `benutzer`

```sql
CREATE TABLE benutzer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    pas VARCHAR(100) NOT NULL,
    rolle VARCHAR(20) DEFAULT 'user'
);
```

## Admin erstellen

```sql
INSERT INTO benutzer (name, pas, rolle)
VALUES ('admin', '1234', 'admin');
```

## Konfiguration

Datenbankverbindung wird über `config.json` gesteuert:

## Programm starten

```bash
python main.py
```

## Autor

[slawaost]