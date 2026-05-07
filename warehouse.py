class Item:
    #TODO: Aufgabe 1 - Klasse Item mit Attribut SKU erstellen 
    __sku: str
    #funktion init implementieren, damit die sku übergeben und gespeichert werden kann.
    def __init__(self, sku: str):
        self.__sku = sku
    # funktion get implementieren, damit die sku eines artikels abgerufen werden kann.
    def getSKU(self) -> str:
        return self.__sku
        
class Shelf:
    __items: list
    __identifier: str

    def __init__(self, identifier: str):
        self.__identifier = identifier
        self.__items = []

    #TODO: Aufgabe 2 - Funktion addItem und getItems implementieren
    def addItem(self, item: Item) -> None: 
        #funktion append() verwende, um den artikel zur liste hinzuzufügen.
        self.__items.append(item)
        
    def getItems(self) -> list:
        return self.__items
    
    def getIdentifier(self) -> str:
        return self.__identifier
    
class Row:
    __shelves: list
    __identifier: str

    def __init__(self, identifier:str):
        self.__identifier = identifier
        self.__shelves = []

    def addShelf(self, shelf:Shelf) -> None:
        self.__shelves.append(shelf)
        
    def getIdentifier(self) -> str:
        return self.__identifier
    
    def getShelves(self) -> list: 
        return self.__shelves

class Warehouse:

    __rows: list

    def __init__(self):
        self.__rows = []
        self.__create_storage()
    
    def __create_storage(self) -> None:
        # In diesem Beispiel erstellen wir ein Lager 
        # mit 3 Reihen und 10 Regalen
        for i in range(1,4):
            r = Row(str(i))
            for i in range(1,11):
                s=Shelf(str(i))
                r.addShelf(s)
            self.__rows.append(r)

#TODO: Aufgabe 3 - Funktion store implementieren, damit der Artikel eingelagert werden können. die funktion soll die sku und den lagerort als parameter erhalten.
    def store(self, sku: str, location: str) -> None:
        #split trennt die Eingabe in Reihe und Regalnummer auf
        a = location.split("-")
        #gpt empfiehlt hier die Überprüfung der Eingabe, um sicherzustellen, dass sie im erwarteten Format vorliegt (z.B. "1-5" für Reihe 1, Regal 5).
        if len(a) != 2:
            raise Exception("Ungültiges Format für Lagerort! Bitte im Format 'Reihe-Regal' eingeben, z.B. '1-5'.")
        
        rowNumber = a[0]
        shelfNumber = a[1]
        # schleife durch alle Reihen rows
        for row in self.__rows:
            if row.getIdentifier() == rowNumber:
                # schleife durch Regale shelves
                for shelf in row.getShelves():
                    #passende finden
                    if shelf.getIdentifier() == shelfNumber:
                        #dann item erstellen 
                        item = Item(sku)
                        #und hinzufügen
                        shelf.addItem(item)
                        return
                raise Exception("Ungültiger Lagerort! Regalnummer nicht gefunden.")
        raise Exception("Ungültiger Lagerort! Bitte überprüfen Sie die eingegebene Reihe und Regalnummer.")
    
#TODO: Aufgabe 4 - Funktion getOverview implementieren
    def getOverview(self) -> str:
        #erstelle string mit Überschrift
        s = "Reihe Regal ItemsSKU\n"
        #schleife durch alle Reihen rows
        for row in self.__rows:
            #schleife durch Regale shelves
            for shelf in row.getShelves():
                s += row.getIdentifier() + " " + shelf.getIdentifier() + " "
                hasItems = False
                for item in shelf.getItems():
                    if hasItems:
                        s += ", "
                    else:
                        hasItems = True
                    s += item.getSKU()
                if not hasItems:
                    s += "leer"

                s += "\n"
                
        return s
  #TODO: Aufgabe 5 funktion find implementieren, damit der artikel anhand der sku gefunden werfen kann
    def find(self, sku: str) -> str:
        #schleife durch alle Reihen rows
        for row in self.__rows:
            #schleife durch Regale shelves
            for shelf in row.getShelves():
                #schleife durch alle artikel items eienes regals
                for item in shelf.getItems():
                    #wenn sku eines artikels mit gesuchter sku übereinstimmt, dann gebe lagerort zurück
                    if item.getSKU() == sku:
                        # Lagerort im Format "Reihe-Regal" zurückgeben (z.b. "1-5")
                        return f"{row.getIdentifier()}-{shelf.getIdentifier()}"
        return "0" 
    
    #item finden und entfernen
    def retrieve(self, sku: str) -> None:
        
        for row in self.__rows:
            
            for shelf in row.getShelves():
            
                for item in shelf.getItems():
                    
                    if item.getSKU() == sku:
                        # artikel aus regal entfernen
                        shelf.getItems().remove(item)
                        return
