while True:
    password= input("Enter new password (8-12 characters): ")
    conform= input("Conform password: ")

    if (password == conform) and (len(password)>= 8 and len(password)<=12) :
        print("Password Set")
        break
    else:
        print("!Error")
        break