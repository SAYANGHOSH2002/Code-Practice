import array
arr = array.array('i')

dec = int(input("Enter a decimal number: "))

while dec > 0:
    a = dec % 2
    dec = int(dec / 2)
    arr.append(a)

arr = arr[::-1]
for i in arr:
    print(i, end = '')
