# cook your dish here
n = input()
n = n.split()

a = int(n[0])
      
i = 1 
max_el = -999
for i in range(1, a+1):
    if int(n[i]) > int(n[i + a]):
        calc = int(n[i])- int(n[i + a])
        if calc > max_el:
            max_el = calc
            flag = 1
    else:
        if (int(n[i]) - int(n[i + a])) > max_el:
            max_el = (int(n[i]) - int(n[i + a]))
            flag = 2
print(flag, max_el)
