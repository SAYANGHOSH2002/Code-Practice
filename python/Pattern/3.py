for i in range(4):
    for j in range(7):
        if i > 0 and j >= (4-i) and j <= (2+i):
            print(" ", end = '')
        else:
            print("*", end = '')
    print()