#Convert Integer to the Sum of Two No-Zero Integers
'''
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
 

Constraints:

2 <= n <= 10^4
'''
def contains0(num):
            temp=num
            while temp>0:
                if temp%10==0: return True
                temp//=10
            return False

def getNoZeroIntegers(n):
        for i in range(1,n):
            if not contains0(i) and not contains0(n-i):
                return [i,n-i]

'''
Approach:
1. Define a helper function `contains0` that checks if a given integer contains the digit '0' in its decimal representation. This is done by repeatedly checking the last digit of the number and removing it until the number becomes zero.
2. In the main function `getNoZeroIntegers`, iterate through all integers `i` from `1` to `n-1`.
3. For each integer `i`, check if both `i` and `n-i` do not contain the digit '0' using the `contains0` function.
4. If both integers are valid No-Zero integers, return them as a list `[i, n-i]`.
'''
#Time Complexity: O(n * d), where n is the input integer and d is the number of digits in the integer.
#Space Complexity: O(1) as we are using only a constant amount of extra space.