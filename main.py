import os 
import hashlib
user_file = 'users.json'

def main():
    options = {'1' :register, '2': login, "3": exit} #dictionary mit schlüsseln (dispatch table) analog:
    '''if choice == '1': 
    register()
elif choice == '2':
    login()
elif choice == '3':
    exit()'''
    while True:
        print ("\1.Register\n2.Login\n3.Exit")
        choice = input ("choose an option: ")

        action = options.get(choice)
        
        if action:
            action()
        
        else:
            print ("invalid option, try again")
