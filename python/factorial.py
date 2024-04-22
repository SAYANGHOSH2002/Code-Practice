def fact(num):
    mul = 1
    for i in range(1, num+1):
        mul = mul*i
    return mul
num = int(input("Enter a number:"))
factorial = fact(num)
print("Factorial of", num, "is", factorial)