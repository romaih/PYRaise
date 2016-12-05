# This program recieve a long string then reverse it
def reverstext(st):
    x = ''
    ttt = st.split()
    for i in range(len(ttt)):
        x += ttt[len(ttt) - 1 - i]
        x += ' '
    print(x)




texts = input("Type any sentence : ")
reverstext(texts)