# -*- coding: utf-8 -*-
# Queue



# 节点类
class Node(object):

    def __init__(self, value, next=None, *args, **kwargs):
        self.value = value
        self.next = next


# 基于链表的链式队列
class LinkedListQueue(object):

    def __init__(self, *args, **kwargs):
        self.head = Node(None)
        self.tail = Node(None)


    def enqueue(self, value):
        item = Node(value)
        item.next = self.head
        self.tail.next = item


    def dequeue(self):
        if self.head == self.tail:
            raise ValueError("Queue is Empty")

        pop_item = self.head.next
        self.head.next = pop_item.next
        return pop_item.value


# 基于链表循环队列
class CycleQueue(object):

    def __init__(self, *args, **kwargs):
        self.head = Node(None)
        self.tail = Node(None)
    

    def enqueue(self, value):
        if not self.tail.value and self.tail.next == self.head:
            raise ValueError("Queue is Full")

        item = Node(value)
        item.next = self.head
        self.tail.next = item
        


    def dequeue(self):
        if self.head == self.tail:
            raise ValueError("Queue is Empty")

        pop_item = self.head.next
        self.head.next = pop_item.next
        return pop_item.value        


