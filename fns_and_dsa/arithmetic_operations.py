# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# main.py

from arithmetic_operations import perform_operation

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation)

if isinstance(result, str) and result.startswith("Error"):
    print(f"Operation failed: {result}")
else:
    print(f"The result of the operation is: {result}")

