inputstr = input("Enter two numbers separated by a space: ")
inputlist = inputstr.split()
a = int(inputlist[0])
b = int(inputlist[1])
i = min(a, b)
while i > 0:
    if a % i == 0 and b % i == 0:
        print(i, "is the GCD of", a, "and", b)
        break
    i-=1
