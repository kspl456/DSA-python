#Greatest Common Divisor of Strings
'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

def gcd(a,b):
        if a==b: return a
        elif a>b : return gcd(a-b,b)
        else: return gcd(a,b-a)

def gcdOfStrings(str1, str2):
        n1,n2=len(str1),len(str2)
        l=gcd(n1,n2)
        ans=str1[:l]
        check1=check2=""
        while len(check1)<n2:
            check1+=ans
        while len(check2)<n1:
            check2+=ans
        if check1==str2 and check2==str1:
            return ans
        else:
            return ""
        
'''
Approach:
1. Define a helper function `gcd` to compute the greatest common divisor of lengths of the strings using the subtraction method.
2. In the main function `gcdOfStrings`, calculate the lengths of both strings `str1` and `str2`.
3. Use the `gcd` function to find the greatest common divisor of the lengths of the two strings.
4. Extract the substring `ans` from `str1` that has the length equal to the gcd.5. Initialize two empty strings `check1` and `check2` to build the repeated versions of `ans`.
6. Use while loops to concatenate `ans` to `check1` until its length is at least `n2`, and to `check2` until its length is at least `n1`.
7. Finally, check if `check1` equals `str2` and `check2` equals `str1`. If both conditions are true, return `ans` as the greatest common divisor string; otherwise, return an empty string.
'''

#Time Complexity: O(n + m), where n and m are the lengths of str1 and str2 respectively.
#Space Complexity: O(n + m) for storing the repeated strings.