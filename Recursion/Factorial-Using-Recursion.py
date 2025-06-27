#Factorial Using Recursion

def factorial(self,n):
        if n==1 or n==0:
            return 1
        return factorial(n-1) * n

'''
Examples
Input: 3
Output: 6

Input: 7
Output: 5040
'''
