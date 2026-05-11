# - - -
# - -
# - 

# Function used to ask the user for two numbers
def ask_numbers():
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        return num1, num2

    except ValueError:
        print("Error: Enter valid numbers")
        return None, None

# Addition function
def addition():
    num1, num2 = ask_numbers()
    
     # Check for input errors
    if num1 is None:
        return None

    result = num1 + num2

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")
    return f"{num1} + {num2} = {result}"

# Subtraction function
def subtraction():
    num1, num2 = ask_numbers()

    if num1 is None:
        return None

    result = num1 - num2

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")
    return f"{num1} - {num2} = {result}"

# Multiplication function
def multiplication():
    num1, num2 = ask_numbers()

    if num1 is None:
        return None

    result = num1 * num2

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")
    return f"{num1} x {num2} = {result}"

# Division function
def division():
    num1, num2 = ask_numbers()

    if num1 is None:
        return None

    try:
        result = num1 / num2

        if result.is_integer():
            result = int(result)

        print(f"Result: {result}")
        return f"{num1} / {num2} = {result}"
    
    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

