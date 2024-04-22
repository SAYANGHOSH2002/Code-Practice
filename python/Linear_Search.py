n = int(input("Enter the number of elements: "))
inputstr = input("Enter the numbers separated by a space: ")
inputlist = inputstr.split()

num = int(input("Enter a number to find: "))
j = 0
flag = 0

for i in range(0, len(inputlist)):
    if num == int(inputlist[i]):
        print(num, "has appeared at index number", i)
        flag = 1

if flag == 0:
    print(num, "was not found")