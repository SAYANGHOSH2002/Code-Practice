# 1^x + 2^x + 3^x + ...

n = int(input("Enter how many numbers: "))
x = int(input("Enter the exponent: "))
sum = 0

for i in range(1, n+1):
    print(i, "^", x, end = '')
    if i < n:
        print(" + ", end = '')
    sum = sum + i ** x

print("\nThe sum is: ", sum)