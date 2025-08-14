#Minimum Add to Make Parentheses Valid
'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
'''
#method-1: using stack
def minAddToMakeValid(s):
        stack=[]
        count=0
        for i in s:
            if i=='(': stack.append(i)
            elif stack==[]: count+=1
            else: stack.pop()
        return count+len(stack)

'''
Approach:
1. Initialize an empty stack to keep track of unmatched opening parentheses.
2. Initialize a counter to count the number of unmatched closing parentheses.
3. Iterate through each character in the string:
   - If the character is '(', push it onto the stack.
   - If the character is ')':
     - If the stack is empty, increment the counter (indicating an unmatched closing parenthesis).
     - Otherwise, pop an opening parenthesis from the stack (indicating a match).
4. After processing all characters, the stack will contain unmatched opening parentheses.
5. The result is the sum of the counter (unmatched closing parentheses) and the length of the stack (unmatched opening parentheses).

Time Complexity: O(n), where n is the length of the input string s.
Space Complexity: O(n) in the worst case, where all characters are opening parentheses.
'''

#method-2: using two counters
def minAddToMakeValid(s):
        oc=0;cc=0
        for i in s:
            if i=='(': oc+=1
            elif oc>0: oc-=1
            else: cc+=1
        return oc+cc

'''
Approach:
1. Initialize two counters: `oc` for unmatched opening parentheses and `cc` for unmatched closing parentheses.
2. Iterate through each character in the string:
    - If the character is '(', increment the `oc` counter.
    - If the character is ')':
      - If there are unmatched opening parentheses (`oc > 0`), decrement the `oc` counter (indicating a match).
      - Otherwise, increment the `cc` counter (indicating an unmatched closing parenthesis).
3. The result is the sum of `oc` and `cc`, which represents the total number of moves required to make the parentheses valid.

Time Complexity: O(n), where n is the length of the input string s.
Space Complexity: O(1), as we are using only a constant amount of extra space for
'''