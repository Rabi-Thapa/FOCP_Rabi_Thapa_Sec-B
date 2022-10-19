age= input("Enter your age: ")
# print("In one year you will be",age+1)
# The above one will not work because an attempt is being made to apply an
# addition (+) operator to a string type('age') ad integer type operand, which cannot be done.

age= int(age)
print("In one year you will be",age+1)