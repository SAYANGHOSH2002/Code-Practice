# cook your dish here
import math

t = int(input())
t1 = [0 for i in range(t)]
t2 = [0 for i in range(t)]
tmin = [0 for i in range(t)]

for i in range (t):
    istr = input()

    il = istr.split()
    l = int(il[0])
    v1 = int(il[1])
    v2 = int(il[2])

    t1[i] = math.ceil(l/v1)
    t2[i] = math.ceil(l/v2)
    
    if t1[i] <= t2[i]:
        tmin[i] = -1
    
    else:
        tmin[i] = t1[i] - t2[i] - 1

for i in range(t):
    print(tmin[i])