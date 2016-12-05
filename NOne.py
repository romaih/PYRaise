#This littel program object is to print the year when the end_user age become 100.
from datetime import date
# cur to get the year from the system
cur = int(date.today().year)
Name = input("Type your name please: ")
Age = int(input("Your Age: "))
fy = (100 - Age) + cur
print ("Hello ",Name)
print ("You will get a 100 years old in ",fy)
rep = int(input("How many times you would like to print this result: "))
for i in range(0,rep):
    print(Name,"You will get a 100 years old in ", fy)