#Jump Game
'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
'''

def canJump(nums):
        n=len(nums)
        if n==1: return True
        reach=0
        for i in range(n):
            if i>reach: return False
            reach=max(reach,i+nums[i])
            if reach>=n-1: return True

'''
Approach:
1. Initialize `reach` to 0, which keeps track of the farthest index that can be reached.
2. Iterate through each index `i` in the array.
3. If `i` is greater than `reach`, it means we cannot reach this index, so return False.
4. Update `reach` to the maximum of its current value and `i + nums[i]`, which represents the farthest index that can be reached from index `i`.
5. If at any point `reach` is greater than or equal to the last index (`n-1`), return True. 
6. If the loop completes without returning, it means we can reach the last index, so return True.   

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we are using only a constant amount of extra space.
'''