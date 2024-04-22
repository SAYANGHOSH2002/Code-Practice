# A Pythagorean triplet is a set of three integers a, b and c such that a2 + b2 = c2. Given a limit, generate all Pythagorean Triples with values smaller than given limit. 
# Input : limit = 20 
# Output : 
# 3 4 5 
# 8 6 10 
# 5 12 13 
# 15 8 17 
# 12 16 20

import math

def square_root(c):
    sqrt_n = math.isqrt(c)
    return sqrt_n * sqrt_n == c

limit = int(input('Limit: '))

# a = 1
# b = 2

for a in range(1, limit):
    for b in range(a, limit):
        sum = ((a*a) + (b*b))
        if square_root(sum) and math.sqrt(sum) <= limit:
            print(a, b, int(math.sqrt(sum)), '\n')
    
