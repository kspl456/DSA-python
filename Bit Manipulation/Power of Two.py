#Power of Two
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
'''

#method 1: Iterative Division
def isPowerOfTwo(n):
        if n<=0:
            return False
        while n%2==0:
            n//=2
        return n==1

'''
Approach:
1. Check if n is less than or equal to 0. If it is, return False since negative numbers and zero cannot be powers of two.
2. Use a while loop to repeatedly divide n by 2 as long as n is even.
3. After the loop, check if n is equal to 1. If it is, return True, indicating that n is a power of two. If not, return False.
Time Complexity: O(log n) - The number of times we can divide n by 2
Space Complexity: O(1) - No additional space is used
'''

#method 2: Bit Manipulation
def isPowerOfTwo(n):
        return n>0 and n &(n-1)==0

'''
Approach:
1.Perform a bitwise AND operation between n and (n-1). If n is a power of two, this operation will yield 0.

Why it works:
- A power of two in binary representation has exactly one bit set to 1 (e.g, 1 is 0001, 2 is 0010, 4 is 0100, etc.).
- Subtracting 1 from a power of two flips all bits after the rightmost set bit, resulting in a number that has no bits in common with the original number.
2. Check if n is greater than 0 to ensure we are not dealing with negative numbers or zero, which cannot be powers of two.
Time Complexity: O(1) - The bitwise operation is constant time.
Space Complexity: O(1) - No additional space is used.
'''