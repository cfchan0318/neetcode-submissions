class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)   # dummy head
        self.tail = ListNode(0)   # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def find(self, index:int):
        i = -1
        node = self.head
        while i< index:
            node = node.next
            i+=1
        return node

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        if index > self.size -1:
            return -1

        i = 0
        node = self.head.next
        while i< index:
            node = node.next
            i+=1
        return node.val

    def addAtHead(self, val: int) -> None:
        #init new head
        newHead = ListNode(val)
        newHead.next = self.head.next
        newHead.prev = self.head

        # set new Head as head
        self.head.next.prev = newHead
        self.head.next = newHead

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        
        #init new tail
        newTail = ListNode(val)
        newTail.next = self.tail
        newTail.prev = self.tail.prev

        # set new Tail as tail
        self.tail.prev.next = newTail
        self.tail.prev = newTail

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return

        next_node = self.find(index)
        prev_node = self.find(index-1)

        node = ListNode(val)
        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return

        node = self.find(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)