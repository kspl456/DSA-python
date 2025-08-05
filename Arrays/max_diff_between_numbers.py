#Maximum difference between increasing elements
'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

 

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
 

Constraints:

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 109
'''

def maximumDifference(nums):
        diff=-1
        left,right=0,1
        while right<len(nums):
            if nums[left]<nums[right]:
                curr_diff=nums[right]-nums[left]
                diff=max(diff,curr_diff)
            else: 
                 left=right
            right+=1
        return diff

'''
Start from the first number in the list.

This is your reference point — the number you're comparing others against.

Look at the next number in the list (moving forward one by one):

If the current number is greater than your reference point:

It’s a valid pair.

Calculate the difference between the two.

Keep track of the maximum difference you’ve found so far.

If the current number is smaller than or equal to your reference point:

It can’t form a valid pair with earlier numbers.

But it might be a better reference point for future numbers.

So, update your reference point to this number.

Repeat this process until you've checked the whole list.

Finally:

If you found at least one valid pair, return the largest difference you calculated.

If you didn’t find any valid pair (meaning the list is non-increasing), return -1.
'''