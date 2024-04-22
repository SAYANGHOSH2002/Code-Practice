bi = int(input("Enter a binary number: "))
i = 0
sum = 0

while bi > 0:
    a = bi % 10
    bi = int(bi / 10)
    sum = sum + a*(2**i)
    i += 1

print(sum)