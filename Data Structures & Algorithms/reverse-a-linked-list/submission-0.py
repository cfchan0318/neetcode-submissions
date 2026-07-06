# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head

        i = 0
        new_head = None

        while cur != None:
            nodes.append(cur)
            cur = cur.next

        while len(nodes) > 0:
            cur = nodes.pop()
            if len(nodes) == 0:
                cur.next = None
            else:
                cur.next = nodes[-1]

            if i == 0:
                new_head = cur

            i+=1
            
        return new_head
            

       