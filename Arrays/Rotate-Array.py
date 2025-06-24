#Rotate-Array
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
        n = len(nums)
        k = k % n

        def reverse(nums, left, right):
            while left < right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

'''
Examples:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: nums = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
'''