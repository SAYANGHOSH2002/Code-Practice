n = 4
for i in range(5):
    j = 0
    while j < 9:
        if j <= (n+i) and j >= (n-i):
            print("* ", end = '')
            j+=2
        else:
            print(" ", end = '')
            j+=1
    print()