#Fibonacci Using Recursion
def fibonacci(n):
        if n==0 or n==1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

# Example:
# Input: n = 5  
# Output: 5
# Explanation: The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ...
# The 5th Fibonacci number is 5.
