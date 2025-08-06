#Common in 3 Sorted Arrays
'''
Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?

Examples :

Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [20, 80]
Explanation: 20 and 80 are the only common elements in arr, brr and crr.
Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
Output: [-1]
Explanation: There are no common elements in arr, brr and crr.
Input: arr1 = [1, 1, 1, 2, 2, 2], B = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
Output: [1, 2]
Explanation: We do not need to consider duplicates
Constraints:
1 <= arr1.size(), arr2.size(), arr3.size() <= 105
-105 <= arr1i , arr2i , 1arr3i <= 105
'''

def commonElements(self, arr1, arr2, arr3):
        i,j,k=0,0,0
        res=[]
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if i!=0 and arr1[i]==arr1[i-1]: 
                i+=1
                continue
            if j!=0 and arr2[j]==arr2[j-1]: 
                j+=1
                continue
            if k!=0 and arr3[k]==arr3[k-1]: 
                k+=1
                continue
            
            if arr1[i]==arr2[j]==arr3[k]:
                res.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr3[k]:
                j+=1
            else:
                k+=1
        return res

'''
Approach:
1.Initialize: i = j = k = 0
2.While i < len(arr1) and j < len(arr2) and k < len(arr3):
    ->If all three elements are equal:
        -->It's a common element → Add to result
        -->Move all three pointers forward
        -->Skip duplicates in each array
    ->Else, advance the pointer pointing to the smallest element (since arrays are sorted)
3.Return result array.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output)
'''