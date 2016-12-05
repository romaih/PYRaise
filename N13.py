#Fibonacci numbers
def fibo(rep1):
    c = [1,1]
    for i in range(1,rep1-1):
        c.append(c[i] + c[i-1])
    print(c)
fibo(int(input("How many Fibonacci number you would like to generate: ")))