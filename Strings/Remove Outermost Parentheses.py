#Remove Outermost Parentheses
'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

1 <= s.length <= 10^5
s[i] is either '(' or ')'.
s is a valid parentheses string.
'''

def removeOuterParentheses(s):
        count=0
        res=""
        n=len(s)
        for i in s:
            if i==')': count-=1
            if count!=0: res+=i
            if i=='(': count+=1
        return res

'''
Approach:
1. Initialize a counter `count` to keep track of the balance of parentheses and an empty string `res` to store the result.
2. Iterate through each character `i` in the input string `s`.
3. If the character is a closing parenthesis `)`, decrement the counter `count`.
4. If the counter `count` is not zero, append the character `i` to the result string `res`. This ensures that we only add characters that are not the outermost parentheses.
5. If the character is an opening parenthesis `(`, increment the counter `count`.
6. After processing all characters, return the result string `res`, which contains the input string without the outermost parentheses of each primitive valid parentheses string.
'''
#Time Complexity: O(n)
#Space Complexity: O(n)
