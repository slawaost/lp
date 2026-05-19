from model import Benutzer
from typing import List
from db import DBConnection
class BenutzerRepoDB:
    def __init__(self, db: DBConnection):
        self.db = db
    #Benutzer aus DB laden
    def laden(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM python")
        rows = cursor.fetchall()
        conn.close()
        return [
            Benutzer(row['name'], row['pas'], row['rolle'], row['expiry_date'], row['aktiv'])
            for row in rows
        ]
    #Benutzer speichern (komplette Liste ersetzen)
    def speichern(self, liste: List[Benutzer]):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM python")
        for benutzer in liste:
            cursor.execute(
                "INSERT INTO python (name, pas, rolle, expiry_date, aktiv) VALUES (%s, %s, %s, %s, %s)",
                (benutzer.name, benutzer.pas, benutzer.rolle, benutzer.expiry_date, benutzer.aktiv)
            )
        conn.commit()
        conn.close()