#Two sum -Pairs with 0 Sum
'''
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

Constraints:
3 <= arr.size <= 105
-105 <= arr[i] <= 105
'''

def getPairs(arr):
        left,right=0,len(arr)-1
        arr.sort()
        res=set()
        while left<right:
            if arr[left]+arr[right]==0:
                res.add((arr[left],arr[right]))
                left+=1
                right-=1
            elif arr[left]+arr[right]<0:
                left+=1
            else:
                right-=1
        return [list(pair) for pair in sorted(res)]

'''
Approach:
1. Sort the array.
2. Use two pointers, one starting from the beginning (left) and the other from the end (right) of the array.
3. If the sum of the elements at these pointers is zero, add the pair to the result set and move both pointers inward.
4. If the sum is less than zero, move the left pointer to the right.
5. If the sum is greater than zero, move the right pointer to the left.
6. Continue until the two pointers meet.
7. Convert the set of pairs to a sorted list and return it. This ensures that we only get unique pairs and the result is sorted.
'''