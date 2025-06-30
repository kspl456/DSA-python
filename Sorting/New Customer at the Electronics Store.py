#New Customer at the Electronics Store
'''
The server is finally happy that he sorted the line and now he gets to sell his portable chargers. But alas, a new person enters with a battery percentage of k comes to the store and stands at the back of the queue. Now he has to fit him in this already ascending ordered queue. He asks for your help.
Formally, you are given an array of size n where the first n - 1 elements are sorted in ascending order and the last element can be any value. Sort this array by sliding the last element into its correct position.
INPUT
The first line of input is n (1≤n≤100), the number of customers in the queue. The second line of input is the battery percentages of the n customers (positive numbers less than 100)
the first n - 1 of which are standing in ascending order according to their battery percentage.
OUTPUT
Print the battery percentages of the customers in a line after the new person has been put in his right place in the queue.
Sample Input 0
6
1 3 5 7 9 4


Sample Output 0
1 3 4 5 7 9

'''

n=int(input())
bt=input().split()
bt=[int(num) for num in bt]

new=bt[-1]
for i in range(n-2):
    if bt[i]<= new and bt[i+1]>new:
        for j in range(n-1, i+1, -1):
            bt[j]=bt[j-1]
        bt[i+1]=new
        break
for i in bt:
    print(i,end=" ")
