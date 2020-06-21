# 堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最
# 高的一堆箱子。箱堆的高度为每个箱子高度的总和。 
# 
#  输入使用数组[wi, di, hi]表示每个箱子。 
# 
#  示例1: 
# 
#   输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#  输出：6
#  
# 
#  示例2: 
# 
#   输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
#  输出：10
#  
# 
#  提示: 
# 
#  
#  箱子的数目不大于3000个。 
#  
#  Related Topics 动态规划 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
import functools


class Solution(object):
    def pileBox(self, box):
        """
        # 动态规划
        :type box: List[List[int]]
        :rtype: int
        """
        if not box:
            return 0
        box.sort(reverse=True, key=lambda i: (i[0], -i[1]))
        box_num = len(box)
        # h[i] 表示第i个箱子是最大高度
        h = [0] * box_num
        h[0] = box[0][2]
        for i in range(box_num):
            h[i] = box[i][2]
            for j in range(i):
                if box[i][1] < box[j][1] and box[i][2] < box[j][2]:
                    h[i] = max(h[i], h[j] + box[i][2])

        return max(h)


class Solution2(object):
    def pileBox(self, box):
        @functools.lru_cache(maxsize=3000)
        def sol(w, d, h):
            inners = [(iw, id, ih) for iw, id, ih in box if iw < w and id < d and ih < h]
            if not inners:
                return h
            return max((sol(*i) for i in inners)) + h

        return max((sol(*i) for i in box))


box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
box.sort(reverse=True, key=lambda i: (i[0], -i[1]))

s = Solution2()
print(s.pileBox([[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]))
