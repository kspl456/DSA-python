#Kth Smallest
'''
Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.
Constraints:
1 <= arr.size <= 106
1<= arr[i] <= 106
1 <= k <= n
'''
import heapq
def kthSmallest(arr,k):
    for i in range(len(arr)):
        arr[i]=-arr[i]
    heapq.heapify(arr)
    while len(arr) >k:
        heapq.heappop(arr)
    return(-heapq.heappop(arr))

'''
Optimal Approach: Max-Heap of size k
Idea:
Use a max-heap of size k to keep track of the k smallest elements seen so far.

Steps:
1.Iterate over the array.

2.Push elements into a max-heap (you simulate it using -num in Python since heapq only supports min-heaps).

3.Keep heap size ≤ k. If it grows beyond, remove the largest (which is the smallest in -num form).

4.The top of the heap after this is the kth smallest.

Time Complexity:
O(n log k) → very efficient when k is much smaller than n.
'''