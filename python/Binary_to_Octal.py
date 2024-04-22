num = input('Enter the binary number: ')
# p = len(num)
# sum = 0

# for i in num:
#     p -= 1
#     print(i)
#     sum = sum + (int(i)) * (8 ** p)
#     print(' ', sum)
c = int(num)
s = 0
b = 1

while(c != 0):
     r = c % 10
     s = s + r * b
     c = c // 10
     b = b * 2

oct = 0
i = 0
while(s > 0):
     a = s % 8
     s = s // 8
     oct = oct + a * (10 ** i)
     i += 1


print('The equivalent octal number is:', oct)