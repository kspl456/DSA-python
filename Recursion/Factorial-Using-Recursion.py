#Factorial Using Recursion

def factorial(self,n):
        if n==1 or n==0:
            return 1
        return factorial(n-1) * n

# Example:
# Input: n = 5  
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
