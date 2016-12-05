#This program generates passwords
import random
def wpass():
    weekpas = ['apple', 'orange', '12345', '112233', 'asdasd', 'nonono']
    rep = random.randint(1, 2)
    pas = random.sample(weekpas, rep)
    pas = "".join(pas)
    print(pas)

def spass():
    i = 0
    x = []
    while i < 2:
        x += random.choice('!@#$%')
        x += random.choice("0123456789")
        x += random.choice("ASDFGHJKLQWERTYUUZXCVBNM")
        x += random.choice("qwertyuiopasdfghjklzxcvbnm")
        i += 1
    random.shuffle(x)
    x = "".join(x)
    print(x)

exx = ' '
while (exx != "exit"):
    ch = input("Type 1 for a week password or type 2 for a strong one : ")
    if ch == '1':
        wpass()
    if ch == '2':
        spass()
    if ch !='1' and ch!='2':
        print("invalid choice, choose 1 or 2 ")
    exx = input("type exit to close the generator or anything to cont: ")