#Array Subset
'''
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
Constraints:
1 <= a.size(), b.size() <= 10^5
1 <= a[i], b[j] <= 10^6
'''

def isSubset(a, b):
        freq={}
        for i in a:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in b:
            if i in freq and freq[i]>0:
                freq[i]-=1
            else: return False
        return True

'''
Approach:
1. Create a frequency dictionary `freq` to count occurrences of each element in array `a`.
2. Iterate through each element in array `b`:
    - If the element exists in `freq` and its count is greater than zero, decrement its count.
    - If the element does not exist in `freq` or its count is zero, return False (indicating `b` is not a subset of `a`).
3. If all elements in `b` are found in `a` with sufficient counts, return True (indicating `b` is a subset of `a`).

Time Complexity: O(n + m), where n is the size of array `a` and m is the size of array `b`.
Space Complexity: O(n) for storing the frequency dictionary.
'''