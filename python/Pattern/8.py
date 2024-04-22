n = 4
N = int(input())
for i in range(N):
    j = 0
    a = 11 ** i
    while j < 9:
        if j <= (n+i) and j >= (n-i):
            b = a % 10
            a = int(a / 10)
            print(b,"", end = '')
            j+=2
        else:
            print(" ", end = '')
            j+=1
    print()