# Given an array of integers where every element appears even number of times except one element which appears odd number of times, write a program to find that odd occurring element in O(log n) time. The equal elements must appear in pairs in the array but there cannot be more than two consecutive occurrences of an element. 

# For example : 

# 3 

# 2 3 2 

# It doesn't have equal elements appear in pairs 

# 7 

# 1 1 2 2 2 3 3 

# It contains three consecutive instances of an element. 

# 5 

# 2 2 3 1 1 

# It is valid and the odd occurring element present in it is 3. 

# Enter only valid inputs. 

# Sample Input : 

# 5 

# 2 2 3 1 1 

# Sample Output : 

# 3

n = int(input())
arr = []

arr = input()
arr = arr.split()

count = 1
max = 1
for i in range(len(arr) - 1):
    if arr[i] == arr[i+1]:
        count += 1
        if count > max and count % 2 == 1:
            max = count
    else:
        count = 1

print(max)