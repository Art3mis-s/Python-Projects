import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleas type a number larger than 0 next time.")
        quit()
else:
    print("Pleas type a number next time.")
    quit()

#randint will include 11 as well whe reas randrange() will not include the number itself
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses +=1
    #it will run the below lines of codes until its true
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Pleas type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        #if the guess is right it will immediately break the loop
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")