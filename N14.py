#Check a list then create new list without duplicates using two functions
import random
def nodup(j):
    v = set(i for i in j)
    print(j)
    print(v)

def nodupfor(r):
    gg=[]
    for i in range(len(r)):
        if r[i] not in gg:
            gg.append(r[i])
    print(gg)
a = [1,1,2,2,5,6,3,8,9,9]
#nodup(random.sample(range(100),10))
nodup(a)
nodupfor(a)