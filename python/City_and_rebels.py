# In a kingdom with 
#  cities connected by 
#  roads, the king's palace is located in the first city. Each city has a specific number of guards, given in an array 
# , where 
#  is the number of guards in the city 
# . The kingdom must assess the risk of revolts starting from any city and how close rebels could get to the king's palace. The guards' effectiveness is such that one guard can stop one rebel. 

# To tackle this, the king has asked you to develop a method for analyzing such scenarios. This includes answering queries of type 'query(
# , 
# )', where 
#  represents the city where the revolt might begin, and 
#  indicates the number of protestors at the start. Your task is to determine for each query the nearest city to the king's palace (i.e., city 1) that the rebels can reach.

# Note: If the rebels can reach City 1, you should print City 1, as this is the city where the King's palace is located.

# Input format

# The first line contains a single integer 
# , which denotes the number of test cases.
# For each test case:
# The first line contains 
#  denoting the number of Cities.
# The following 
#  lines contain 2 space-separated integers, 
#  & 
#  indicating that there is a road between City 
#  & City 
 
# The next line contains N integers, denoting the array Guards.
# The next line contains 
#  denoting the number of queries.
# The next 
#  lines contain 2 space-separated integers, 
#  and 
# , where 
#  denotes the city where the revolt might begin, and 
#  indicates the number of rebels at the start.
# Output format

# For each test case, answer all the 
#   queries. For each query, print in a new line the nearest city to the king's palace (i.e., city 1) that the rebels can reach.

# Constraints


# Sample Input
# 1
# 7
# 1 2
# 1 5
# 2 3
# 5 6
# 5 7
# 3 4
# 5 3 2 4 6 4 4
# 3
# 4 10
# 6 10
# 7 2
# Sample Output
# 1
# 5
# 7
# Time Limit: 2
# Memory Limit: 512
# Source Limit:
# Explanation
# The first line denotes T = 1.

# For test case 
# :

# We are given:

# N = 7, and the city connection looks like this:
                

# Guards in each of the cities are : 
# We need to answer 3 queries.
# Now,

# For the first query, 10 rebels start from city 10. 
# out of 10, 6 rebels can reach City 3, 2 rebels will be stopped at City 3 & 4 can reach City 2, 3 rebels will be stopped here & 1 can reach City 1. Hence, the answer to this query is 1.
# For the second query, 10 rebels start from city 6. 
# out of 10, 6 rebels can reach city 5, and 0 can reach city 1, as all 6 rebels will be stopped at city 5. Hence the answer for this query is 5.
# For the second query, 3 rebels start from city 7. 
# out of 2, 0 can reach city 5, as all 3 rebels will be stopped at city 7. Hence the answer for this query is 7.

#incomplete

n = int(input())
cities = int(input())

# a = []
# b = []
c = [[0 for i in range(cities)] for i in range(cities)]

for i in range(cities):
    for j in range(cities):
        c[i][j] = 0

for i in range(cities):
    a, b = input().split()
    c[int(a)-1][int(b)-1] = 1

guards = input()
guards_list = guards.split()

int_list = [int(num) for num in guards_list]

p = 0
for i in range(cities):
    for j in range(cities):
        if c[i][j] == 1:
            c[i][j] = int_list[p]
            p+=1

q = int(input())
a = []
b = []

for i in range(q):
    a[i], b[i] = input().split()

