# -*- coding: utf-8 -*-
# Sort



def bubble_sort(data):
    """
    冒泡排序
    """
    if not data or len(data) == 1:
        return data

    for i in range(len(data)):
        swap = False
        for n in range(len(data) - i - 1):
            if data[n] > data[n+1]:
                data[n], data[n+1] = data[n+1], data[n]
                swap = True

        if not swap:
            break

    return data


def insert_sort(data):
    """
    插入排序
    tips: 重点在数据移动
    """
    if not data or len(data) == 1:
        return data

    for i in range(1, len(data)):
        start = data[i]
        n = i - 1
        while n >= 0 and a[n] < a[i]:
            a[n + 1] = a[i]
            n -= 1
        a[n + 1] = start

    return data



def selection_sort(data):
    """
    选择排序
    tips: 每次只交换一次
    """
    if not data or len(data) == 1:
        return data

    for i in range(0, len(data)):
        min_index = i
        min_value = a[i]
        for n in range(i+1, len(data)):
            if a[n] < a[i]:
                min_value = a[n]
                min_index = n

        a[i], a[min_index] = a[min_index], a[i]

    return data









