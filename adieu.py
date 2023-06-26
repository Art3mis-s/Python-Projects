import inflect

p = inflect.engine()

# creating the list to keep of names
names = []

#Loop forever
while True:
    try:
        # Get the user input
        name = input("Name: ")
        # When the user add many names then we append it
        names.append(name)
    # EOFFError is for "ctrl+d"
    except EOFError:
        # Creat new line and stop the loop
        print()
        break

# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
