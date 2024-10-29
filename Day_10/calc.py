# This is the final project of day 10 
# Creating a calculator program.

# Defining operations sign

print("""
================================================================
                WELCOME IN MATH CALCULATIONS
================================================================   
""")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operator = {"+": add, "-": sub, "*": multiply, "/": divide}

def calculator():
    should_accumulate = True
    num1 = float(input("Type your first number?: "))

    while should_accumulate:
        for symbol in operator:
            print(symbol)
        operation_symbol = input("Choose your operation symbol: ")
        num2 = float(input("Type your second number?: "))
        result = operator[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input("Type 'y' to continue calculation with {answer}, or type 'n' to stop: ")

        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 10)

            calculator()

# Calling the function to start functioning
calculator()
