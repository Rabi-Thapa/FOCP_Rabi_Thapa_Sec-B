import sys
length_args= len(sys.argv)-1

print("Total arguments passed:", length_args)
print("Argument passed are: ",end=" ")

for item in range(1,length_args + 1):
    print(sys.argv[item],end=" ")

 
