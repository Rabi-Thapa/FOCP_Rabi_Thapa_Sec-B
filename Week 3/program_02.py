while True:
    password= input("Enter New password: ")
    conform= input("Conform password: ")
    if password== conform:
        print("Password Set")
        break
    else:
        print("Error!")