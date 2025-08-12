# Diagonal Traverse
'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''

def findDiagonalOrder(mat):
        n,m=len(mat),len(mat[0])
        d={}
        for i in range(n):
            for j in range(m):
                if i+j not in d:
                    d[i+j]=[mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        res=[]
        key=0
        while key in d:
            if key%2==0:
                d[key].reverse()
            res.extend(d[key])#adds the elements of the list at d[key] to res element by element
            key+=1
        return res

'''
Approach:
1. Initialize an empty dictionary `d` to store the diagonal elements.
2. Iterate through each element in the matrix using two nested loops:
   - The outer loop iterates over the rows (`i`).
   - The inner loop iterates over the columns (`j`).
3. For each element `mat[i][j]`, calculate the sum of its indices `i + j` to determine the diagonal level.
4. If the diagonal level `i + j` is not already a key in the dictionary `d`, create a new entry with the value as a list containing the current element.
5. If the diagonal level already exists, append the current element to the list at that key.
6. Initialize an empty list `res` to store the final result.
7. Iterate through the keys of the dictionary `d` in order:
   - If the key is even, reverse the list at that key to maintain the correct diagonal order.
   - Extend the result list `res` with the elements from the list at that key.

Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix. We traverse each element once.
Space Complexity: O(m * n) in the worst case, where all elements are stored in the dictionary `d` if they are all on different diagonals. However, in practice, the space used will be proportional to the number of unique diagonals, which is typically much less than m * n.
'''