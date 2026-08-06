# Checking if a string is empty or not
username = input("Enter username: ")

if username:  # True if string is NOT empty
    print("User entered:", username)
else:         # False if user pressed Enter without typing
    print("Username cannot be empty!")
