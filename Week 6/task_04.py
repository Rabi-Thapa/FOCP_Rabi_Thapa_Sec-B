def obfuscation(message):
    message= message[::-1]
    return message.replace(" ","")

if __name__== '__main__':
    msg= input("Enter any message: ")
    print(obfuscation(msg))


