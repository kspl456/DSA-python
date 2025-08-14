#Linked List Cycle
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(head):
        if head==None or head.next==None: return False
        s=f=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                return True
        return False

'''
Approach:
Initialize fast and slow pointers to the head of the linked list.

fast and slow are initially pointing to the head of the linked list, which is the starting point.
Enter a loop while both fast and fast.next are not null.

This loop will continue until either fast or fast.next becomes null, indicating the end of the linked list or if there is no cycle.
Move the fast pointer two steps ahead (fast = fast.next.next) and the slow pointer one step ahead (slow = slow.next).

This step simulates the two-pointer traversal where fast moves twice as fast as slow.
Check if fast is equal to slow.

If fast and slow pointers meet at the same node, it means there is a cycle in the linked list, and we return True.
If the loop exits without finding a cycle, return False.

If the loop completes without finding a cycle, it means that the fast pointer has reached the end of the list, and there is no cycle. In this case, we return False

Time Complexity: O(n)
Space Complexity: O(1)
'''