# Write a Python program to print the numbers of a specified list after removing even numbers from it.
b = [0,1,2,3,4,5,6,7,8,9,8,6]
c = []
for each in b:
    if each%2 != 0:
        c.append(each)
print(c)
