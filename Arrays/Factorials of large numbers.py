#Factorials of large numbers
'''
Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [1]
Explanation: 1! = 1 

Constraints:
1 ≤ n ≤ 103
'''
#method-1 (naive approach):
def fact(n):
            res=1
            for i in range(2,n+1):
                res*=i
            return res
def factorial(n):
        res= fact(n)
        return [int(digit) for digit in str(res)]

'''
Approach:
1. Define a function `fact(n)` that calculates the factorial of n iteratively.
2. Split the result into its individual digits by converting it to a string and then to a list of integers.
'''

#method-2 (efficient for larger n):
def factorial( n):
        res = [1]
        
        for x in range(2, n + 1):
            carry = 0
            for i in range(len(res)):
                prod = res[i] * x + carry
                res[i] = prod % 10
                carry = prod // 10
            while carry:
                res.append(carry % 10)
                carry //= 10
                
        return res[::-1] 

'''
Approach:
1. Initialize a list `res` with the first element as 1, which will hold the digits of the factorial.
2. Loop through numbers from 2 to n:
    - For each number x, initialize a carry variable to 0.
    - Loop through the digits in `res` and multiply each digit by x, adding the carry from the previous multiplication.
    - Update the digit in `res` with the last digit of the product and update carry with the rest.
    - If there's any carry left after processing all digits, append it to `res`.

Time Complexity: O(n * m), where n is the number and m is the number of digits in the result.
Space Complexity: O(m) for storing the digits of the factorial.
'''