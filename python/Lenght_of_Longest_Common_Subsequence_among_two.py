# Longest Common Subsequence – We have discussed Overlapping Subproblems and Optimal Substructure properties in Set 1 and Set 2 respectively. We also discussed one example problem in Set 3. Let us discuss Longest Common Subsequence (LCS) problem as one more example problem that can be solved using Dynamic Programming. LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.
# It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences between two files), and has applications in bioinformatics. 
# Examples: LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

def lcs(X, Y, m, n): 
    if m == 0 or n == 0: 
        return 0 
    elif X[m-1] == Y[n-1]: 
        return 1 + lcs(X, Y, m-1, n-1); 
    else: return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

ip1 = input("Enter String one: ")
ip2 = input("Enter String two: ")

if len(ip1) <= len(ip2):
    ips = ip1
    ipl = ip2
else:
    ips = ip2
    ipl = ip1

# ipu = []
# count = 0
# for i in range(0, len(ips)):
#     for j in range(i, len(ipl)):
#         if ips[i] == ipl[j]:
#             count += 1
#             ipu.append(ips[i])

count = lcs(ip1, ip2, len(ip1), len(ip2))

print('\nThe length is: ', count)
