a = [2,4,6,10,12]

# Sum of elements in list
print ("The sum of list a is: ", sum(a))

# Multiply all the elements in list
total = 1
for each in a:
    total = total * each
print("Multiplication of elements in list is: ", total)

# Largest number in list
print ("Largest number in list a is: ", max(a))

# Smallest number in list
print ("Smallest number in list a is: ", min(a))

# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
list1 = ['abc', 'xyz', 'aba', '1221']

count = 0
for i in list1:
    if len(i) >= 2:
        if i[0] == i[-1]:
            count = count + 1
            print(i)
print("Total number of strings are: ", count)

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
list2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2.pop(0)
list2.pop(3)
list2.pop(3)
print(list2)

# Write a Python program to print the numbers of a specified list after removing even numbers from it.
b = [0,1,2,3,4,5,6,7,8,9,8,6]
c = []
for each in b:
    if each%2 != 0:
        c.append(each)
print(c)

# Python program to shuffle and print a specified list
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,])))

# Python program to find the index of an item in a specified list.
c = [12,'abc',34,65]
print(c.index(34))

# Python program to append a list to the second list.
list1 =  [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
print(list1 + list2)

list1 =  [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
list1.append(list2)
print(list1)

list1 =  [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
list1.extend(list2)
print(list1)

# Python program to select an item randomly from a list.
from random import choice
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(choice(color_list))


# python program to check whether two lists are circularly identical
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('Compare list1 and list2')
print(' '.join(map(str,list2)) in ' '.join(map(str,list1 *2)))

print('Compare list1 and list3')
print(' '.join(map(str,list3)) in ' '.join(map(str,list1 *2)))

# Python program to find the largest, 2nd Largest, Smallest and 2nd Smallest number in a list.
number = [8, 12, 3, -1,-2]
largest = number[0]
largest2 = number[0]
lowest = number[0]
lowest2 = number[0]

number.sort()
print(number)

print("Largest element is:", number[-1])
print("Smallest element is:", number[0])
print("Second Largest element is:", number[-2])
print("Second Smallest element is:", number[1])

# Python program to get unique values from a list
list1 = [10, 20, 10, 30, 40, 40]
unique_list = list(set(list1))
print(unique_list)

# Write a Python program to find common items from two lists
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(set(color1) & set(color2))

list1 = [1,4,7,9]
list2 = [1,2,3,4,5,6,7,8]
print(set(list1) & set(list2))

# Write a Python program to convert a list of multiple integers into a single integer.
list1 = [11, 33, 50]
string = " "
int_string = 0
for i in list1:
    string = string + str(i)
string.strip()
print(string)
int_string = int(string)
print(int_string)
