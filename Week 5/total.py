import sys

# The first element of the sys.argv list is the program name itself,
count = len(sys.argv)


# This statement will execute if no argument is provided.
if count <= 1:
    print("No arguments were provided.")

# This will execute if one or more argument is passed.
else:
    total= 0
    while count>1 :
        count -= 1
        total += float(sys.argv[count])

    print("Total is ",total)
    print("The average is ",total/len(sys.argv[1:]))


# python total.py 10 11 12 13 14 15 16 17
# Output 1
# Total is  108.0
# The average is  13.5  

# python total.py
# Output 2
# No argument is provided.


