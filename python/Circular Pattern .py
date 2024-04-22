def print_pattern(N):
    pattern = [[0 for _ in range(N)] for _ in range(N)]

    num = 1
    left, right, top, bottom = 0, N - 1, 0, N - 1

    while num <= N * N:
        for i in range(left, right + 1):
            pattern[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            pattern[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            pattern[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            pattern[i][left] = num
            num += 1
        left += 1

    for row in pattern:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == "__main__":
    N = int(input())  
    print_pattern(N)
