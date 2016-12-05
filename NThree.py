#This program checks a list then create a new list of items less than a specific number.
a = [1,1,2,3,5,8,13,21,4,55,89,3]
c = []
b = int(input("Enter a number: "))
for i in range(0,len(a)):
    if a[i]<b:
        #print(a[i])
        c.append(a[i])
print(c)