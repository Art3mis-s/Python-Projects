math = input("Expression: ")
#x is the first number, y is the opertors and z is the second number
x, y, z = math.split()
#converting the input number to float
x = float(x)
z = float(z)
if y == "/":
    result = x / z
elif y == "*":
    result = x * z
elif y == "+":
    result = x + z
elif y == "-":
    result = x - z
else:
    print("Invalid Operator:", y)
#printing the floating point result with one decimal place 
print("Result:", round(result, 1))
