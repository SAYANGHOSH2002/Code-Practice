# 1 + 5 + 9 + 13 + ...

n = int(input("Enter upto which number you want to add: "))
i = 1
sum = 0

while i <= n:
    print(i, end = '')
    if i < n-3:
        print(" + ", end = '')
    sum = sum + i
    i += 4

print("\nThe sum is: ", sum)