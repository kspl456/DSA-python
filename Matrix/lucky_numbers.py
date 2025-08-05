#Lucky Numbers in a Matrix
'''
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
'''
#method 1:
# Time Complexity: O(m*n)
# Space Complexity: O(m)
def luckyNumbers(matrix):
        row=len(matrix)
        col=len(matrix[0])
        row_set=set()
        res=[]
        for r in range(row):
            row_set.add(min(matrix[r]))
        for c in range(col):
            curr_max=matrix[0][c]
            for r in range(row):
                curr_max=max(curr_max, matrix[r][c])
            if curr_max in row_set:
                res.append(curr_max)
        return res

'''
Approach:
1. Iterate through each row to find the minimum element and store it in a set.
2. For each column, find the maximum element.
3. If the maximum element of a column is present in the set of minimum elements, add it to the result list.
4. Return the result list containing all lucky numbers.
'''

#method 2:
# Time Complexity: O(m*n)
# Space Complexity: O(1)
def luckyNumbers(matrix):
        row=len(matrix)
        col=len(matrix[0])
        row_min=float("-inf")
        for r in range(row):
            curr_min=min(matrix[r])
            row_min=max(row_min,curr_min)
        for c in range(col):
            curr_max=matrix[0][c]
            for r in range(row):
                curr_max=max(curr_max,matrix[r][c])
            if curr_max==row_min:
                    return [curr_max]
        return []

'''
Approach:
1. Iterate through each row to find the minimum element and keep track of the maximum of these minimums.
2. For each column, find the maximum element.
3. If the maximum element of a column matches the maximum of the minimums, return it as the lucky number.
4. If no lucky number is found, return an empty list.
'''