# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        #Return the second middle node (Even Linked List)

        #Slow and Fast Pointer Technique
        slow = head
        fast = head
        #While fast pointer is not pointing to null or next to
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow