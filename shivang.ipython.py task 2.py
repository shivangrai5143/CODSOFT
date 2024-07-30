# Simple Calculator Program

def calculator():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation. Please enter +, -, * or /.")
        return

    # Display the result
    print("The result is:", result)

# Call the calculator function
calculator()