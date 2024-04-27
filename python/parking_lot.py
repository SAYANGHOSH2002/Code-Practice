# A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).

# Note :
# RxC- Size of the matrix
# Elements of the matrix M should be only 0 or 1.

# Example 1:
# Input :
# 3   -> Value of R(row)
# 3    -> value of C(column)
# [0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
# Output :
# 3  -> Row 3 has maximum number of 1’s

# Example 2:
# input :
# 4 -> Value of R(row)
# 3 -> Value of C(column)
# [0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
# Output :
# 4  -> Row 4 has maximum number of 1’s

r = int(input())
c = int(input())
p_lot = [[0 for j in range(c)] for i in range(r)]

for i in range(r):
    for j in range(c):
        p_lot[i][j] = int(input())

max = -99
max_row = 0
for i in range(r):
    count = 0
    for j in range(c):
        if p_lot[i][j] == 1:
            count += 1
    if count > max:
        max = count
        max_row = i

print(max_row + 1)

