# Problem Statement: Write a code in python to take input from user about a lock combination as a string and a key
# combination as string. The first two inputs will be length of lock and length of key. Then lock and key will be taken
# as input. We need to find the minimum number of iterations we need to perform on lock string to make the key string
# look like a substring of it.
# For example-
# input
# 5 2
# 10234
# 32
# output
# 2
# Here in the lock string, we need to iterate 2 to 3 and 3 to 2 to make it 32. Therefore  number of iterations = 2.
# We could have also iterated 1 to 3 and 0 to 2. Therefore number of iterations would be = 4.
# But we need to find the minimum number of iterations.
# The digits of the lock can iterate towards both ways (0 -> 9) and (9 -> 0). 

n = input()

n = n.split()
a = int(n[0])
b = int(n[1])

s = input()
k = input()

i = 0
j = 0
min_val = 999
while i <= (a - b):
    diff = 0
    while j < b:
        diff = diff + abs(int(s[i]) - int(k[j]))
        i += 1
        j += 1
    i -= (b - 1)
    j = 0
    if diff < min_val:
        min_val = diff

print(min_val)
