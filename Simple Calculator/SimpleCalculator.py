#Define Functionality

#Addition
def add(x, y):
    return x + y
#Subtraction
def subtract(x, y):
    return x - y
#Multiplication
def multiply(x, y):
    return x * y
#Division
def divide(x, y):
    return x / y

#Operations
print("Select operation from:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    #Take user input
    choice = input("Enter a number from 1-4: ")

    #Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        numberOne = float(input("Enter first number: "))
        numberTwo = float(input("Enter second number: "))

        #Mathematical functionality
        if choice == '1':
            print(numberOne, "+", numberTwo, "=", add(numberOne,numberTwo))

        elif choice == '2':
            print(numberOne, "-", numberTwo, "=", subtract(numberOne,numberTwo))

        elif choice == '3':
            print(numberOne, "*", numberTwo, "=", multiply(numberOne,numberTwo))

        elif choice == '4':
            print(numberOne, "/", numberTwo, "=", divide(numberOne,numberTwo))
        break
    else:
        print("Invalid Input")