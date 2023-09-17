"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
"""

x = int(input("enter the first number: "))
y = int(input("enter the second number: "))

for i in range(1,11):
   print(x,'x',i,'=',x*i)
   print(y,'x',i,'=',y*i)