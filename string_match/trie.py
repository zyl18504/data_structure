# -*- coding: utf-8 -*-
# Trie



START_ASCII = ord('a')

class TrieNode(object):
    """
    Trie树结点
    假设data都是a-z的小写字母
    """
    def __init__(self, data, children=[], is_end=False):
        self.data = data
        self.children = [None] * 26
        self.is_end = is_end



def insert(data, root=None):
    """
    Trie树插入
    假设data是a-z的小写字母
    """
    if not root:
        root = TrieNode('/')

    parent = root
    for s in data:
        index = ord(s) - START_ASCII
        temp_node = TrieNode(s)
        if not parent.children[index]:
            parent.children[index] = temp_node
        parent = parent.children[index]

    parent.is_end = True



def get_find_node(data, root):
    if not root or not data:
        return

    parent = root
    for s in data:
        index = ord(s) - START_ASCII
        if not parent.children[index]:
            result = False
            break

        parent = parent.children[index]

    return parent


def find(data, root):
    """
    Trie树查找
    假设data是a-z的小写字母
    """
    node = get_find_node(data, root)
    return node.is_end



def get_children_suffix(node):
    parent = node
    result = ""
    for val in parent.children:
        if val:
            result = "{}{}".format(result, get_children_suffix(val))

    return result




def starts_with(s, root):
    """
    Trie树前缀模糊匹配
    假设data是a-z的小写字母
    """
    if not find(s, root):
        return

    node = get_find_node(s, root)
    result = []
    for node in node.children:
        result.append("{}{}".format(s, get_children_suffix(node)))

    return result

    













