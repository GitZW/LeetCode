# 有 N 个网络节点，标记为 1 到 N。 
# 
#  给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从
# 源节点传递到目标节点的时间。 
# 
#  现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# 输出：2
#  
# 
#  
# 
#  注意: 
# 
#  
#  N 的范围在 [1, 100] 之间。 
#  K 的范围在 [1, N] 之间。 
#  times 的长度在 [1, 6000] 之间。 
#  所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。 
#  
#  Related Topics 堆 深度优先搜索 广度优先搜索 图


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import collections
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        node_time = {i: float("inf") for i in range(1, N + 1)}

        def dfs(n, t):
            if t >= node_time[n]:
                return
            node_time[n] = t

            # 优化路径短的先计算
            for w, v in sorted(graph[n]):
                dfs(v, t + w)

        dfs(K, 0)
        ans = max(node_time.values())
        return ans if ans < float("inf") else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
s = Solution()
print(s.networkDelayTime(times, N, K))
