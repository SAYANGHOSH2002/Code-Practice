# Given an array of integers and a sum, the task is to count all subsets of given array with sum equal to given sum. 
# Input :  

# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the sum. 

# Output : 

# Count all the subsets of given array with sum equal to given sum. 

# NOTE: Since result can be very large, print the value modulo 109+7. 

# Constraints : 

# 1<=T<=100 

# 1<=n<=103 

# 1<=a[i]<=103 

# 1<=sum<=103 

# Example : 

# Input : 

# 2 

# 6 

# 2 3 5 6 8 10 

# 10 

# 5 

# 1 2 3 4 5 

# 10 

# Output : 

# 3 

# 3 

# Explanation : 

# Testcase 1: possible subsets : (2,3,5) , (2,8) and (10) 

# Testcase 2: possible subsets : (1,2,3,4) , (2,3,5) and (1,4,5)

n = int(input())
ar = input()
ar = ar.split()
sum = int(input())

for i in range(len(ar)):
    ar[i] = int(ar[i])

count = 0
# e = 0

for i in range(len(ar)):
    if ar[i] == sum:
        count += 1

# # for i in range(len(ar) - 1):
# #     for j in range(i + 1, len(ar)):
# #         if ar[i] + ar[j] == sum:
# #             count += 1

p = len(ar) - 1
for i in range(p):
    for j in range(i + 1, len(ar)):
        total = ar[i]
        for k in range(i + 1, j):
            total = total + ar[k]
            print(i, j, k, total)
        if sum == total:
            count += 1
        total = ar[i]
        for k in range(j, i + 1, -1):
            total = total + ar[k]
            print(i, j, k, total)
            if total == sum:
                count += 1

# for i in range(len(ar)):
# for j in range(0, len(ar)):
#     total = 0
#     for k in range(0, j):
#         total = total + ar[k]
#         print('(i, j) i = ', i, 'j = ', j, 'k = ', k, 'total = ', total)
#     if total == sum:
#         count += 1
#     total = 0
#     for k in range(j, 0, -1):
#         total = total + ar[k]
#         print('(j, i, -1) i = ', i, 'j = ', j, 'k = ', k, 'total = ', total)
#         if total == sum:
#             count += 1            


print(count)
