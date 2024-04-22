def fact(num):
    fac = 1
    for i in range(2, num+1):
        fac = fac*i
    return fac

num = int(input("Enter a number: "))
num2 = num
sum = 0

while num > 0:
    a = num % 10
    sum = sum + fact(a)
    num = int(num / 10)

if num2 == sum:
    print(num2, "is a krishnamurthy number")
else:
    print(num2, "is not a krishnamurthy number")
