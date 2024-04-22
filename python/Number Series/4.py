# sum of odd numbers

n = int(input("Enter upto which number you want to add: "))
i = 1
sum = 0

while i <= n:
    print(i, end = '')
    if i < n-1:
        print(" + ", end = '')
    sum = sum + i
    i += 2

print("\nThe sum is: ", sum)