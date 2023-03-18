#Get the user input
camelCase = input("camelCase: ")
#print "snake_case"
print("snake_case: ", end="")


#loop through every letter
for letter in camelCase:
    #check if the letter is uppercase
    if letter.isupper():
        #print underscore and the letter in lowercase
        print("_" + letter.lower(), end="")
    #otherwise, print letter
    else:
        print(letter, end="")
#print space at the end
print()