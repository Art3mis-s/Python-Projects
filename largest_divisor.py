# test if an int > 2 is prime. If not, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
# This line is essentially saying that smallest_divisor does not currently have any meaningful value or it is undefined.
largest_divisor = None
# Starting from the largest potential divisor (x - 1) and counting down to 1,
# we iterate through numbers (guess) to find the largest divisor of x.
for guess in range(x - 1, 1, -1):
    # it checks if the user's input x is divisible evenly (with a remainder of 0) by the current value of guess. If it is, it means that guess is a divisor of x.
    if x % guess == 0:
        largest_divisor = guess
        break
if largest_divisor != None:
    print('largest divisor of', x, 'is', largest_divisor)
else:
    print(x, 'is a prime number')