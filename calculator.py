#prompt the user to input numbers for calulation
calculate = input("What you want to calculate?😃 ")
#calulating
#x is the first number, y is the opertors and z is the second number
x, y, z = calculate.split()
#converting the input number to float
x = float(x)
z = float(z)
if y == '/':
    print(x / z)
elif y == '*':
    print(x * z)
elif y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
else:
    print('Syntax Error!⚠️', y)

