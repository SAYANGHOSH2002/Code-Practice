n = int(input())
word = input()

#i = 0
#j = 1
#while i < (n-1):
max_len = 0
new_str = ' '
for i in range (0, (n-1)):
    #while j <= n:
    for j in range (1, n+1):
        sub_string = word[i:j]
        if sub_string == sub_string[::-1]:
            if (j - i) > max_len:
                new_str = sub_string
                max_len = j - i
#        j += 1
#   i += 1
    
print(max_len)
print(new_str)
