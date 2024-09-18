try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Catching Specific Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Handling Multiple Exceptions in One Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero.")

#Catching All Exceptions
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

#Finally Block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()
    print("File closed.")

#Else Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input!")
else:
    print(f"Result is {result}")
finally:
    print("Execution complete.")


#Raising Exceptions Manually
def check_positive(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")
    return number

try:
    result = check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")
