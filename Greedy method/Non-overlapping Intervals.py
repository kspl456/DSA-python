#Non-overlapping Intervals
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
'''

def eraseOverlapIntervals(intervals):
        n=len(intervals)
        intervals.sort(key=lambda x: x[1])
        i=0
        count=1
        for j in range(1,n):
            if intervals[j][0] >=intervals[i][1]:
                count+=1
                i=j            
        return n-count

'''
Approach:
1. Sort the intervals based on their end times. This helps in ensuring that we always consider the interval that ends the earliest, which allows for more room for subsequent intervals.
2. Initialize a counter `count` to 1, as the first interval will always be counted.
3. Use a variable `i` to keep track of the last non-overlapping interval.
4. Iterate through the sorted intervals starting from the second interval:
   - If the start time of the current interval is greater than or equal to the end time of the last non-overlapping interval, it means they do not overlap. Increment the `count` and update `i` to the current index.
5. Finally, return the total number of intervals minus the count of non-overlapping intervals to get the minimum number of intervals to remove.

Time Complexity: O(n log n) due to sorting, where n is the number of intervals.
Space Complexity: O(1) as we are using only a constant amount of extra space.
'''