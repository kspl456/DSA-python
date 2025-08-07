#Alternate Positive Negative
'''
Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers.

Examples:

Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.
Input: arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Output: [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
Explanation : The positive numbers are [5, 2, 4, 7, 1, 8, 0] and the negative integers are [-5,-2,-8]. According to the given conditions we will start from the positive integer 5 and then -5 and so on. After reaching -8 there are no negative elements left, so according to the given rule, we will add the remaining elements (in this case positive elements are remaining) as it in by maintaining the relative order.
Input: arr[] = [9, 5, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 5, -1, 5, -5, 0, -3, 2]
Explanation: The positive numbers are [9, 5, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 5 and then -1 and so on.
Constraints:
1 ≤ arr.size() ≤ 106
-106 ≤ arr[i] ≤ 106
'''

def rearrange(arr):
        positive=[]
        negative=[]
        for i in arr:
            if i>=0: positive.append(i)
            else: negative.append(i)
        i,j,k=0,0,0
        while i<len(positive) and j<len(negative):
            if k%2==0:
                arr[k]=positive[i]
                i+=1
            else:
                arr[k]=negative[j]
                j+=1
            k+=1
        while i<len(positive):
            arr[k]=positive[i]
            i+=1
            k+=1
        while j<len(negative):
            arr[k]=negative[j]
            j+=1
            k+=1
        return arr

'''
Approach:
1. Initialize two lists: one for positive numbers and one for negative numbers.
2. Traverse the input array:
   - If the number is non-negative, append it to the positive list.
   - If the number is negative, append it to the negative list.
3. Use three pointers: i for positive numbers, j for negative numbers, and k for the current position in the original array.
4. While both lists have elements:
    - If k is even, place the next positive number in the array and increment i.
    - If k is odd, place the next negative number in the array and increment j.
    - Increment k after placing an element.
5. After one of the lists is exhausted, append the remaining elements from the other list to the array.
6. Return the modified array.

Time Complexity: O(n), where n is the size of the input array.
Space Complexity: O(n) for storing positive and negative numbers separately.
'''