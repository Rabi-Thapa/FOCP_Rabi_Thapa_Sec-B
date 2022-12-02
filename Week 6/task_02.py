def factor(num):
    my_list= []
    for i in range (1,num+1):
        if num % i ==0:
            my_list.append(i)

    print(my_list)
    return

if __name__ == '__main__':
    num= int(input("Enter the number: "))
    factor(num)    


import task_03
task_03.isPrime(num)