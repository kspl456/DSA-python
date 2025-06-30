#Vasya and Birthday Presents
# Vasya's sister loves arrays that are sorted in non-increasing order.
# Today is her birthday. Vasya wants to gift her sister sorted arrays on her birthday.
# But the shop has only unsorted arrays.
# So, Vasya bought T unsorted arrays and is trying to sort them.
# But, she doesn't have much time to sort the arrays manually as she is getting late for the birthday party.
# So, she asked you to write a program to sort the T arrays in non-increasing order.
# Help her, or her sister will be upset.
#
# Formally, given T arrays as input, sort each one of them in non-increasing order and print each array in a new line.
#
# INPUT
# First line contains an integer T(1 <= T <= 100), denoting the number of test cases.
# First line of each test case contains an integer N(1 <= N <= 100000), denoting the size of the array.
# Second line contains N space separated integers, denoting the array elements Ai(1 <= Ai <= 1000000000).
#
# OUTPUT
# For each test case, print the sorted array in non-increasing order.
#
# Sample Input 0
# 2
# 5
# 2 5 2 4 3
# 5
# 5 4 2 3 1
#
# Sample Output 0
# 5 4 3 2 2
# 5 4 3 2 1

def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    i=0;j=0;k=low
    m=len(left)
    n=len(right)
    while i<m and j<n:
        if left[i] >= right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<m:
        arr[k]=left[i]
        k+=1
        i+=1
    while j<n:
        arr[k]=right[j]
        k+=1
        j+=1
        
def mergeSort(arr,low,high):
    if low<high:
        mid=(low+high)//2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mergeSort(arr,0,n-1)
    print(*arr)
