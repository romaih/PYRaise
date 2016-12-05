#program to get a number and find all of its divisors
num = int(input("Enter a number to find all its divisors : "))
lis = [i for i in range(1,num+1) if num%i == 0]
print(lis)
