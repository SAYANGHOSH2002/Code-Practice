# Problem Statement –

# Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

# Constrains-

# 1<=N<=100

# Example 1:

# Input :

# 10  -> Integer

# Output :

# 5    -> result- Integer

# Explanation:

# Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.

n = int(input())
sum = 0
i = 0

while(n > 0):
    a = n % 2
    n = n // 2
    sum = sum + a*pow(10, i)
    i += 1

s = str(sum)
c = []

for i in s:
    if i == '0':
        c.append(1)
    else:
        c.append(0)

sum = 0
p = len(s) - 1
for i in c:
    if i == 1:
        sum = sum + pow(2, p)
    p -= 1

print(sum)