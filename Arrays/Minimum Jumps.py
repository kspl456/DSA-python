#Minimum Jumps
'''
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.
Constraints:
2 ≤ arr.size() ≤ 104
0 ≤ arr[i] ≤ 104
'''

'''
Algorithm Explanation:
Initialize variables:

jumps to count the number of jumps made.

current_end to indicate the range that can be reached with the current number of jumps.

farthest to track the farthest index that can be reached in the next jump.

Iterate through the array:

At each index, update the farthest index we can reach.

If we reach current_end, it means we have to make a jump:

Increment jumps.

Update current_end to farthest.

If at any point the current index is greater than farthest, then the end cannot be reached.
'''

def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:
                return jumps
            
            if i >= farthest:
                return -1

    return jumps