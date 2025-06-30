#Min and Max in Array
#Given an array of integers, find the minimum and maximum elements in the array.

def get_min_max(arr):
        n=len(arr)
        
        if n==1: return arr[0], arr[0]
        
        mi=ma=arr[0]
        
        if n % 2 ==0:
            if arr[0]> arr[1]:
                ma=arr[0]
                mi=arr[1]
            else:
                ma=arr[1]
                mi=arr[0]
            i=2
        else: 
            mi=ma=arr[0]
            i=1
        
        while(i<n-1):
            if arr[i] < arr[i+1]:
                if arr[i] < mi:
                    mi = arr[i]
                if arr[i+1] > ma:
                    ma = arr[i+1]
            else:
                if arr[i+1] < mi:
                    mi = arr[i+1]
                if arr[i] > ma:
                    ma = arr[i]
                    
            i=i+2
            
        return mi,ma

#Examples:

#Input: arr[] = [3, 2, 1, 56, 10000, 167]
#Output: 1 10000

#Input: arr[] = [1, 2, 3, 4, 5]
#Output: 1 5

