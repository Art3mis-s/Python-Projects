import sys
import random
from pyfiglet import Figlet

# we can then get a list of available fonts with code like this:
figlet = Figlet()

 # we keep track if we are going to get random fonts thats why its == True
if len(sys.argv) == 1:
    isRandomFont = True
    # as   cs50 said here we know that if the user input 3 then it means that the user wat the text in a specific font
    # and by arv[1] it means that inn the terminal "figlet.py" is the 0th argument and after that whattever user inputs then its in position 1
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    # If the above conditions doesn't worked then we will exit the program via "sys.exit"
    sys.exit(1)

# we can then get a list of available fonts with code like this:
figlet.getFonts()


if isRandomFont == False:
    # If the user type in a Font that does not exist, we have to be aware of it by using try and ecept function
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
# here if we dont know what is the font that the user wanna work, so we use "random.choice" method
else:
    font = random.choice(figlet.getFonts())

str_input = input("Input: ")

print("Output: ")
print(figlet.renderText(str_input))

