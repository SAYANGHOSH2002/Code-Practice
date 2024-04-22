# x^m + x^m+1 + x^m+2 + ...

print("The series is: x^m + x^m+1 + x^m+2 + ... + x^m+n \nEnter values of x, m and n respectively")
x = int(input("x: "))
m = int(input("m: "))
n = int(input("n: "))

sum = 0

for i in range(0, n+1):
    print(x, "^", (m+i), end = '')
    if i < n:
        print(" + ", end = '')
    sum = sum + x ** m+i

print("\nThe sum is: ", sum)