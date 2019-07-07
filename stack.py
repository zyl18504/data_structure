# -*- coding: utf-8 -*-
# Stack



# 节点类
class Node(object):

    def __init__(self, value, next, *args, **kwargs):
        self.value = value
        self.next = next


# 基于链表的栈
class LinkedListStack(object):

    def __init__(self, *args, **kwargs):
        self.top = Node(None)


    def add(self, node):
        node.next, self.top.next = self.top.next, node



    def remove(self):
        self.top.next = self.top.next.next
