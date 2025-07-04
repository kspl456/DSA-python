#Subarray with 0 sum
#Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. 

#Examples:

#Input: arr[] = [4, 2, -3, 1, 6]
#Output: true
#Explanation: 2, -3, 1 is the subarray with a sum of 0.
#Input: arr = [4, 2, 0, 1, 6]
#Output: true
#Explanation: 0 is one of the element in the array so there exist a subarray with sum 0.
#Input: arr = [1, 2, -1]
#Output: false
#Constraints:
#1 <= arr.size <= 104
#-105 <= arr[i] <= 105

def subArrayExists(arr):
        Sum=0
        hashMap={}
        for i in arr:
            Sum+=i
            if Sum==0 or Sum in hashMap:
                return True
            hashMap[Sum]=1
        return False