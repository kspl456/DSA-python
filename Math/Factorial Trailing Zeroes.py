#Factorial Trailing Zeroes
'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
'''

def trailingZeroes(n):
        if n<5:
            return 0
        count=0
        d=5
        while n>=d:
            count+=n//d
            d*=5
        return count

'''
Approach:
1. If n is less than 5, return 0 since there are no trailing zeroes.
2. Initialize a count variable to 0 and a divisor d to 5.
3. While n is greater than or equal to d:
   - Add the integer division of n by d to count.
   - Multiply d by 5 to check for higher powers of 5.

Time Complexity: O(log n)
Space Complexity: O(1)
'''