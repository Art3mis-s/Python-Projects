#Get user input
user_input = input("Input: ")
#print "Output: "
print("Output: ", end="")

#Looping through every letter
for letter in user_input:
    #Check if its not a vowels whether inputed lowercase or uppercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        #print the letter
        print(letter, end="")

#add a new line
print()