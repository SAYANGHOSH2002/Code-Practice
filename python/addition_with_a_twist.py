# Addition of two numbers a Twist
# Using a method, pass two variables and find the sum of two numbers.
# Test case:
# Number 1 – 20
# Number 2 – 20.38
# Sum = 40.38

# There were a total of 4 test cases. Once you compile 3 of them will be shown to you and 1 will be a hidden one. You have to display error message if numbers are not numeric. 

def add_numbers(num1, num2):
    try:
        sum = num1 + num2
        if isinstance(sum, int):  
            return int(sum)  
        return sum
    except TypeError:
        return "Error: Both numbers should be numeric."


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:

    num1 = int(num1) if num1.isdigit() else float(num1)
    num2 = int(num2) if num2.isdigit() else float(num2)

    print("Number 1:", num1)
    print("Number 2:", num2)

    result = add_numbers(num1, num2)
    print("Sum:", result)
except ValueError:
    print("Error: Please enter numeric values.")
