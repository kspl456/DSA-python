# Find the Duplicate Number
# Given an array of integers `nums` containing `n + 1` integers where 
# each integer is in the range `[1, n]` (inclusive). 
# There is exactly one repeated number in `nums`, but it could appear more than once.
#
# The task is to find the duplicate number without:
# - Modifying the input array
# - Using more than constant (O(1)) extra space
# - Exceeding O(n) time complexity
# Constraints:
# - 1 <= n <= 10⁵
# - nums.length == n + 1
# - 1 <= nums[i] <= n
# - Only one integer appears two or more times, others appear exactly once


#Example:
# Input: nums = [3, 1, 3, 4, 2]
# Output: 3
#
# Index -> Value
#   0    -> 3
#   1    -> 1
#   2    -> 3
#   3    -> 4
#   4    -> 2
#
# Cycle path: 0 → 3 → 4 → 2 → 3 (cycle starts at 3)

def findDuplicate(nums):
        slow=fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow

# Time Complexity: O(n)
# Space Complexity: O(1) – Constant extra space

# Approach: Floyd’s Tortoise and Hare (Cycle Detection)
# Treat the array as a linked list:
# - Each index points to nums[i]
# - Due to the duplicate, there must be a cycle
# - Use Floyd's algorithm to detect the start of the cycle (duplicate number)

# -----------------------
# Phase 1: Finding intersection point
# -----------------------
# - Initialize two pointers, slow and fast
# - Move slow by one step: slow = nums[slow]
# - Move fast by two steps: fast = nums[nums[fast]]
# - Continue until they meet

# -----------------------
# Phase 2: Finding entrance to the cycle
# -----------------------
# - Reset slow to nums[0]
# - Move both slow and fast one step at a time
# - When they meet again, that's the duplicate number
