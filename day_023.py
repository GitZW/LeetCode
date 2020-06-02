"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). Return a array containing all the linked lists.

 

Example:

Input: [1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

Output: [[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        if not tree:
            return

        queue = [(0, tree)]

        result = []
        list_node_cur = []
        while queue:
            depth, node = queue.pop(0)
            if depth <= len(result) - 1:
                list_node_cur_node = list_node_cur[depth]
                list_node_cur_node.next = ListNode(node.val)
                list_node_cur[depth] = list_node_cur_node.next

            else:
                list_node_cur_node = ListNode(node.val)
                result.append(list_node_cur_node)
                list_node_cur.append(list_node_cur_node)

            if node.left is not None:
                queue.append((depth + 1, node.left))
            if node.right is not None:
                queue.append((depth + 1, node.right))
        return result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7
node4.left = node8

s = Solution()
s.listOfDepth(node1)
