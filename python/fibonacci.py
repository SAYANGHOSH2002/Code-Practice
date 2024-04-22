#n = int(input("Enter how many numbers you want to see in fibonacci series: "))
n = int(input("Enter upto which you want to see the fibonacci series: "))
a = 0
b = 1
print(a, b, end = ' ')
i = 0

# while i < (n-2):
#     temp = b
#     b = b + a
#     a = temp
#     print(b, end = ' ')
#     i+=1

while (a + b) < n:
    temp = b
    b = b + a
    a = temp
    print(b, end = ' ')