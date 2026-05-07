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
            Benutzer(row['name'], row['pas'], row['rolle'])
            for row in rows
        ]

    #Benutzer speichern (komplette Liste ersetzen)
    def speichern(self, liste):
        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM python")

        for benutzer in liste:
            cursor.execute(
                "INSERT INTO python (name, pas, rolle) VALUES (%s, %s, %s)",
                (benutzer.name, benutzer.pas, benutzer.rolle)
            )

        conn.commit()
        conn.close()