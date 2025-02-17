class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            runner = current  
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next 
                else:
                    runner = runner.next  
            current = current.next  
        return head
