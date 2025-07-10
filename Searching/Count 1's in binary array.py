#Count 1's in binary array
# You are given a binary array that is sorted in non-increasing order, meaning all the 1's appear before the 0's.
# Find the total number of 1's present in the array.
#
# Examples:
#
# Input: arr[] = [1, 1, 1, 1, 1, 0, 0, 0]
# Output: 5
# Explaination: Count of 1's in the array is 5.
#
# Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
# Output: 7
# Explaination: Count of 1's in the array is 7.
#
# Constraints:
# 1 ≤ arr.size() ≤ 10^5 
# 0 ≤ arr[i] ≤ 1


def countOnes(arr):
        n=len(arr)
        low=0;high=n-1
        res=-1
        while(low<=high):
            mid=low+(high-low)//2
            if arr[mid]<1:
                high=mid-1
            else:
                low=mid+1
                res=mid
        return res+1