# -*- coding: utf-8 -*-
# Sort
import itertools



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


def merge_data(data, start, middle, end):
    """
    归并排序的合并算法
    """
    i, j = start, middle + 1
    tmp = []
    while i <= middle and j <= end:
        # 判断一定要加等号才能保证排序的结果是稳定的
        if data[i] <= data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1

    low = i if i <= middle else j
    high = middle if i <= middle else end
    a[low:high+1] = tmp


def merge_sort_helper(data, start, end):
    """
    归并排序的递归方法
    """
    if start >= end:
        return

    middle = (start + end) / 2
    merge_sort_helper(data, start, end)
    merge_sort_helper(data, middle+1, end)
    merge_data(data, start, middle, end)




def merge_sort(data, n):
    """
    归并排序
    n为数组data的长度
    """
    merge_sort_helper(data, 0, n-1)


def quick_sort_partition(data, start, end):
    """
    快速排序获取分区点下标方法
    """
    high = data[end]
    i = start
    while start <= j <= end-1:
        if data[j] < high:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[end] = data[end], data[i]
    return i



def quick_sort_helper(data, start, end):
    """
    快速排序递归方法
    """
    if start == end:
        return

    q = quick_sort_partition(data, start, end)
    quick_sort_helper(data, start, q - 1)
    quick_sort_helper(data, q + 1, end)



def quick_sort(data, n):
    """
    快速排序
    """
    quick_sort_helper(data, 0, n-1)



def counting_sort(data):
    """
    计数排序
    data为初始的数组
    """
    if not data or len(data) == 1:
        return data

    length = len(data)

    temp_list = [0] * (max(data) + 1)
    for num in data:
        temp_list[num] += 1

    # only support in py3
    # temp_list = list(itertools.accumulate(temp_list))
    for i in xrange(1, len(temp_list)):
        temp_list[i] = temp_list[i] + temp_list[i-1]


    result = [0] * length
    i = len(temp_list) - 1
    for num in data:
        result[temp_list[num] - 1] = num
        temp_list[num] -= 1

    return result

a1 = [1,2,3,4]
a2 = [1,1,1,1]
a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
print counting_sort(a1)
print counting_sort(a2)
print counting_sort(a3)












