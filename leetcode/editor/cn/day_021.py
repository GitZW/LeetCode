"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Example1:

 Input: n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 Output: true
Example2:

 Input: n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 Output true
Note:

0 <= n <= 100000
All node numbers are within the range [0, n].
There might be self cycles and duplicated edges.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
"""


class Solution:
    def findWhetherExistsPath(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        link_list = [[] for _ in range(n)]
        for n, v in graph:
            link_list[n].append(v)

        set_n = set()

        queue = [start]
        while queue:
            current_node = queue.pop()

            if target in link_list[current_node]:
                return True

            set_n.add(current_node)

            for node in link_list[current_node]:
                if node not in set_n:
                    queue.append(node)

        return False
