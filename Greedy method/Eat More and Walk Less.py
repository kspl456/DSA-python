#Eat More and Walk Less
# --------------------------------
# Marc loves eating cupcakes, but he also wants to stay fit.
# He eats all n cupcakes in one sitting. Each cupcake i has a certain calorie count c[i].

# After eating a cupcake with c calories, Marc must walk at least:
#     2^j * c miles,
# where j is the number of cupcakes he has already eaten before that one.

# To minimize the total number of miles he must walk, Marc should eat the highest-calorie cupcakes first.

# Your task is to compute the **minimum number of miles** Marc must walk to stay fit.

# Input Format:
# -------------
# The first line contains an integer N — the number of cupcakes.
# The second line contains N space-separated integers, representing the calorie counts of the cupcakes.

# Constraints:
# ------------
# 1 <= N <= 40               # Small input size
# 1 <= c[i] <= 1000          # Calories per cupcake

# Output Format:
# --------------
# Output a single long integer — the minimum number of miles Marc must walk.

# Sample Input:
# -------------
# 3
# 1 3 2

# Sample Output:
# --------------
# 11

# Explanation:
# ------------
# Optimal order to eat: 3 (0th), 2 (1st), 1 (2nd)
# Miles = 2^0 * 3 + 2^1 * 2 + 2^2 * 1 = 3 + 4 + 4 = 11

#method 1 - using sort()
n=int(input())
c=list(map(int,input().split()))
c.sort(reverse= True)
miles=0
for j,i in enumerate(c):
    miles+=(2**j) * i
print(miles)

#method 2 - using quick sort
def partition(a,low,high):
    pivot=a[high]; i=low-1
    for j in range(low,high):
        if a[j] > pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1

def quickSort(a,low,high):
    if low>high:
        return
    p=partition(a,low,high)
    quickSort(a,low,p-1)
    quickSort(a,p+1,high)

n=int(input())
c=list(map(int,input().split()))
quickSort(c,0,n-1)
miles=0

for i,j in enumerate(c):
    miles+=(2**i)*j
print(miles)
