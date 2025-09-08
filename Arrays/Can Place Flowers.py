#Can Place Flowers
'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

def canPlaceFlowers(flowerbed, n):
        count=0
        length=len(flowerbed)
        for i in range(length):
            if flowerbed[i]==0:
                if (i==0 or flowerbed[i-1]==0) and (i==length-1 or flowerbed[i+1]==0):
                    flowerbed[i]=1
                    count+=1
            if count>=n:
                return True
        return count>=n

'''
Approach:
1. Initialize a counter `count` to keep track of the number of flowers that can be planted.
2. Iterate through each plot in the `flowerbed` array.
3. For each plot, check if it is empty (0). If it is, check the adjacent plots:
   - If it's the first plot, only check the next plot.
   - If it's the last plot, only check the previous plot.
   - For all other plots, check both the previous and next plots.
4. If both adjacent plots are empty (or if it's at the boundary), plant a flower in the current plot (set it to 1) and increment the `count`.
5. If at any point the `count` of planted flowers reaches or exceeds `n`, return `True`.
6. After checking all plots, if the `count` is still less than `n`, return `False`.
'''
#Time Complexity: O(m), where m is the length of the flowerbed array.
#Space Complexity: O(1) as we are using only a constant amount of extra space.