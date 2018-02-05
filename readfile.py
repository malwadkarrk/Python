from sys import argv
script, filename = argv
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

#Take file name as input
file_again = input("Enter your filename: ")
txt_again = open(file_again)
print(txt_again.read())
