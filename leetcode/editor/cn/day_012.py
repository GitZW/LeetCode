"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

Example:

Input: head = 3->5->8->5->10->2->1, x = 5
Output: 3->1->2->5->5->8->10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        current_node = head

        while current_node.next:
            if current_node.next.val < x:
                tmp_node = current_node.next
                current_node.next = tmp_node.next
                tmp_node.next = head
                head = tmp_node
            else:
                current_node = current_node.next

        return head


class Solution2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 双链表实现，小于x的组成一链表，大于x的组成另一链表，然后两链表拼接
        if not head:
            return head
        fnode = ListNode(-1)
        snode = ListNode(-1)
        first = fnode
        second = snode
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next

        first.next = snode.next
        second.next = None

        return fnode.next



node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

s = Solution()
s.partition(head, 3)
