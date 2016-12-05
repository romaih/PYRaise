# Same as NFour but using list Comprehensions
a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(i for i in a for j in b if i == j)
print(c)
# set to prevent duplicat
# c= [i for i in a for j in b if i==j] will print with duplicate.
