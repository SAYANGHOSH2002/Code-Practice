# sum of prime numbers
# need to check

def prime(a):
    for i in range(2, int(a/2)):
        if a%i == 0:
            return 0
        elif i == int(a/2) - 1:
            return a

n = int(input("Enter upto which number you want to add: "))
num = 1
sum = 0

while num <= n:
    for i in range(2, int(num/2)):
        if num%i == 0:
            break
        elif i == int(num/2) - 1:
            sum = sum + num
    num += 1

print("\nThe sum is: ", sum)