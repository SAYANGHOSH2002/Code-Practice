# Find the Position of a Substring within a String


# 3

# 0
# In this article we will solve the most asked interview question: "Find the Position of a Substring within a String"

# Problem statement: “Given two strings text and pattern find the first occurrence of str1 in str2 if found print it’s index if not found print -1.”

# Examples:

# Example 1:
# Input: str1 = "takeuforward"
#        str2 = “forward”
# Output: 5
# Explanation: "Forward" is present in the 5th index in "takeuforward"

# Example 2:
# Input: str1 = “hello”
#        str2 = “az”
# Output: -1
# Explanation: "az" is not a substring of "hello"

s1 = input()
s2 = input()

if s2 in s1:
    for i in range(len(s1)):
        if s1[i:i + len(s2)] == s2:
            print(i)

else:
    print(-1)
