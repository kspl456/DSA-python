# Pay Per Cluster

# Jaime the Tailor's new customer wants to add n distinct clusters of buttons to her dress,
# where each cluster is filled with a distinct number of buttons of a certain color.

# The customer also has specific ideas about how much she wants to pay for each cluster.
# For some cluster i, she wants to pay at least ai dollars.

# In addition, she wants each cluster to contain a distinct number of buttons.

# And, finally, she wants to minimize her total cost.

# Jaime stocks an infinite number of buttons in an infinite number of colors at his shop,
# and each button costs p dollars.

# Given n, p, and the amount of money that the customer wants to pay for each respective cluster,
# help Jaime by finding and printing a long integer denoting the minimum number of buttons
# he can use to satisfy her request.

# Input Format:
# The first line contains two space-separated integers denoting the respective values of n and p.
# The second line contains n space-separated integers where each integer i denotes the value of ai 
# (i.e., the minimum amount of money she wants to spend on cluster i).

# Constraints:
# 1 <= n, p, a <= 10^5

# Output Format:
# Print a single long integer denoting the minimum number of buttons required for Jaime to satisfy his customer's request.

# Sample Input 0:
# 3 2
# 4 6 6

# Sample Output 0:
# 9

# Sample Input 1:
# 2 3
# 4 5

# Sample Output 1:
# 5

import math

n,p=map(int,input().split())
a=list(map(int,input().split()))

buttons=[math.ceil(i/p) for i in a]
buttons.sort()

next_free = 0
total = 0

for b in buttons:
    if b < next_free:
        b = next_free
    total += b
    next_free = b + 1
    
print(total)

