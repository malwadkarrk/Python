#rite a Python program to get the difference between a given number and 17,
#if the number is greater than 17 return double the absolute difference.

inputnumber = int(input("Enter any number: "))
seventeen = 17
diff = inputnumber - seventeen
if diff > seventeen:
    print("Difference is greater then 17, hence (difference * 2): ", diff * 2)
else:
    print("Difference of " + str(inputnumber) + "-" + str(seventeen) + " is: ", diff)
