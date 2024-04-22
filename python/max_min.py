inputstr = input("Enter the numbers separated by space: ")
inputlist = inputstr.split()

max = inputlist[0]
min = inputlist[0]

for i in range(0, len(inputlist)):
    if inputlist[i] > max:
        max = inputlist[i]
    if inputlist[i] < min:
        min = inputlist[i]

print("The max value of the list is: ", max, "\nThe min value of the list is: ", min)
