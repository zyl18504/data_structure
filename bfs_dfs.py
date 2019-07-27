# -*- coding: utf-8 -*-
# BFS & DFS


class Graph(object):
    """
    v 表示顶点的个数
    adj表示顶点的邻接表
    """
    def __init__(self, v, adj):
        self.v = v
        self.adj = adj
        self.dfs_found = False
        


    def _bfs_search(self, start, end):
        """
        广度优先搜索
        """
        if start == end:
            return

        visited_v = [0] * self.v
        visited_q = deque()
        visited_v[start] = 1
        visited_q.append(start)
        prev_q = [-1] * self.v


        while visited_q:
            next_v = visited_q.popleft()
            for v in self.adj[v]:
                prev_q[v] = next_v
                if v == end:
                    return
                visited_q.append(v)
                visited_v[v] = 1


    def _dfs_search(self, start, end):
        """
        深度优先搜索
        """
        if start == end:
            return

        visited_v = [0] * self.v
        visited_q = [start]
        visited_v[start] = 1
        prev_q = [-1] * self.v

        self.__dfs_recurit(start, end, visited_q, prev_q)


    def __dfs_recurit(self, start, end, visitied_q, prev_q):
        """
        深度优先搜索递归函数
        """
        if self.dfs_found:
            return

        visitied_q[start] = 1
        if start == end:
            self.dfs_found = True
            return

        for v in self.adj[start]:
            if not visitied_q[v]:
                prev_q[v] = start
                self.__dfs_recurit(v, end, visitied_q, prev_q)

            



