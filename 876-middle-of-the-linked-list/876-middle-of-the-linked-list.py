from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr.next != None:
            nums.append(curr.val)
            curr = curr.next
        nums.append(curr.val)
        flag = len(nums)//2
        curr = head
        # nums_dict = Counter(nums[:len(nums)//2+1])
        # flag_cnt = nums_dict[flag]
        # print(nums_dict)
        # print(flag, flag_cnt)
        cnt = 0
        while True:
            if(cnt == flag):
                return curr
            curr = curr.next
            cnt = cnt + 1
            # if curr.val == flag:
            #     flag_cnt = flag_cnt - 1
            #     if(flag_cnt == 0):
            #         return curr
            # curr = curr.next
            # if(curr == None):
            #     return head