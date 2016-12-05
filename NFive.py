#This program recieve a string input then check if is a palindrome or not.
# palindrome is a word which can be read the same forward or backward.
t = input("Please type A palindrome: ")
x=''
for i in range(len(t)):
    x+=t[len(t)-1-i]


if t == x:
    print("Correct! This is a palindrome :)")
else:
    print("Wrong, please try again later")
