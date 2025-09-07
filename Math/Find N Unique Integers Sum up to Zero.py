#Find N Unique Integers Sum up to Zero
'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
'''

def sumZero(n):
        res=[]
        if n%2==1:
            res.append(0)
        for i in range(1,(n//2)+1):
            res.append(i)
            res.append(-i)
        return res

'''
Approach:
1. Initialize an empty list `res` to store the unique integers.
2. If `n` is odd, append `0` to the list `res` since it is the only integer that can balance out an odd count of integers.
3. Use a for loop to iterate from `1` to `n//2` (inclusive). In each iteration, append both `i` and `-i` to the list `res`. This ensures that for every positive integer added, its negative counterpart is also added, maintaining the sum of zero.
4. Finally, return the list `res` which contains `n` unique integers that sum up to zero.
'''
#Time Complexity: O(n), where n is the input integer.
#Space Complexity: O(n) for storing the result list.