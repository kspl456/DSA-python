#Fibonacci Using Recursion
def fibonacci(n):
        if n==0 or n==1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

'''
Examples:
Input: 1
Output: 1

Input: 5
Output: 5
'''
