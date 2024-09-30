# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        #slow fast pointer tech
        slow = head
        fast = head
        #While there is a Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #If there's a cycle
            if slow == fast:
                return True
        #If not -- This automatically returns False if fast points to null
        return False

        