""" 
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
"""

x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
odd = []
even = []

for num in range(x, y + 1):
    if num % 2 != 0:
        odd.append(num)

    elif num % 2==0:
        even.append(num)

print("even list", even)
print("odd list", odd)     
        