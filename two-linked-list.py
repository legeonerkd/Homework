class TwoLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class TwoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, node: TwoLinkedNode) -> None:
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert(self, node: TwoLinkedNode, pos: int) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return   
        if pos == 0:
            self.head.prev = node
            node.next = self.head
            self.head = node
        elif pos == -1:
            self.add_to_tail(node)
        else:
            cur = self.head
            index = 0
            while cur is not None:
                cur = cur.next
                index += 1
                if index == pos and cur.next is not None:
                    prev = cur.prev
                    cur.prev = node
                    node.next = cur
                    node.prev = prev
                    prev.next = node
                elif index == pos and cur.next is None:
                    self.add_to_tail(node)




            
    
    
    
    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def get_length(self) -> int:
        length = 0
        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next
        return length
        

        
lst = TwoLinkedList()
lst.insert(1,2)
lst.insert(2,0)
lst.insert(3,3)
lst.insert(4,1)
lst.insert(5,4)
lst.insert(6,6)
lst.insert(7,5)
lst.print()


# lst.print()
# print('Size: %d' % lst.get_length())
# lst.remove_by_value(3)
# lst.print()



