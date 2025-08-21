#Max Consecutive Ones
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''

def findMaxConsecutiveOnes(nums):
        ones=0;max_1=0
        for i in nums:
            if i==0:
                ones=0
            else:
                ones+=1
                max_1=max(max_1,ones)
        return max_1
                
'''
Approach:
1. Initialize two variables: `ones` to count the current consecutive ones and `max_1` to keep track of the maximum found so far.
2. Iterate through each element in the binary array `nums`.
3. If the current element is `0`, reset `ones` to `0`.
4. If the current element is `1`, increment `ones` by `1`.
5. Update `max_1` to be the maximum of its current value and `ones`.
6. After the loop, return `max_1` which contains the maximum number of consecutive 1's found in the array.
'''
#Time Complexity: O(n) where n is the length of the input array.
#Space Complexity: O(1) since we are using a constant amount of space.