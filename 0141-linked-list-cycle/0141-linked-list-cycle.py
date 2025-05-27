# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize two pointers
        slow = head
        fast = head
        
        # Loop to check if the fast pointer reaches the end or if the two pointers meet
        while fast and fast.next:
            slow = slow.next        # Move slow pointer one step
            fast = fast.next.next   # Move fast pointer two steps
            
            if slow == fast:        # If slow and fast meet, there is a cycle
                return True
        
        return False  # If fast pointer reaches the end, no cycle exists
     