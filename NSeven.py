#Rock Paper Scissors game
print("This is Rock Paper Scissors game (2 playes)")
p1=''
p2=''
c=''
aga=''
while aga != 'quit':
    p1= input("Player 1 choose Rock Paper or Scissors: ")
    while  p1 != 'Rock' and p1 != 'Paper' and p1 != 'Scissors':
        p1 = input("Player 1 choose Rock Paper or Scissors: ")
    p2= input("Player 2 choose Rock Paper or Scissors: ")
    while  (p2 != 'Rock' and p2 != 'Paper' and p2 !='Scissors'):
        p2 = input("Player 2 choose Rock Paper or Scissors: ")
    if p1 == 'Rock' and p2 == 'Scissors':
        print("Player 1 wins")
        c = 'done'
    if p1 == 'Paper' and p2 == 'Rock':
        print("Player 1 wins")
        c= 'done'
    if p1 == 'Scissors' and p2 == 'Paper':
        print("Player 1 wins")
        c = 'done'
    if p2 == 'Rock' and p1 == 'Scissors':
        print("Player 2 wins")
        c = 'done'
    if p2 == 'Paper' and p1 == 'Rock':
        print("Player 2 wins")
        c= 'done'
    if p2 == 'Scissors' and p1 == 'Paper':
        print("Player 2 wins")
        c = 'done'
    if c != 'done' :
        print("it is a dual")
    aga= input('type "quit" to exist or anything to play again: ')