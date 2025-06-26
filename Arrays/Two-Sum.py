#Two Sum

def twoSum(nums, target):
        Map={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in Map:
                return [i,Map[diff]]
            Map[num]=i
        return

'''
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0,1]

Input: nums = [3, 2, 4], target = 6
Output: [1,2]
'''