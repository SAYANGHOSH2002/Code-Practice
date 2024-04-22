inputstr = input('Enter three space separated integers: ')

inputlist = inputstr.split()

a = int(inputlist[0])
b = int(inputlist[1])
c = int(inputlist[2])

num = min(a, b, c)

for i in range(num, 0, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print('The GCD of the given numbers is:', i)
        break

n = max(a, b, c)
num = 0
while True:
    num = num + n
    if num % a == 0 and num % b == 0 and num % c == 0:
        print('The LCM of the given numbers is:', num)
        break
    