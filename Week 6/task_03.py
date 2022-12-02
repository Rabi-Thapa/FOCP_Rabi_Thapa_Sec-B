def isPrime(num):
    

    if(num > 1):
        for i in range(2, num):
            if( num % i ==0):
                print(num, " is Not prime")
                break
        else:
            print(num, " is prime.") 
    
    else:
       print("num must be greater than 1.")


if __name__== '__main__':
    n= int(input("Enter any number: "))
    isPrime(n)