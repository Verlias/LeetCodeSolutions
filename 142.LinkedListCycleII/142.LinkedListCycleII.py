# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        #slow fast pointer tech
        slow = head
        fast = head
        #In a Cycle
        while fast and fast.next:
            #Iterate to Determine Cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        #If fast pointers are pointing to null or next to (Means no Cycle)
        if not fast or not fast.next:
            return None

        #Find the node where the cycle begins. Return when slow2 and slow are on same nodes
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next    

        return slow

        