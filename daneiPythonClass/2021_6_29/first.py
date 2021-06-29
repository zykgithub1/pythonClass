# import sys
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class LinkedQue:
    def __init__(self):
        self.__front = Node(None)
        self.__tail = self.__front

    def enque(self, val):
        if self.isEmpty():
            node = Node(val)
            self.__front.next = node
            self.__tail = node
        else:
            self.__tail.next = Node(val)
            self.__tail = self.__tail.next

    def isEmpty(self):
        return self.__front == self.__tail

    def deque(self):
        if not self.isEmpty():
            self.__front = self.__front.next
            return self.__front.val

lq = LinkedQue()
lq.enque(1)
lq.enque(2)
lq.enque(3)
lq.enque(4)
lq.enque(5)
print(lq.deque())
print(lq.deque())
print(lq.deque())
a=112312.432342132
print("该数据为%.3f"%a)