s = input()
s = str(s)
print(s)
r = s
i = 0
j = len(s)
flag = 1
while True:
    if s[i] != r[j]:
        print("Not Pallindrome")
        flag = 0
        break
    while j >= i:
        i += 1
        j -= 1
if flag == 1:
    print("Pallindrome")