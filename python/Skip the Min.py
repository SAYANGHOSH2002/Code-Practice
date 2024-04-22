# cook your dish here
def total_sum(arr1):
    a = True
    total = 0
    print(min(arr1))
    for j in range(len(arr1)):
        print(arr1[j])
        if arr1[j] == min(arr1) and a == True:
            a = False
        else:
            print(total, end = ' ')
            total = total + int(arr1[j])
            print(total)
    return total
    
n = int(input())
arr = [0 for i in range(n)]

for i in range(n):
    d = int(input())
    arr1 = input().split()
    for j in range(len(arr1)):
        arr1[j] = int(arr1[j])
    arr[i] = total_sum(arr1)
    
for i in range(n):
    print(arr[i])
