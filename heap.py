# -*- coding: utf-8 -*-
# Heap Sort



def heapify(data, start):
    """
    堆化函数
    结果堆化出一个大顶堆
    """
    while True:
        max_pos = start
        if start * 2 <= len(data) and data[start] < data[start*2]:
            start = start * 2
        if start * 2 + 1 <= len(data) and data[start] < data[start*2+1]:
            start = start * 2 + 1

        if max_pos == start:
            break

        data[max_pos], data[start] = data[start], data[max_pos]


def build_heap(data):
    """
    构建一个大顶堆
    """
    sorts = range(1, len(data/2) + 1)
    for i in reversed(sorts):
        heapify(data, i)


def heap_insert(heap, value):
    """
    大顶堆中插入一个元素
    """
    heap.append(value)
    start = len(heap) - 1
    while start / 2 >=0 and a[start] > a[start/2]:
        a[start], a[start/2] = a[start/2], a[start]
        start = start / 2


def heap_remove(heap):
    """
    大顶堆删除堆顶元素
    """
    if not heap:
        return
    heap[1], heap[-1] = heap[-1], heap[1]
    heap = heap[:-2]
    heapify(heap, 1)


def heap_sort(data):
    """
    堆排序
    """
    heap = build_heap(data)
    length = len(data)
    while length >= 1:
        heap[1], heap[-1] = heap[-1], heap[1]
        length -= 1
        heapify(heap, 1)


            

