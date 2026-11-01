class Node:
    def __init__(self, val = 0):
        self.value = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False

        new_node = Node(value)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.value if self.size > 0 else -1

    def Rear(self) -> int:
        return self.tail.value if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()