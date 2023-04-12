from calculate import calculate
from even_list import even_str

print("Hello, world!")

print("Even numbers in the list: ", even_str)

print("Enter first number")
try:
    num1 = int(input())
except ValueError:
    print("Wrong input!")
    num1 = 0

print("Enter second number")
try:
    num2 = int(input())
except ValueError:
    print("Wrong input!")
    num2 = 0

print(f"{num1} + {num2} = ", calculate(num1, num2, "add"))
print(f"{num1} - {num2} = ", calculate(num1, num2, "sub"))
print(f"{num1} * {num2} = ", calculate(num1, num2, "mul"))
print(f"{num1} / {num2} = ", calculate(num1, num2, "div"))

