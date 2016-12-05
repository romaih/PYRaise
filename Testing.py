import random
'''
import sys
name = input("who are you: ")
print ("hello %s" % (name,))

print(sys.version)
#python_version()
'''

#square = [x**2 for x in range(10)]
#print(square)

#weekpas = ['apple', 'orange', '12345', '112233', 'asdasd', 'nonono']
#rep = random.randint(1,2)
#pas = random.sample(weekpas, rep)
#pas = "".join(pas)
#print(pas)
i = 0
x = []
while i < 2:
    x+= random.choice('!@#$%')
    x+= random.choice("0123456789")
    x+= random.choice("ASDFGHJKLQWERTYUUZXCVBNM")
    x+= random.choice("qwertyuiopasdfghjklzxcvbnm")
    i += 1
random.shuffle(x)
x = "".join(x)
print(x)