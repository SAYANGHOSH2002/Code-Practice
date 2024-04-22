def maxElements(m, n, grid):
    count = 0
    for i in range (0, m):
        maX = []
        for j in range (0, n):
            if i - 1 >= 0:
                maX.append(grid[i-1][j])
                if j - 1 >= 0:
                    maX.append(grid[i-1][j-1])
                if j+1 < n:
                    maX.append(grid[i-1][j+1])
            if j - 1 >= 0:
                maX.append(grid[i][j-1])
            if i + 1 < m:
                maX.append(grid[i+1][j])
                if j - 1 >= 0:
                    maX.append(grid[i+1][j-1])
                if j+1 < n:
                    maX.append(grid[i+1][j+1])
            if j + 1 < n:
                maX.append(grid[i][j+1])
            if grid[i][j] > max(maX):
                print("Max Element: ", grid[i][j], " Neighbours: ", maX)
                count += 1
            maX.clear()

    return count
                
m = int(input())
n = int(input())

grid = [[0 for j in range (n)] for i in range (m)]

for i in range (0, m):
    for j in range (0, n):
        grid[i][j] = int(input())

for i in range (0, m):
    for j in range (0, n):
        print(grid[i][j], end = ' ')
    print()

c = maxElements(m, n, grid)
print("The number of max elements is: ", c)
