# String protocol
# You are given a string `S` of length `N`. The string is transferred using a special protocol through a network.
# In one operation, you can either transfer:
# 1) 1 copy of a character.
# 2) 2 copies of the same character.
# The goal is to find the minimum time (in units) to transfer the entire string.

# Procedure to solve:
# We want to minimize the number of operations needed to transfer the string.
# The strategy is to send two copies of consecutive identical characters together in one operation.
# If consecutive characters are different, send them one by one.

# Steps:
#1.Read the string length `N` and the string `S`.
#2.Initialize a `count` variable to track the number of operations.
#3.Traverse the string:
#4.If two consecutive characters are the same, increment the operation count by 1 and skip the next character.
#5.Otherwise, just send one copy of the character, increment the operation count by 1.
#6.Return the result (minimum number of operations) for each test case.

def stringProtocol(n,s):
    count=0
    i=0
    while i<n:
        if i!=n-1 and s[i]==s[i+1]:
            i+=2
            count+=1
        else:
            count+=1
            i+=1
    return count

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 10^5
# Sum of N over all test cases does not exceed 10^5.
# String S contains lowercase English alphabets only.

# Sample Input:
# 2
# 5
# cbcdc
# 6
# aabeee

# Sample Output:
# 5
# 4