# Gussing Game
import random
stop = ''
while stop != "exit":
    cn = random.randint(1,9)
    num = ''
    try1 = 0
    while (num != cn):
        num = int(input("Guess the number 1 to 9: "))
        if num < cn:
            print('you guessed lower number')
            try1 +=1
        if num > cn:
            print('you guessed higher number:')
            try1 +=1
        if num == cn :
            try1 += 1
            print('YOU GUESSED CORRECTLY, IT IS NUMBER ',cn)
            print('You guessed ',try1," times")
            stop = input("Type 'exit' to close the game, or anything to play again")
