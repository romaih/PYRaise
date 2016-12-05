#This program compare two list and print out the common elements.
a = [1,1,2,3,5,8,13,21,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
c = []
for i in range(0,len(a)):
    if a[i] in b and a[i] not in c:
        c.append(a[i])
print(c)