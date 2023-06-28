print("Hey there! Welcome to this Game!😃")

playing = input("In this game I have some very good questions from you, So do you want to play?🤔  ")

if playing.lower() != "yes":
    quit()

print("Cool! Let's play 😀")

score = 0

answer = input("Which command is use to change the directory? ")

if answer.lower() == "cd":
    print("Perfect!")
    score += 1
else:
    print("Hmm try one more time!")

answer = input("How to list files and directories in the current directory? ")

if answer.lower() == "ls":
    print("Amazing!")
    score += 1
else:
    print("Hmm try one more time!")

answer = input("How to create a new directory? ")

if answer.lower() == "mkdir":
    print("Correct!")
    score += 1
else:
    print("Hmm try one more time!")

answer = input("How to remove a file or directory? ")

if answer.lower() == "rm":
    print("Perfect!")
    score += 1
else:
    print("Hmm try one more time!")

answer = input("How to open a file or folder in VSCode? ")

if answer.lower() == "code":
    print("Perfect!")
    score += 1
else:
    print("Hmm try one more time!")


print("You got " + str(score) + " questions correct")
print("You got " + str(score/5 * 100) + "%.")