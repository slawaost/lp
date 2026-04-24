''' diese repo habe für db connect erstellt'''
from model import Benutzer
import mysql.connector
from db import DBConnection

class BenutzerRepoDB:
    def __init__ (self, db):
        self.db = db

    def laden(self): 
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM python")
        rows = cursor.fetchall()

        conn.close()
        return [Benutzer(row['name'], row['pas'], row['rolle']) for row in rows]
    

    def speichern(self, liste):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM python")  # Alle vorhandenen Einträge löschen

        for benutzer in liste:
            cursor.execute(
                "INSERT INTO python (name, pas, rolle) VALUES (%s, %s, %s)",
                (benutzer.name, benutzer.pas, benutzer.rolle)                          
            )

            conn.commit()
        conn.close()
        