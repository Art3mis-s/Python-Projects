while True:
    fuel = input("Fraction: ")

    try:
        #spliting the fuel
        numerator, denumerator = fuel.split("/")
        #converting the numerator and denumerator to integers
        numerator = int(numerator)
        denumerator = int(denumerator)

        #calculating the percentage
        fraction = numerator / denumerator
        #checking if its less than 1 and then stop the loop
        if fraction <= 1:
            break
    except(ValueError, ZeroDivisionError):
        # here we use pass bcz this way we're gonna prompt the user again for a new input and the try and except will repeat
        pass

#Multiplying the percentage by 100
percentage = int(fraction * 100)
#checking if percentage is less than 1, so then print E
if percentage <= 1:
    print("E")
#else if the percentage is greater than 99, so then print F
elif percentage >= 99:
    print("F")
#otherwise, print the %, so we will use "formated string" aka: fstring
else:
    print(f"{percentage}%")

