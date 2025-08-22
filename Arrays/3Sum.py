#3Sum
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 10^5
'''

def threeSum(nums):
        res=[]
        nums.sort()
        for i,num in enumerate(nums):
            if i>0 and num==nums[i-1]: continue
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum=num+nums[l]+nums[r]
                if threeSum>0: r-=1
                elif threeSum<0: l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]: l+=1
        return res

'''
Approach:
1. Sort the input array `nums`.
2. Iterate through the sorted array, using each element as a potential first element of a triplet.
3. For each element, use a two-pointer technique to find pairs that sum to the negative of the current element.
4. Skip duplicate elements to avoid duplicate triplets in the result.
5. Store valid triplets in the result list `res`.
6. Return the result list `res` containing all unique triplets that sum to zero.
'''
#Time Complexity: O(n^2) where n is the length of the input array.
#Space Complexity: O(1) if we don't count the output list, otherwise O(k) where k is the number of triplets found.