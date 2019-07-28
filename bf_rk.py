# -*- coding: utf-8 -*-
# 字符串匹配算法


def bk_match(data, match_str):
    """
    BK算法
    """
    if not data or not match_str:
        return

    if len(match_str) > len(data):
        return

    total_length = len(data)
    match_length = len(match_str)
    forloop_length = total_length - match_length + 1
    found = -1
    for i in range(forloop_length):
        if data[i:i+match_length] == match_str:
            found = i
            break

    return found


def rk_hash(data, start, end):
    return hash(data[start:end+1])



def rk_match(data, match_str):
    """
    RK算法
    """
    if not data or not match_str:
        return

    if len(match_str) > len(data):
        return

    total_length = len(data)
    match_length = len(match_str)
    forloop_length = total_length - match_length + 1
    hash_list = [rk_hash(data, i, i+m-1) for i in range(forloop_length)]
    match_hash = rk_hash(match_str, 0, match_length-1)
    found = -1
    for i in range(forloop_length):
        if hash_list[i] == match_hash:
            found = i
            break
            
    return found
