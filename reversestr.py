# Write a Python program which accepts the user's first and last name
#and print them in reverse order with a space between them.
firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")
print("Reverse of full name name is",firstname[::-1] + ' ' + lastname[::-1])

fullname = firstname + ' ' + lastname
print("Reverse of full name is",fullname[::-1])
