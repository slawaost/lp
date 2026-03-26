def login():
    #definiere variable
    username = str(input("Username: " ))
    password = str(input("Password: " ))
    #ersltelle anweisung
    if username == "slawa" and password == "777":
        print("erfolgreich!")
    else:
        print("falsch!")

login() #rufe methode auf