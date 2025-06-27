#Check Palindrome
#You are given a number n. You need to see if the number is a palindrome or not

def isPalin(N):
        n=len(str(N))
        if n<=1:
            return True
        if str(N)[0] != str(N)[-1]:
            return False
        return isPalin(str(N)[1:-1])

'''
Examples:
Input: 1010101
Output: True

Input: 57567
Output: False
'''
