#Left Index
#Given a sorted array of integers of size N and a number X. Find the leftmost index of X in the array arr[].

#Example 1:

#Input:
#N = 10
#arr[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
#X = 1
#Output: 0

def leftIndex (N, arr, X): 
        result=-1
        
        low=0
        high=N-1
        while high>=low:
            mid=low+(high-low)//2
            if arr[mid]>X:
                high=mid-1
            elif arr[mid]<X:
                low=mid+1
            else:
                result=mid
                high=mid-1
        return result