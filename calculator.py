print("Welcome to Calculator in Python")

# This function adds two numbers
def add(x,y):
    return x + y

# This function substract two numbers
def substract(x,y):
    return x-y

# This function multiply two numbers
def multiply(x,y):
    return x*y

# This function divide two numbers
def divide(x,y):
    return x/y

print("Select Operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# Take input from user
choice = int(input("Enter Choice(1/2/3/4): "))

if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "-", num2, "=", substract(num1,num2))
elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Invalid Input")
