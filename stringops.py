# Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.
#For eg: if string is "I am here", return "Is I am here"

inputstr = input("Enter string: ")
searchstr = input("Enter search string: ")
if inputstr.find(searchstr) == -1:
    print("Is", inputstr)
else:
    print(inputstr)
