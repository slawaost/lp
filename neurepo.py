from model import Benutzer

class BenutzerRepoDB:
    def __init__(self, db):
        self.db = db

    #Benutzer aus DB laden
    def laden(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM python")
        rows = cursor.fetchall()

        conn.close()

        return [
            Benutzer(row['name'], row['pas'], row['rolle'], row['expiry_date'])
            for row in rows
        ]

    #Benutzer speichern (komplette Liste ersetzen)
    def speichern(self, liste):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM python")

        for benutzer in liste:
            cursor.execute(
                "INSERT INTO python (name, pas, rolle, expiry_date) VALUES (%s, %s, %s, %s)",
                (benutzer.name, benutzer.pas, benutzer.rolle, benutzer.expiry_date)
            )

        conn.commit()
        conn.close()