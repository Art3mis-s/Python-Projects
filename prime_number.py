# test if an int > 2 is prime. If not, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
# This line is essentially saying that smallest_divisor does not currently have any meaningful value or it is undefined.
smallest_divisor = None
for guess in range(2, x):
    # it checks if the user's input x is divisible evenly (with a remainder of 0) by the current value of guess. If it is, it means that guess is a divisor of x.
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')