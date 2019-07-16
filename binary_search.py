# -*- coding: utf-8 -*-
# Seek



def binary_search(data, value):
    """
    二分查找
    data为已经排好序的数据
    value是需要查找的数据
    """

    res = -1
    if not data:
        return res

    low = 0
    high = len(data) - 1

    
    while low <= high:
        # 当low和hight都很大时防止溢出所以不写成(low+high)/2
        mid = low + (high - low)/2

        if data[mid] == value:
            res = mid

        if data[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return res


def cal_square(data):
    """
    计算data的平方根，精确到6位小数
    """

    low = 0
    high = data
    mid = low + (high - low) / 2
    res = 0
    while abs(mid ** 2 - data) > 0.000001:
        if mid ** 2 > data:
            high = mid - 1
        else:
            low = mid + 1

        res = mid
    return res


def find_first_equal(data, value):
    """
    二分查找变形：查找有序数组中第一个等于value的元素
    """
    if not data:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] > value:
            high = mid - 1
        elif data[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or data[mid - 1] != value:
                return mid
            else:
                high = mid -1


def find_last_equal(data, value):
    """
    二分查找变形：查找有序数组中最后一个等于value的元素
    """
    if not data:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] > value:
            high = mid - 1
        elif data[mid] < value:
            low = mid + 1
        else:
            if mid == n-1 or data[mid + 1] != value:
                return mid
            else:
                low = mid + 1


def find_first_greater_equal(data, value):
    """
    二分查找变形：查找有序数组中第一个大于等于value的元素
    """
    if not data:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] >= value:
            if mid == 0 or data[mid + 1] < value:
                return mid
            high = mid - 1
        else:
            low = mid + 1


def find_last_greater_equal(data, value):
    """
    二分查找变形：查找有序数组中最后一个大于等于value的元素
    """
    if not data:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] >= value:
            if mid == n-1 or data[mid + 1] < value:
                return mid
            low = mid + 1
        else:
            high = mid - 1


def find_last_smaller_equal(data, value):
    """
    二分查找变形：查找有序数组中最后一个小于等于value的元素
    """
    if not data:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] <= value:
            if mid == n-1 or data[mid + 1] > value:
                return mid
            low = mid + 1
        else:
            high = mid - 1


def find_value_in_cycle_sort_queue(data, value):
    """
    二分查找：循环有序数组中查找等于给定值的元素
    """
    res = []
    temp = []
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            temp.append(data[i])
        else:
            res.apend(binary_search(temp, value))
            temp = []
    return res








