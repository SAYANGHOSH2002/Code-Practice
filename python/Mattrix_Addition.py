rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of columns: '))

arr1 = [[0 for j in range(cols)] for i in range(rows)]
arr2 = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        # a = int(input())
        # arr1.append(a)
        arr1[i][j] = int(input())

print(arr1)

for i in range(rows):
    for j in range(cols):
        # a = int(input())
        # arr2.append(a)
        arr2[i][j] = int(input())

print(arr2)

for i in range(rows):
    for j in range(cols):
        arr1[i][j] = arr1[i][j] + arr2[i][j]

print(arr1)

for i in range(rows):
    for j in range(cols):
        print(arr1[i][j], end=' ')
    print()