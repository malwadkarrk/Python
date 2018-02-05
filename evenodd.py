#Write a Python program to find whether a given number (accept from the user) is even or odd,
#print out an appropriate message to the user.
inputnumber = int(input("Please enter a number: "))
if (inputnumber%2 == 0):
    print(inputnumber, "is an even number")
else:
    print(inputnumber, "is an odd number")
