password = "J"
#prompt the user for a password<<---
password = input("Enter your password: ")
#checking the length of the password
if len(password) < 3:
    print("password must be at least 3 characters")
elif len(password) > 50:
    print("password must be a maximum of 50 characters")
else:
    print("password looks good!")