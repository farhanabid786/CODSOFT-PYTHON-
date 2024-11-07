# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "not defined."
    else:
        return x / y

# Main program
while True:
    print("\nJust a Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    enter = input("Enter choice (1/2/3/4/5): ")

    if enter in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if enter == '1':
            print(f"The result is: {add(num1, num2)}")
        elif enter == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif enter == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif enter == '4':
            print(f"The result is: {divide(num1, num2)}")
    elif enter == '5':
        print("Exiting the program.\nHope you get the desired output! \nGoodbye!")
        break
    else:
        print("Invalid input.\nPlease enter a number between 1 and 5.")