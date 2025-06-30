#Sum of Digits of a Number
def sumOfDigits(n):
        if n<10:
            return n
        return n%10 + sumOfDigits(n//10)

# Example:
# Input: n = 12345  
# Output: 15
# Explanation: The sum of the digits is 1 + 2 + 3 + 4 + 5 = 15
