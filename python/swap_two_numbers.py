inputstr = input("Enter the numbers separated by space: ")
inputlist = inputstr.split()

print("Before swap: a = ", inputlist[0], ", b = ", inputlist[1])
a = int(inputlist[0])
b = int(inputlist[1])

a = a + b
b = a - b
a = a - b

print("Before swap: a = ", a, ", b = ", b)