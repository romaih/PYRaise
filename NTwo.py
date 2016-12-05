#a program to check if the number is even or odd.
num = int(input("Enter a random number: "))
if (num%2 ==0):
    if (num%4 ==0):
        print("this number is a multiple of 4")
    else:
        print("this is an even number")
else:
    print("this is an odd number")

num = int(input("Enter a random number again: "))
check = int(input("Dividable number: "))
if (num%check==0):
    print("correct",num,"is dividable by ",check)
else:
    print("Incorrect",num,"is not dividable by ",check)

