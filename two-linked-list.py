
class EmptyListError(Exception):
    pass


class TwoLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class TwoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: TwoLinkedNode) -> None:
        if self.head is not None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            return

    def insert(self, node: TwoLinkedNode, pos: int) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return   
        if pos == 0:
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        elif pos == -1:
            self.append(node)
            return
        cur = self.head
        index = 0
        while cur is not None:
            cur = cur.next
            index += 1
            if index == pos:
                if cur.next is not None:
                    prev = cur.prev
                    cur.prev = node
                    node.next = cur
                    node.prev = prev
                    prev.next = node
                    return
                self.append(node)
                    
    def remove_tail(self):
        if self.tail is None:
            raise EmptyListError()
        self.tail = self.tail.prev
        self.tail.next = None
        if self.tail is None:
            self.head = None
           
    def remove_by_pos(self, pos: int):
        if pos < -1:
            raise IndexError()
        if self.head is None:
            raise EmptyListError()
        if pos == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        elif pos == -1:
            self.remove_tail()   
            return
        cur = self.head
        index = 0
        while cur != self.tail:
            if index == (pos - 1):
                if cur.next is not None:
                    follow = cur.next.next
                    cur.next = follow
                    follow.prev = cur
                else:
                    self.remove_tail()
                return
            cur = cur.next
            index += 1
        raise IndexError()

    
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
#lst.insert(1, 2)
#lst.insert(2, 0)
#lst.insert(3, 3)
#lst.insert(4, 1)
# lst.insert(5, 4)
# lst.insert(6, 6)
# lst.insert(7, 5)
# lst.print()
try:
    lst.remove_by_pos(2)
except EmptyListError:
    print('What the fuck')



