# 1! + 2! + 3! + ....

def fact(a):
    mul = 1
    while a > 1:
        mul = mul * a
        a -= 1
    return mul

n = int(input("Enter how many numbers: "))
sum = 0

for i in range(1, n+1):
    print(i, "!", end = '')
    if i < n:
        print(" + ", end = '')
    sum = sum + fact(i)

print("\nThe sum is: ", sum)