inputstr = input("Enter the numbers separated by a space: ")
inputlist = inputstr.split()

for i in range (0, len(inputlist)):
    for j in range(i, len(inputlist)-1):
        if inputlist[j+1] < inputlist[j]:
            temp = inputlist[j+1]
            inputlist[j+1] = inputlist[j]
            inputlist[j] = temp
            #swap(inputlist[j+1], inputlist[j])

print("After sorting: ")
for i in inputlist:
    print(i, " ",end = '')