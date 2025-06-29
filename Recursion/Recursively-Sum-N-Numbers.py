#Recursively Sum N Numbers

def recursiveSum(n):
        if n<=1:
            return n
        return n+recursiveSum(n-1)

'''
Examples
Input: 3
Output: 6

Input: 19
Output: 190
'''
