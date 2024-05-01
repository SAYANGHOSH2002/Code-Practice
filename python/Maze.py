# Define a square Maze
# take the length as input
# then add 0s or 1s 
# 0 means clear way and 1 means obstacles
# you need to find the optimized path to go to the co-ordinates = [ length - 1, length - 1 ] from [0, 0]
# P.T.B.N. -  You can only move in either right or bottom direction


moves = []
visited = []

length = int(input('Enter the dimension of the Maze: '))
maze = [[0 for j in range(length)] for i in range(length)]

def check_square(r, c):
    if maze[r][c] == 0:
        return True
    return False

def calc(i, j):

    if i == length - 1 and j == length - 1:
        print(moves)
        return
    
    else:

        if i < length - 1 and check_square(i + 1, j):
            moves.append('d')
            calc(i + 1, j)
            moves.pop()

        elif j < length - 1 and check_square(i, j + 1):
            moves.append('r')
            calc(i, j + 1)
            moves.pop()

        # if moves[-1] == 'r':
        #     j -= 1
        #     i += 1
        #     print(i, j)
        #     if i == -1 or j == -1:
        #         print('Path Not Found')
        #         return
        #     elif check_square(i, j):
        #         calc(i, j)
        #         moves.pop()

        # elif moves[-1] == 'd':
        #     i -= 1
        #     j += 1
        #     print(i, j)
        #     if i == -1 or j == -1:
        #         print('Path Not Found')
        #         return
        #     elif check_square(i, j):
        #         calc(i, j)
        #         moves.pop()
    
    


print('Enter the maze values')

for i in range(length):
    for j in range(length):
        maze[i][j] = int(input())

for i in range(length):
    for j in range(length):
        print(maze[i][j], end  = ' ')
    print('\n')


calc(0, 0)
    

    
