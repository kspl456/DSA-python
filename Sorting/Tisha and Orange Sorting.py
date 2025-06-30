#Tisha and Orange Sorting
#You have seen Tisha and he oranges in the previous question. Her eldest son on the other hand, sees what his mother does and decides to help her sort out the oranges in increasing order of size. He is also quick to realize that they should be following the quicksort algorithm and finds this pseudocode from this Data Structures text book. Assume the oranges are neatly stacked in a row.
#Quicksort Pseudocode :
#Quicksort(arr, l, r) : 
	#if (l < r) : 
#		p = partition(arr, l, r)
#		print(p)
#		print(arr from l to r)
#		Quicksort(arr, l, p - 1)
#		Quicksort(arr, p + 1, r)


#INPUT
#The first line of input is n (1≤n≤100), the number of oranges Tisha plucked from the orchard
#The second line of input are the diameters of the oranges you just took (positive numbers) each separated by a space. Assume the first orange in the row to be the pivot element each time.
#OUTPUT
#Print the sizes of the oranges in a row after the sorting has been done
#Sample Input 0
#10
#2 4 6 8 10 1 3 5 7 9


#Sample Output 0
#8
#2 4 6 8 1 3 5 7 9 10 
#6
#2 4 6 1 3 5 7 8 
#4
#2 4 1 3 5 6 
#2
#2 1 3 4 
#0
#1 2


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


    
def Quicksort(arr, l, r) : 
    if (l < r) : 
        p = partition(arr, l, r)
        print(p)
        for i in range(l,r+1):
            print(arr[i], end=" ")
        print()
        Quicksort(arr, l, p - 1)
        Quicksort(arr, p + 1, r)


n=int(input())
orange=input().split()
orange=[int(num) for num in orange]
Quicksort(orange, 0, n-1)
