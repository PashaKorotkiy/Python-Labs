from calculate import calculate
from even_list import even_str

print("Hello, world!")

print("15+5 = ", calculate(15, 5, "add"))
print("15*5 = ", calculate(15, 5, "mul"))
print("15-5 = ", calculate(15, 5, "sub"))
print("15/5 = ", calculate(15, 5, "div"))

print("Even numbers in the list: ", even_str)
