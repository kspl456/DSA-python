# Find the Great Product
# Problem: Find the Great Product
# --------------------------------
# Given an array of N integers, the task is to compute and print the highest possible
# product that can be obtained by multiplying any three numbers from the array.

# Input Format:
# -------------
# The first line contains a single integer N — the number of elements in the array.
# The second line contains N space-separated integers representing the array elements.

# Constraints:
# ------------
# 1 <= N <= 10^6            # Up to a million integers
# 0 <= |Ai| <= 10^3         # Each element is between -1000 and 1000 (inclusive)

# Output Format:
# --------------
# Output a single integer — the maximum product of any three numbers from the array.

# Sample Input:
# -------------
# 6
# 0 -1 3 100 70 50

# Sample Output:
# --------------
# 350000

n=int(input())
a=list(map(int,input().split()))
prod=1
for _ in range(3):
    m=max(a)
    prod*=m
    a.remove(m)
    
print(prod)
