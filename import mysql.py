import mysql.connector                     # das ist bibliothek für die mysql verbindung
import json
    
with open('config.json', "r") as file:         #JSON-datei
    config = json.load(file)

con = mysql.connector.connect(               # verbindung zur datenbank herstellen
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database'],
    port=config['port'])

if con.is_connected():
    print("Verbindung zur Datenbank hergestellt.")            # überprüfung 

cursor = con.cursor(buffered=True)                         # cursor objekt erstellen, buffered=True ermöglicht das Abrufen von Ergebnissen
SQLBefehl = "SELECT * FROM benutzer" 
cursor.execute(SQLBefehl)                                   # SQL befehl ausführen

row=cursor.fetchone()                               # holt die erste Zeile des Ergebnisses, wenn es mehrere Zeilen gibt, kann man mit fetchone() weiter durch die Ergebnisse iterieren
while row is not None:                      # solange es eine Zeile gibt, wird sie ausgegeben
    print(row[0], row[1], row[2], row[3], row[4], row[5]) 
    row=cursor.fetchone()                    # holt die nächste Zeile des Ergebnisses, wenn es keine Zeile mehr gibt, wird None zurückgegeben und die Schleife endet

cursor.close()                           # schließt den Cursor, um Ressourcen freizugeben. 
con.close()                                   # schließt die Datenbankverbindung