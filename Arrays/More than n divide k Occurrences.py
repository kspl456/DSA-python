#More than n/k Occurrences
'''
Given an array arr and an element k. The task is to find the count of elements in the array that appear more than n/k times and n is length of arr.

Examples :

Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.
Input: arr = [2, 3, 3, 2], k = 3
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.
Input: arr = [1, 4, 7, 7], k = 2
Output: 0
Explanation: In the given array, no element appears more than n/k times.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 108
1 <= k <= arr.size()
'''

def countOccurence(arr, k):
        n=len(arr)
        freq={}
        num=n/k
        count=0
        
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in freq.values():
            if i>num: count+=1
        return count

'''
Approach:
1. Initialize a dictionary `freq` to store the frequency of each element in the array.
2. Calculate `num` as `n/k`, where `n` is the length of the array.
3. Iterate through the array and populate the `freq` dictionary with the count of each element.
4. Iterate through the values in the `freq` dictionary and count how many elements have a frequency greater than `num`.
5. Return the count of such elements.

Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(n), for storing the frequency of elements.
'''