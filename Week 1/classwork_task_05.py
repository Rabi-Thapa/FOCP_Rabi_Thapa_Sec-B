
student=[113,175,12]
lab= 24
n=1
for i in student:
    full_group= i//lab
    left_over= i-(full_group * lab)
    print("In {} group \nFull Group= {} Left Over Student= {}".format(n,full_group,left_over))
    n= n+1

