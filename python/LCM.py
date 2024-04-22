inputstr = input("Enter two numbers separated by a space: ")
inputlist = inputstr.split()
a = int(inputlist[0])
b = int(inputlist[1])
num = max(a, b)
i = 2
while True:
    if num % a == 0 and num % b == 0:
        print(num, "is the LCM of ", a, " and ", b)
        break
    num = max(a, b)*i
    i+=1
    