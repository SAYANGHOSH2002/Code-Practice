num = int(input("Enter a number: "))
for i in range(2, int(num/2)):
    if num%i == 0:
        print(num, "is not a Prime number")
        break
    elif i == int(num/2) - 1:
        print(num, "is a Prime number")