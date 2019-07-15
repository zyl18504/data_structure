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

    # 当low和hight都很大时防止溢出所以不写成(low+high)/2s
    mid = low + (high - low)/2
    while low <= high:
        if data[mid] == value:
            res = mid

        if a[mid] > value:
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



