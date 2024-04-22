for i in range(4):
    a = 64
    for j in range(7):
        if j >= (3-i) and j <= (3+i):
            if j <= 3:
                a += 1
                print(chr(a), end = ' ')
            else:
                a -= 1
                print(chr(a), end = ' ')
        else:
            print(' ', end = ' ') 
    print()
