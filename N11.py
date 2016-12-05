#Program to check a number if it is a primal or not

def Pri_check(a):
    lis = [i for i in range(2, a) if a % i == 0]
    if lis == []:
        print(a, "is a prime number")
    else:
        print(a, "is not a prime number")


num = int(input("Enter a number to check if it is a prime or not : "))
Pri_check(num)