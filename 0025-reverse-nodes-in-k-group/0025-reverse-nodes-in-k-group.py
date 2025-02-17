from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def has_k_nodes(curr, k):
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            return count == k

        
        def reverse_k_nodes(start, k):
            prev = None
            curr = start
            while k > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k -= 1
            return prev  

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while has_k_nodes(prev_group.next, k):
            
            start = prev_group.next
            end = start
            for _ in range(k - 1):
                end = end.next

            
            next_group = end.next
            end.next = None  

            
            new_head = reverse_k_nodes(start, k)
            prev_group.next = new_head
            start.next = next_group

            
            prev_group = start

        return dummy.next
