#Sum of Digits of a Number
def sumOfDigits(n):
        if n<10:
            return n
        return n%10 + sumOfDigits(n//10)

'''
Examples:
Input: 231
Output: 6

Input: 5792
Output: 5
'''
