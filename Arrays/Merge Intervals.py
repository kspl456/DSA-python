#Merge Intervals
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''
def merge(intervals):
        intervals.sort()
        output=[]
        for i,num in enumerate(intervals):
            if not output:
                output.append(num)
            elif output[-1][1] >= num[0]:  # Overlap
                output[-1][1] = max(output[-1][1], num[1])
            else:
                output.append(num)
        return output

'''
Approach:
1.Sort the intervals by their starting point. This helps in processing them in order, so overlaps are easy to detect.
2.Initialize an output list to store merged intervals.
3.Iterate through the sorted intervals:
4.If the output list is empty or there is no overlap with the last interval in output, just append the interval.
5.If there is overlap, merge the current interval with the last one in output by updating the end of the last interval.
'''

'''
Time Complexity: O(n log n) due to sorting, where n is the number of intervals.
Space Complexity: O(n) for the output list in the worst case where no intervals overlap.
'''