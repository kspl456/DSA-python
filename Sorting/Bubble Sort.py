#Bubble Sort
# This is a simple implementation of the Bubble Sort algorithm in Python.

def bubble_sort(arr):
    n=len(arr)
    swap=False
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if (swap==False):
             return arr
    return arr