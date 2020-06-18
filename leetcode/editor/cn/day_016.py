"""
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Example 3:

Input: head = [1], pos = -1
Output: no cycle
Follow Up:
Can you solve it without using additional space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        set_node = set()
        while head:
            if head in set_node:
                return head
            set_node.add(head)
            head = head.next

        return None



class Solution2:
    """
    参考 https://blog.csdn.net/wuzhekai1985/article/details/6725263
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        p1 = head
        p2 = head
        flag = False
        while p1 and p1.next and p2:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                flag = True
                break
        if not flag: return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2


