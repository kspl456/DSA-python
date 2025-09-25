#Largest Odd Number in String
'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
 

Constraints:

1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
'''

def largestOddNumber(num):
        res=""
        n=len(num)
        i=n-1
        while i>=0:
            if num[i] in {'1','3','5','7','9'}:
                res=num[:i+1]
                break
            else:
                i-=1
        return res

'''
Approach:
1. Initialize an empty string `res` to store the result.
2. Get the length `n` of the input string `num`.
3. Start a loop with an index `i` initialized to `n-1` (the last character of the string) and decrement `i` until it reaches 0.
4. In each iteration, check if the character at index `i` is an odd digit (i.e., one of '1', '3', '5', '7', '9').
5. If an odd digit is found, set `res` to the substring of `num` from the start to index `i` (inclusive) and break the loop.
6. If no odd digit is found by the end of the loop, `res` remains an empty string.
7. Return the result string `res`, which contains the largest odd integer substring or an empty string if no odd integer exists.
'''
#Time Complexity: O(n), where n is the length of the input string num. In the worst case, we may need to check all characters in the string.
#Space Complexity: O(1), as we are using a constant amount of extra space for the result string res, regardless of the input size.