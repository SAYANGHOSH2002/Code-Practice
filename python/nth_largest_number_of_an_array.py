arr = input('Enter the array elements separated by space: ')
n = int(input('Enter the value of n: '))

arr = arr.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

arr = sorted(arr)

print('The', n, 'largest value of the given array is: ', arr[n - 1])