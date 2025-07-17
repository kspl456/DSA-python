#Kadane's Algorithm / Maximum Subarray
#Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maxSubArray(nums):
        current_sum=0
        max_sum=nums[0]
        for i in nums:
            if current_sum<0:
                current_sum=0
            current_sum+=i
            max_sum=max(current_sum,max_sum)
        return max_sum