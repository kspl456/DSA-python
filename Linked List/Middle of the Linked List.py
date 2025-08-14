#Middle of the Linked List
'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleNode(head):
    if head==None: return head
    s,f=head,head
    while f.next and f.next.next:
        f=f.next.next
        s=s.next
    if f.next==None: return s
    return s.next

'''
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Initialize two pointers, slow and fast, both pointing to the head of the linked list.
2. Move the slow pointer one step at a time and the fast pointer two steps at atime.
3. If the fast pointer's next next node is null, then there are even number of nodes. Return slow pointer's next node as it is the second middle node.
4. If the fast pointer's next node is null, then there are odd number of nodes. Return s as it is the middle node.
'''