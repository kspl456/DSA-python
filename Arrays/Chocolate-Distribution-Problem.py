#Chocolate Distribution Problem

def findMinDiff(arr,m):
        arr.sort()
        n=len(arr)
        min_diff=float('inf')
        for i in range(n-m+1):
            diff=arr[m+i-1]-arr[i]
            if diff< min_diff:
                min_diff=diff
        return min_diff

#Example:
#Input: arr = [12, 4, 7, 9, 23, 25,41, 30, 40, 28, 42, 30, 44, 48, 43, 50], m = 7
#Output: 10

#Input: arr = [12, 4, 7, 9, 23, 25,41, 30], m = 3
#Output: 5
