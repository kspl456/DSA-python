#Valid Palindrome
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
'''

def isPalindrome(s):
        if s==" " or s=="": return True
        upperalpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha="abcdefghijklmnopqrstuvwxyz"
        digit="1234567890"
        new=""
        for i in s:
            if i in upperalpha: 
                new+=i.lower()
            elif i in alpha: 
                new+=i
            elif i in digit: 
                new+=i
        newr=new[::-1]
        if new==newr: return True
        return False

'''
Approach:
1. Check if the string is empty or contains only a space. If so, return True since an empty string is considered a palindrome.
2. Define strings containing uppercase letters, lowercase letters, and digits to identify alphanumeric characters.
3. Initialize an empty string new to store the cleaned version of the input string.
4. Iterate through each character in the input string s:
    - If the character is an uppercase letter, convert it to lowercase and append it to new.
    - If the character is a lowercase letter or a digit, append it to new as is.
5. Create a reversed version of new called newr.
6. Compare new with newr. If they are the same, return True (indicating that the string is a palindrome); otherwise, return False.
'''

#Time Complexity: O(n) where n is the length of the string s. 
#Space Complexity: O(n) for storing the cleaned string new.