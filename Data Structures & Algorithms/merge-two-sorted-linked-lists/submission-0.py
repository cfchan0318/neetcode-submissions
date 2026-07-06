# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur3 = None
        new_head = None

        cur1 = list1
        cur2 = list2

        while cur1 is not None or cur2 is not None:
            ins = None

            if cur1 is None and cur2 is not None:
                ins = cur2
                cur2 = cur2.next
            elif cur2 is None and cur1 is not None:
                ins = cur1
                cur1 = cur1.next
            elif cur1.val < cur2.val:
                ins = cur1
                cur1 = cur1.next
            elif cur2.val < cur1.val:
                ins = cur2
                cur2 = cur2.next
            else:
                ins = cur1
                cur1 = cur1.next

            if cur3 == None:
                new_head = ins
                cur3 = ins
            else:
                cur3.next = ins
                cur3 = cur3.next

        return new_head
        