#Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

#method 1:Sorting
def singleNumber(nums):
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

'''
Approach:
1. Sort the input list `nums`.
2. Iterate through the sorted list in steps of 2.
3. For each pair of elements, check if they are equal. If they are not, return the first element of the pair, as it is the single number.
4. If no unequal pair is found, return the last element of the sorted list, which is the single number.
Time Complexity: O(n log n) - Sorting the list takes O(n log n) time
Space Complexity: O(1) - No additional space is used for the sorting operation.
'''

#method 2: Hash Map
def singleNumber(nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, value in count.items():
            if value == 1:
                return key
'''Approach:
1. Initialize an empty dictionary `count` to keep track of the frequency of each number in the input list `nums`.
2. Iterate through each number `num` in `nums`.
3. For each number, check if it is already in the `count` dictionary:
   - If it is, increment its count by 1.
   - If it is not, add it to the dictionary with a count of 1.
4. After counting the frequencies, iterate through the items in the `count` dictionary.
5. For each key-value pair, check if the value is 1. If it is, return the key, which is the single number that appears only once.
Time Complexity: O(n) - We traverse the list once to count frequencies and then iterate through the dictionary.
Space Complexity: O(n) - We use additional space for the dictionary to store counts.
'''

#method 3: Bit Manipulation
def singleNumber(nums):
        res=0
        for i in nums:
            res^=i
        return res

'''
Approach:
1. Initialize a variable `res` to 0.
2. Iterate through each number `i` in the input list `nums`.
3. For each number, perform a bitwise XOR operation between `res` and `i`, and store the result back in `res`.
4. After iterating through all numbers, `res` will contain the single number that appears only once, since XORing a number with itself results in 0, and XORing with 0 results in the number itself.
Time Complexity: O(n) - We traverse the list once.
Space Complexity: O(1) - We use a constant amount of space for the variable `res`.
'''