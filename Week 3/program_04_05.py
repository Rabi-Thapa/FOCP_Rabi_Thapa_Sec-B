BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password= input("Enter a New Password: ")
    conform= input("Conform Password: ")

    if password != conform:
        print("password does't match")

    elif (password or conform) in BAD_PASSWORDS :
        print("BAD PASSWORD.")

    elif (password== conform) and (len(password)>= 8 and len(password)<= 12) :
        print("Password Set.")
        break
    
    else:
        print("Password  must of length of 8 to 12 character.")








    
    