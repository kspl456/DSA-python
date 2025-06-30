#Reverse an Array
# Given an array of integers, reverse the array in place.

def reverseArray(arr):

        n=len(arr)
        for i in range(n//2):
            arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
        return arr

# Example:
# Input: arr = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]   