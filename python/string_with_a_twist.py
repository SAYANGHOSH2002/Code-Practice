# The program will recieve 3 English words inputs from STDIN

# These three words will be read one at a time, in three separate line
# The first word should be changed like all vowels should be replaced by %
# The second word should be changed like all consonants should be replaced by #
# The third word should be changed like all char should be converted to upper case
# Then concatenate the three words and print them
# Other than these concatenated word, no other characters/string should or message should be written to STDOUT

# For example if you print how are you then output should be h%wa#eYOU.

# You can assume that input of each word will not exceed more than 5 chars a

s1 = input()
s2 = input()
s3 = input()
s = []

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in s1:
    if i in vowels:
        s.append('%')
    else:
        s.append(i)

for j in s2:
    if j not in vowels:
        s.append('#')
    else:
        s.append(j)

s.append(s3.upper())

for i in s:
    print(i, end = '')


