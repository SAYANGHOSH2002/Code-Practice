# Question -: Consider a set of web pages, numbered from 1 to N. Each web page has links to one or more web pages. Clicking on a link in a page, takes one to the other web page. You are provided numbers of two web pages viz, starting web page and end web page. Your task is to find the minimum number of clicks required to reach the end page from the start page. If end page cannot be reached from start page, print -1 as the output. For better understanding refer Examples section.

# Constraints

# 0 < N <= 100

# 0 < L < 10

# Input

# First line contains an integer N denoting number of web pages.

# Next N lines contain L space separated integers depicting linked webpage number(s) from that webpage

# Output

# Print the minimum number of clicks required to open the end page from start page. If not possible, print -1 as output.

# Time Limit (secs)

# 1

# Example 1

# Input

# 5

# 2 4

# 1

# 1 5

# 2 3

# 5

# 2 3

# Output

# 3

# Explanation:

# First line conveys that there is total 5 pages.

# Second line conveys that there are links from page 1 to pages 2 and 4.

# Third line conveys that there is a link from page 2 to page 1.

# Fourth line conveys that there are links from page 3 to pages 1 and 5.

# Fifth line conveys that there are links from page 4 to pages 2 and 3.

# Sixth line conveys that there is a links from page 5 to page 5 itself.

# Seventh line conveys that starting page is 2 and ending page is 3

# From page 2, we can open only page 1. From page 1, we can open page 4. From page 4, we can open page 3. So, minimum 3 clicks are required, and this is the output.

# Example 2

# Input

# 3

# 2

# 1

# 1

# 2 3

# Output

# -1

# Explanation:

# First line conveys that there is total 3 pages.

# Second line conveys that there are links from page 1 to page 2.

# Third line conveys that there is a link from page 2 to page 1.

# Fourth line conveys that there are links from page 3 to page 1.

# Since there is no way to reach from page 2 to page 3, print -1 as output.

