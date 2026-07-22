# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr:
            temp = curr
            while temp.next :
                if temp.next.val == curr.val:
                    temp.next = temp.next.next
                else :
                    temp = temp.next
            curr = curr.next
        return head


        