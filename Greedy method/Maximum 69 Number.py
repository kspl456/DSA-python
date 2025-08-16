#Maximum 69 Number
'''
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.
'''

def maximum69Number (num):
        n=list(str(num))
        for i,num in enumerate(n):
            if num=='6':
                n[i]='9'
                break
        return int(''.join(n))

'''
Approach:
1. Convert the number to a string and then to a list of characters.
2. Iterate through the list of characters.
3. If a '6' is found, change it to '9' and break the loop to ensure only one change is made.
4. Join the list back into a string and convert it to an integer before returning.
'''