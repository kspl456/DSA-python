#Power of Four
'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
'''

#method 1: Iterative Division
def isPowerOfFour(n):
        if n<1:
            return False
        while n%4==0:
            n//=4
        return n==1

'''
Approach:
1. Check if n is less than 1. If it is, return False since negative numbers and zero cannot be powers of four.
2. Use a while loop to repeatedly divide n by 4 as long as n is divisible by 4.
3. After the loop, check if n is equal to 1. If it is, return True, indicating that n is a power of four. If not, return False.
Time Complexity: O(log n) - The number of times we can divide n by 4
Space Complexity: O(1) - No additional space is used
'''

#method 2: Bit Manipulation
def isPowerOfFour(n):
        return n>0 and n & (n-1) == 0 and (n-1) % 3 == 0

'''
Approach:
1. Perform a bitwise AND operation between n and (n-1). If n is a power of two, this operation will yield 0.
2. Check if n is greater than 0 to ensure we are not dealing with negative numbers or zero, which cannot be powers of four.
3. Additionally, check if (n-1) is divisible by 3
Why it works:
- A power of four in binary representation has exactly one bit set to 1, and it is at an even position (e.g., 1 is 0001, 4 is 0100, 16 is 10000).
- If a number is a power of four, subtracting 1 from it will yield a number that is divisible by 3.
Time Complexity: O(1) - The bitwise operations are constant time.
Space Complexity: O(1) - No additional space is used.
'''