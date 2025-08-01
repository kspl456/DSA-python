#Next Permutation
'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''

def nextPermutation(nums):
        idx=-1
        n=len(nums)
        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                idx=i
                break
        if idx==-1:
            nums.reverse()
        else:
            prev=idx
            for i in range(idx,n):
                if nums[i]>nums[idx-1] and nums[i]<=nums[prev]:
                    prev=i
            nums[idx-1],nums[prev]=nums[prev],nums[idx-1]
            nums[idx:] = reversed(nums[idx:])

'''
Algorithm:
1.Find the first decreasing element from the right.
2.If such element doesn't exist, reverse the whole array (i.e., it's the last permutation).
3.Otherwise, find the smallest element larger than that element to the right.
4.Swap them.
5.Reverse the elements to the right of the original index.
'''