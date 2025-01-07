a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sw = input("You want add or sub?: ")

def addition(a, b):
    sum = a + b
    print(sum)

def subtraction(a, b):
    sub = a - b
    print(sub)

if sw=="add":
    addition(a, b)
else:
    subtraction(a, b)