# Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

# Examples:

# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.

def true_false(s1, s2):
    for i in s1:
        if i not in s2:
            return False
        
    for j in s2:
        if j not in s1:
            return False
    return True

s1 = input()
s2 = input()

s_already = []
s1_count = []

for i in range(0, len(s1)):
    if s1[i] not in s_already:
        count = 0
        for j in range(i, len(s1)):
            if s1[j] == s1[i]:
                count += 1
        s1_count.append(count)
        s_already.append(s1[i])

s1_count.sort()

s_already = []
s2_count = []

for i in range(0, len(s2)):
    if s2[i] not in s_already:
        count = 0
        for j in range(i, len(s2)):
            if s2[j] == s2[i]:
                count += 1
        s2_count.append(count)
        s_already.append(s2[i])

s2_count.sort()

if s1_count == s2_count and true_false(s1, s2):
    print('true')
else:
    print('false')