a = 0
print(1)
for i in range(4):
    for j in range(7):
        if j >= (3-i) and j <= (3+i) and a <= 10:
                print(a, end = ' ')
                a += 1
        else:
            print(' ', end = ' ') 
    print()
