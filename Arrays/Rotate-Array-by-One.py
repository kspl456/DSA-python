#Rotate Array by One
#Given an array arr, rotate the array by one position in clockwise direction.

def rotate(arr):
        if not arr:
            return arr
        last=arr[-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=last
        return arr

'''Examples:
Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]

Input: arr[] = [10, 20, 30, 40, 50]
Output: [50, 10, 20, 30, 40]
'''