"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
"""

x = int(input("enter the first number: "))
y = int(input("enter the second number: "))

for num in range(1,101):
    if num % x==0 and num % y==0:
        print (num)
   