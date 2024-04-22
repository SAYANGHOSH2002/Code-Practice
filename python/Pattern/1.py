for i in range(4):
    a = 0
    for j in range(7):
        if j >= (3-i) and j <= (3+i):
            if j <= 3:
                a += 1
                print(a, end = ' ')
            else:
                a -= 1
                print(a, end = ' ')
        else:
            print(' ', end = ' ') 
    print()

