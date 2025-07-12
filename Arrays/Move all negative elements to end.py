#Move all negative elements to end
# Given an unsorted array arr[] having both negative and positive integers.
# The task is to place all negative elements at the end of the array without 
# changing the order of positive elements and negative elements.

# Note: Don't return any array, just modify the array in-place.

# Examples:

# Input  : arr[] = [1, -1, 3, 2, -7, -5, 11, 6]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.

# Input  : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]

# Expected Time Complexity   : O(n)
# Expected Auxiliary Space   : O(n)

# Constraints:
# 1 ≤ arr.size ≤ 10^6
# -10^9 ≤ arr[i] ≤ 10^9

def segregateElements(arr):
        res=[]
        for i in arr:
            if i>=0:
                res.append(i)
        for i in arr:
            if i<0:
                res.append(i)
        for i in range(len(arr)):
            arr[i]=res[i]
        
# Approach:
# Use a temporary array to store the result, since in-place rearrangement
# while preserving the order of elements requires extra space.

# 1. First, copy all positive elements (including zero) into the temporary array in order.
# 2. Then, copy all negative elements into the temporary array in order.
# 3. Finally, overwrite the original array with the elements from the temporary array.
