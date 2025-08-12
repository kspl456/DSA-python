#Power of Three
'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
'''

def isPowerOfThree(n):
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1

'''
Approach:
1. Check if n is less than or equal to 0. If it is, return False since negative numbers and zero cannot be powers of three.
2. Use a while loop to repeatedly divide n by 3 as long as n is divisible by 3.
3. After the loop, check if n is equal to 1. If it is, return True, indicating that n is a power of three. If not, return False.
Time Complexity: O(log n) - The number of times we can divide n by 3
Space Complexity: O(1) - No additional space is used
'''