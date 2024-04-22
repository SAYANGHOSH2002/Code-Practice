# need to ber checked

num = int(input("Enter a number: "))
numstr = str(num)
num2 = num
n = len(numstr)
sum = 0

while num > 0:
    a = num % 10
    sum = sum + a**n
    num = int(num / 10)

if num2 == sum:
    print(num2, "is an armstrong number")
else:
    print(num2, "is not an armstrong number")