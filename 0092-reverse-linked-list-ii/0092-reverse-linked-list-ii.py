class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy


        for _ in range(left - 1):
            prev = prev.next


        values = []
        current = prev.next
        for _ in range(right - left + 1):
            values.append(current.val)
            current = current.next

  
        values.reverse()


        current = prev.next
        for val in values:
            current.val = val
            current = current.next

        return dummy.next
