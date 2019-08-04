# -*- coding: utf-8 -*-
# 回溯算法


queen_result = [None] * 8

def check_queen(row, column):
    """
    八皇后校验方法
    """
    start_row = row - 1
    left = column - 1
    right = column + 1
    while start_row >= 0:
        if queen_result[start_row]:
            # 同行
            return False
        if queen_result[start_row] == column:
            # 同列
            return False
        if left >= 0 and queen_result[start_row] == left:
            # 左上对角线
            return False
        if right <= 8 and queen_result[start_row] == right:
            # 右上对角线
            return False

        left -= 1
        right += 1

    return True


def eight_queens(row):
    """
    八皇后
    """

    if row == 8:
        return

    for column in range(8):
        if check_queen(row, column):
            queen_result[row] = column
            eight_queens(row + 1)




# 初始最大背包中物品总价值
max_values = 0

# put_weight表示已经放进背包的物品重量
weight_list = list()

# put_values表示已经放进背包的物品总价值
values_list = list()

# item_cont表示物品总数
item_count = 15

# bearing_weight表示背包的最大承重
bearing_weight = 100

def zero_one_package(i, put_weight, put_values):
    """
    0-1背包问题变体
    i 表示当前处理的第几个物品
    weight_list表示物品的重量数据列表
    values_list表示物品的价值数据列表
    """
    if i >= item_count or put_weight >= bearing_weight:
        if put_values > max_values:
            max_values = put_values

    zero_one_package(i+1, put_weight, put_values)
    if put_weight + weight_list[i] <= bearing_weight:
        zero_one_package(i+1, put_weight + weight_list[i], put_values + values_list[i])


