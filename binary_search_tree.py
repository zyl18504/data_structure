# -*- coding: utf-8 -*-
# Binary Search Tree



# 节点类
class TreeNode(object):
    def __init__(self, data, left=None, right=None, *args, **kwargs):
        self.data = data
        self.left = left
        self.right = right



def search(root, data):
    """
    二叉查找树
    查找操作
    """
    node = root
    result = []
    while node:
        if data < node.data:
            node = node.left
        else:
            # 为了查处右子树中所有等于搜索值的结点，解决树中有重复结点的情况
            if data == node.data:
                result.append(node)

            node = node.right

    return result


def insert(root, data):
    """
    二叉查找树
    插入操作
    """
    node = root
    prev = root
    new_node = TreeNode(data)
    while node:
        prev = node
        node = node.left if data < node.data else node.right

    if prev.data < data:
        prev.left = new_node
    else:
        prev.right = new_node


def remove(root, data):
    """
    二叉查找树
    删除操作
    """
    node = root
    prev = root
    while node:
        prev = node
        if node.data == data:
            break
        node = node.left if data < node.data else node.right

    if not all(node.left, node.right):
        if node.left:
            child = node.left
        elif node.right:
            child = node.left
        else:
            child = None
    else:
        min = node.left
        temp_node = node.left
        temp_prev = node.left
        while temp_node:
            temp_prev = node
            if temp_node.data < min:
                temp_node = temp_node.left

        temp_prev.left = None
        child = temp_node

    if prev.left == p:
        prev.left = child
    elif prev.right == p:
        prev.right = child
