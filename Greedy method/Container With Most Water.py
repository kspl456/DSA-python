#Container With Most Water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''

def maxArea(height):
        left,right=0,len(height)-1
        maxarea=0
        while left<right:
            maxarea=max(maxarea, min(height[left],height[right])* (right-left))
            if height[left]<height[right]:
                left+=1 
            else: right-=1
        return maxarea

'''
Approach:
1. Initialize two pointers, `left` at the start (0) and `right` at the end (length of height - 1) of the array.
2. Initialize a variable `maxarea` to keep track of the maximum area found.
3. Use a while loop to iterate until `left` is less than `right`:
   - Calculate the area formed by the lines at the `left` and `right` pointers using the formula: area = min(height[left], height[right]) * (right - left).
   - Update `maxarea` if the calculated area is greater than the current `maxarea`.
   - Move the pointer pointing to the shorter line inward (increment `left` if height[left] < height[right] or decrement `right` otherwise).
4. Return `maxarea` after the loop ends.

Time Complexity: O(n), where n is the length of the height array, as we traverse the array only once.
Space Complexity: O(1), as we are using only a constant amount of extra space.
'''