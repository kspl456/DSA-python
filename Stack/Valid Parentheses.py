#Valid Parentheses
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def isValid(s):
        stack=[]
        for i in s:
            if i=='(' or i== '{' or i=='[':
                stack.append(i)
            elif stack==[]: return False
            elif i==')' and stack[-1]=='(': 
                        stack.pop()
            elif i=='}' and stack[-1]=='{': 
                        stack.pop()
            elif i==']' and stack[-1]=='[': 
                        stack.pop()
            else: return False
        return stack==[]

'''
Approach:
1. Initialize an empty stack to keep track of opening brackets.
2. Iterate through each character in the string:
   - If the character is an opening bracket ('(', '{', or '['), push it onto the stack.
   - If the character is a closing bracket (')', '}', or ']'):
        - Check if the stack is empty. If it is, return False (indicating an unmatched closing bracket).
        - Check if the top of the stack matches the corresponding opening bracket for the current closing bracket. If it does, pop the top of the stack.
        - If it does not match, return False (indicating a mismatch).
3. After processing all characters, check if the stack is empty. If it is, return True (indicating all brackets were matched). If not, return False (indicating unmatched opening brackets).    

Time Complexity: O(n), where n is the length of the input string s.
Space Complexity: O(n) in the worst case, where all characters are opening brackets.
'''