number= int(input("Enter a Number: "))

if number <0:
    for i in range(12,-1,-1):
        print("{} * {} = {}".format(i,number,i*number))

else:
    for i in range(12):
        print("{} * {} = {}".format(i,number,i*number))
