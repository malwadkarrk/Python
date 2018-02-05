# Check if entered number is present in the list
inputnumber = int(input("Please enter a number: "))
list1 = [1,2,4,5,6,7,'a','b']
if inputnumber in list1:
    print(inputnumber, "present in list")
else:
    print(inputnumber, "not present in list")
