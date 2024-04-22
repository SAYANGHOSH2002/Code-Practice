num = int(input("Enter a number: "))
numstr = str(num)
numstr2 = numstr[::-1]

if numstr2 == numstr:
    print(num, "is a pallindrome number")

else:
    print(num, "is not a pallindrome number")