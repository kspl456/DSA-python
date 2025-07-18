"""
Problem: Minimize the Height Difference After Modifications

You are given an array `arr[]` representing the heights of N towers and an integer `k`.

**Task:**
Modify each element in the array exactly once by either:
- Increasing the height by `k`, OR
- Decreasing the height by `k`

**Constraints:**
- After modification, no height should become negative.
- Return the minimum possible difference between the maximum and minimum tower heights after these modifications.

Example 1:
Input: arr = [1, 5, 8, 10], k = 2
Output: 5
Explanation: Modified array = [3, 3, 6, 8] → max = 8, min = 3, diff = 5

Example 2:
Input: arr = [3, 9, 12, 16, 20], k = 3
Output: 11
Explanation: Modified array = [6, 12, 9, 13, 17] → max = 17, min = 6, diff = 11

Approach:
-----------
1. Sort the array so we can handle elements in order.
2. Initialize the result as the difference between the original max and min.
3. The idea is to try every possible partition where:
    - Elements from index 0 to i are increased by k.
    - Elements from index i+1 to n-1 are decreased by k.
4. For each partition:
    - Calculate new potential min and max values.
    - Skip cases where any height becomes negative.
    - Update the result if the new difference is smaller.
5. Return the minimum difference found.

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) (in-place operations).
"""

def getMinDiff(arr, k):
    # Step 1: Sort the array
    arr.sort()
    n = len(arr)

    # Step 2: Initialize answer with the difference of original max and min
    ans = arr[-1] - arr[0]

    # Step 3: Initialize smallest and largest values after hypothetical modifications
    smallest = arr[0] + k
    largest = arr[-1] - k

    # Step 4: Try all possible partition points
    for i in range(n - 1):
        min_elem = min(smallest, arr[i + 1] - k)
        max_elem = max(largest, arr[i] + k)

        # Skip if any value becomes negative
        if min_elem < 0:
            continue

        # Step 5: Update the minimum difference
        ans = min(ans, max_elem - min_elem)

    return ans

