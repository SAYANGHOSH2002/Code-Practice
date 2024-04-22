num = int(input("Enter a number: "))
count = 0
sum = 0

while num > 0:
    a = num % 10
    num = num // 10
    count += 1
    sum = sum + a

print("The number of digits: ", count, "\nThe sum of digits: ", sum)