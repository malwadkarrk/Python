
# print out 0,1,2,4,5... (while loop with else)
count = 0
while count <= 10:
    print(count)
    count += 1
#    if count > 10:
#        break
else:
    print ("count value reached %d" %(count))
#-----------------------------------------------------------------------------------------------------#
# Prints out 1,2,3,4 (For loop with else)
for i in range(1,15):
    if i%5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#-----------------------------------------------------------------------------------------------------#
# print out only odd numbers using for loop
for x in range(10):
    #check if x is even
    if x % 2 == 0:
        continue
    print(x)
#-----------------------------------------------------------------------------------------------------#
# For loop to find the sum of all numbers stored in a list
#list of all numbers
numbers = [6,4,5,8,9,3,2,6,7,8,10,123]

#variable to store the sume of numbers
sum = 0

#for loop to iterate the list
for val in numbers:
    print(val)
    sum = sum + val
print("The sum is", sum)
