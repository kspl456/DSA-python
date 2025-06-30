#Recursively Sum N Numbers

def recursiveSum(n):
        if n<=1:
            return n
        return n+recursiveSum(n-1)

# Example:
# Input: n = 5
# Output: 15
# Explanation: The sum of the first 5 natural numbers is 1 + 2 + 3 + 4 + 5 = 15