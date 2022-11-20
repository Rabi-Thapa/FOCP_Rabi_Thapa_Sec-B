import sys
my_list=[]

n= len(sys.argv)
print("Argument passed are: ")

for i in range(1,n):
    my_list.append(sys.argv[i])

print(my_list)
my_list.sort(key=len)

print("The shortest length argument is: ",my_list[0])


