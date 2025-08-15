#Next Greater Element I
'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
'''

def nextGreaterElement(nums1, nums2):
        d={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack: d[nums2[i]]=stack[-1]
            else: d[nums2[i]]=-1
            stack.append(nums2[i])
        res=[]
        for i in nums1:
            res.append(d[i])
        return res

'''
Approach:
1. Create a dictionary `d` to store the next greater element for each number in `nums2`.
2. Use a stack to keep track of the elements while iterating through `nums2` from right to left.
3. For each element in `nums2`, pop elements from the stack that are less than or equal to the current element, as they cannot be the next greater element.
4. If the stack is not empty after popping, the top of the stack is the next greater element for the current number; otherwise, it is -1.
5. Store the result for each number in `nums1` by looking it up in the dictionary `d`.
6. Return the results as a list.
'''