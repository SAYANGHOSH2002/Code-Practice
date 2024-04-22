num = int(input("Enter a number: "))
sum = 0
for i in range(1, int(num/2)+1):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")