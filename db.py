import mysql.connector
import json

''' Diese Klasse stellt eine Verbindung zur MySQL-Datenbank her.
 Sie liest die Konfigurationsdaten aus einer JSON-Datei und bietet 
 eine Methode zum Herstellen der Verbindung. '''

class DBConnection:
    # config.json wird gelesen 
    def __init__(self, config_file="config.json"): 
        with open(config_file, "r") as file:
            self.config = json.load(file)
    
    def connect(self):
        #gibt das Verbindungsobjekt zurück
        return mysql.connector.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            database=self.config['database'],
            port=self.config['port']
        )
    