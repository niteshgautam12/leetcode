class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        
        values = sorted(values)

        
        unique_values = []
        i = 0
        while i < len(values):
            if i + 1 < len(values) and values[i] == values[i + 1]:  
                while i + 1 < len(values) and values[i] == values[i + 1]:  
                    i += 1
            else:
                unique_values.append(values[i])  
            i += 1

        
        dummy = ListNode(0)
        current = dummy
        for val in unique_values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
