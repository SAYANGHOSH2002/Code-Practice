# 1^2 + 2^2 + 3^2 + ...

n = int(input("Enter how many numbers: "))
sum = 0

for i in range(1, n+1):
    print(i, "^2", end = '')
    if i < n:
        print(" + ", end = '')
    sum = sum + i ** 2

print("\nThe sum is: ", sum)