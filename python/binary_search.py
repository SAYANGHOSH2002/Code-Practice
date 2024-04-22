def binarySearch(s1, s2, num, arr):
    i = (s1 + s2) // 2
    if arr[i] == num:
        print("\nElement found at", i, "th index")
    elif arr[i] >= num and i > 0:
        binarySearch(s1, i, num, arr)
    elif arr[i+1] <= num and s1 < (s2-1):
        binarySearch(i+1, s2, num, arr)
    else:
        print("\nElement not found")

n = int(input("Enter the number of elements: "))
arr = [0 for i in range(n)]
print("Enter the elements: ")
for i in range(n):
    arr[i] = int(input())
num = int(input("Enter the element to find: "))

arr.sort()
print("Sorted array: ")
for i in range(n):
    print(arr[i], end = " ")
binarySearch(0, n-1, num, arr)
