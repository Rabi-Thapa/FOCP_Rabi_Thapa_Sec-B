from re import A


age= 30
a= (age >= 18 and age <= 65)   # True
b= (age <18 or age > 65)       # False
c= (not age > 18)              # False

print(a)
print(b)
print(c)

d= (age >= 18 and age <= 65) and (not age == 30)     #False  
print(d)