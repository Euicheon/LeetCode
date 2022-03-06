# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head): return head
        val = head.val
        if(not head.next): return head
        rev = self.reverseList(head.next)
        tail = ListNode(val)
        temp = rev
        while temp.next:
            temp = temp.next
        temp.next = tail
        # rev.next = tail
        # print(rev,val)
        return rev
            