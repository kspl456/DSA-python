#Island Perimeter
'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid
'''

def islandPerimeter(grid):
        n,m=len(grid), len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0: res+=1
                    if j==0 or grid[i][j-1]==0: res+=1
                    if i==n-1 or grid[i+1][j]==0: res+=1
                    if j==m-1 or grid[i][j+1]==0: res+=1
        return res

'''
Approach:
1. Initialize a variable `res` to 0 to keep track of the perimeter.
2. Iterate through each cell in the grid using two nested loops.
3. For each cell that contains land (grid[i][j] == 1):
   - Check the four possible directions (up, left, down, right):
     - If the cell is at the top edge or the cell above it is water, increment `res`.
     - If the cell is at the left edge or the cell to the left is water, increment `res`.
     - If the cell is at the bottom edge or the cell below it is water, increment `res`.
     - If the cell is at the right edge or the cell to the right is water, increment `res`.
4. Return the total perimeter stored in `res`.

Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid. We traverse each cell once.
Space Complexity: O(1), since we are using a constant amount of extra space for the perimeter count.
'''