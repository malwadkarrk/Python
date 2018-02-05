# Write a Python program to accept a filename from the user
#and print the extension of that.

filename = input("Enter the file name: ")
extension = filename.split(".")[-1]
print("Extension of file" , filename +  " is: " + extension)
