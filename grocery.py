#creat an empty dictionary
grocery = {}

#using forever loop to take user's input
while True:

    try:
        #prompting the user to input
        object = input().lower()
        #checking if the object is already in the dictionary
        if object in grocery:
        #If it is, we will add 1 in the count
        #in a dictionary if we want to access the value we use the key name so here the object is the key
            grocery[object] += 1
        #otherwise, add the newely object on the list
        else:
             grocery[object] = 1
    except EOFError:
          #printing all the objects in alphabatical order
          for key in sorted(grocery.keys()):
              print(grocery[key], key.upper())
          break

