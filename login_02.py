username = "slawa" #definiere richtige variable
password = "1234"

# schleife für 3 versuchen 
for i in range (3):
    user = input("username: ")
    pas = input("password: ")

    if username == user and password == pas:
        print("erfolgreich!")
        break
    else:
        print("versuch noch mal ")
#nach der schleife print ausgebe
else: 
    print("du kannst nur 3 mal versuchen!")